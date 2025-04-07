import os
import logging
import re
import random
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import random
import templates
import extract_prompts
import fetch_from_pexels
import hashlib

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get the Pexels API key from the .env file
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def generate_code_from_azure_ai(prompt: str, index) -> dict:
    """Generate code using Azure AI Inference SDK."""
    try:
        # Get Azure AI credentials and endpoint
        token = os.getenv("GITHUB_TOKEN")  # Use your GitHub token (or Azure key if different)
        endpoint = "https://models.inference.ai.azure.com"
        model_name = "DeepSeek-V3"

        # Initialize the client
        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        # Define the chat messages with enhanced image and video instructions
        # i = random.randint(0, 9)
        # i = int(hashlib.md5(prompt.encode()).hexdigest(), 16) % 10

        messages = [
            SystemMessage("You are an expert React developer. Generate a complete React project structure with separate files for components, styles, and entry points. For any images or videos in your components, follow these guidelines:\n\n1. Use responsive techniques:\n   - Set images/videos to have width='100%' (or appropriate percentage) and height='auto'\n   - Use Tailwind CSS classes for proper sizing and responsive behavior\n   - Include max-width properties to prevent oversizing\n\n2. For each <img> or <video> tag :\n   - Include descriptive alt attributes (use a single phrase of at least 2 words that best describes the image/video, and if using Array.fill(), ensure each item includes an alt tag, e.g., Array(6).fill({ src: 'https://via.placeholder.com/400x400', alt: 'Sample placeholder image' }))\n   - Include className attributes for styling\n   - Use 'https://via.placeholder.com/800x600' as placeholder URLs\n\n3. Include responsive design principles in your Tailwind CSS\n\nUse the following format for each file:\n\n```src/components/Header.js\n// Header.js code here\n```\n\n```src/components/Hero.js\n// Hero.js code here\n```\n\n```src/App.js\n// App.js code here\n```\n\n```src/index.js\n// index.js code here\n```\n\n```src/App.css\n// App.css code here\n```\n\n```public/index.html\n// index.html code here\n```\n\n```package.json\n// package.json code here\n```"),
            UserMessage(f"Create a React project for: {prompt}. Use the following design template:\n\n{templates.design_templates[index]['description']}\n\nEnsure all components are placed in the 'src/components' folder which are imported into App.js and also include index.js inside src. Make sure to include relevant images and videos with descriptive alt tags (single word) and placeholder URLs. Provide the folder structure and file paths in the response."),
        ]

        # Send the request to the model
        response = client.complete(
            messages=messages,
            model=model_name,
        )

        # Validate response structure
        if not response.choices or not response.choices[0].message or not response.choices[0].message.content:
            raise Exception("Azure AI API returned an empty response.")

        # Extract generated content
        generated_text = response.choices[0].message.content.strip()

        # Parse the generated code into separate files
        project_files = parse_generated_code(generated_text)
        
        # Replace placeholder images and videos with real URLs from Pexels
        project_files = replace_placeholders(project_files, PEXELS_API_KEY)
        
        return project_files

    except Exception as e:
        raise Exception(f"Error from Azure AI Inference API: {str(e)}")

    finally:
        client.close()


def parse_generated_code(generated_text: str) -> dict:
    """Parse the generated code into separate files for a React project."""
    project_files = {}

    # Use regex to extract code blocks
    matches = re.findall(r"```(.*?)\n(.*?)```", generated_text, re.DOTALL)
    for file_path, content in matches:
        file_path = file_path.strip()
        content = content.strip()

        # Add the file to the project_files dictionary
        project_files[file_path] = content

    return project_files

def replace_placeholders(project_files: dict, api_key: str) -> dict:
    """Replace all placeholder image and video URLs with real ones from Pexels."""

    # Extract prompts for images and videos
    image_prompts = extract_prompts.extract_image_prompts(project_files)
    video_prompts = extract_prompts.extract_video_prompts(project_files)
    logging.info(f"Image prompts: {image_prompts}")
    logging.info(f"Video prompts: {video_prompts}")

    image_url_cache = {}

    # Replace placeholder image URLs
    for file_path, content in project_files.items():
        updated_content = content

        # Generic regex for matching all src/alt style placeholders
        matches = re.findall(
            r'src\s*[:=]\s*["\'](https://via\.placeholder\.com/(\d+)(x(\d+))?)["\']\s*,?\s*alt\s*[:=]\s*["\']([^"\']+)["\']',
            content
        )

        for full_match, dim, width, _, alt in matches:
            prompt = alt.strip()
            if prompt not in image_url_cache:
                try:
                    image_url = fetch_from_pexels.fetch_image_from_pexels(prompt, api_key)
                    image_url_cache[prompt] = image_url
                    logging.info(f"Fetched image for prompt '{prompt}': {image_url}")
                except Exception as e:
                    logging.error(f"Failed to fetch image for prompt '{prompt}': {str(e)}")
                    continue
            else:
                image_url = image_url_cache[prompt]

            height = dim.split('x')[1] if 'x' in dim else width
            photo_id = image_url.split('/')[-2]
            sized_url = (
                f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg"
                f"?auto=compress&cs=tinysrgb&w={width}&h={height}&fit=crop"
            )

            updated_content = updated_content.replace(full_match, sized_url)

        project_files[file_path] = updated_content

    # Replace video placeholders
    for prompt in video_prompts:
        try:
            video_url = fetch_from_pexels.fetch_video_from_pexels(prompt, api_key)
            logging.info(f"Fetched video for prompt '{prompt}': {video_url}")
        except Exception as e:
            logging.error(f"Failed to fetch video for prompt '{prompt}': {str(e)}")
            continue

        for file_path, content in project_files.items():
            updated_content = content

            updated_content = re.sub(
                r'src="https://via\.placeholder\.com/[^"]*"',
                f'src="{video_url}"',
                updated_content
            )

            updated_content = re.sub(
                r'<source[^>]*src="https://via\.placeholder\.com/[^"]*"[^>]*>',
                f'<source src="{video_url}" type="video/mp4">',
                updated_content
            )

            project_files[file_path] = updated_content

    return project_files
