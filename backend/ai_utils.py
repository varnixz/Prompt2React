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

def generate_code_from_azure_ai(prompt: str) -> dict:
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
        i = int(hashlib.md5(prompt.encode()).hexdigest(), 16) % 10

        messages = [
            SystemMessage("You are an expert React developer. Generate a complete React project structure with separate files for components, styles, and entry points. For any images or videos in your components, follow these guidelines:\n\n1. Use responsive techniques:\n   - Set images/videos to have width='100%' (or appropriate percentage) and height='auto'\n   - Use CSS classes for proper sizing and responsive behavior\n   - Include max-width properties to prevent oversizing\n\n2. For each <img> or <video> tag:\n   - Include descriptive alt attributes (use a single word that best describes the image/video)\n   - Include className attributes for styling\n   - Use 'https://via.placeholder.com/800x600' as placeholder URLs\n\n3. Include responsive design principles in your CSS\n\nUse the following format for each file:\n\n```src/components/Header.js\n// Header.js code here\n```\n\n```src/components/Hero.js\n// Hero.js code here\n```\n\n```src/App.js\n// App.js code here\n```\n\n```src/index.js\n// index.js code here\n```\n\n```src/App.css\n// App.css code here\n```\n\n```public/index.html\n// index.html code here\n```\n\n```package.json\n// package.json code here\n```"),
             UserMessage(f"Create a React project for: {prompt}. Use the following design template:\n\n{templates.design_templates[i]['description']}\n\nEnsure all components are placed in the 'src/components' folder which are imported into App.js and also include index.js inside src. Make sure to include relevant images and videos with descriptive alt tags (single word) and placeholder URLs. Provide the folder structure and file paths in the response."),
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
    """Replace placeholder image and video URLs with real URLs from Pexels."""
    # Extract image-related prompts from <img> tags
    image_prompts = extract_prompts.extract_image_prompts(project_files)
    logging.info(f"Extracted image prompts: {image_prompts}")

    # Extract video-related prompts from <video> tags
    video_prompts = extract_prompts.extract_video_prompts(project_files)
    logging.info(f"Extracted video prompts: {video_prompts}")

    # Replace placeholder image URLs with real image URLs
    for prompt in image_prompts:
        try:
            # Fetch image from Pexels
            image_url = fetch_from_pexels.fetch_image_from_pexels(prompt, api_key)
            logging.info(f"Fetched image URL for prompt '{prompt}': {image_url}")

            # Replace placeholder image URLs in the project files
            for file_path, content in project_files.items():
                if f'alt="{prompt}"' in content:  # Find the <img> tag with the matching alt text
                    # Log the file and content before replacement
                    logging.info(f"Replacing image placeholder in file: {file_path}")
                    
                    # Extract the placeholder URL dimensions if available
                    placeholder_match = re.search(r'src="(https://via\.placeholder\.com/([^"]+))"', content)
                    
                    if placeholder_match:
                        placeholder_url = placeholder_match.group(1)
                        placeholder_dim = placeholder_match.group(2)
                        
                        # Check if the placeholder has dimensions in the format WIDTHxHEIGHT
                        if 'x' in placeholder_dim:
                            width, height = placeholder_dim.split('x')
                            
                            # Use the Pexels resize URL to get image with appropriate dimensions
                            photo_id = image_url.split('/')[-2]
                            sized_image_url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w={width}&h={height}&fit=crop"
                        else:
                            # If no dimensions in expected format, use the original image URL
                            sized_image_url = image_url
                        
                        # Replace the specific placeholder URL with the sized image URL
                        updated_content = content.replace(placeholder_url, sized_image_url)
                    else:
                        # If no placeholder URL found, use the original image URL
                        updated_content = re.sub(
                            r'src="https://via\.placeholder\.com/[^"]*"',
                            f'src="{image_url}"',
                            content
                        )
                    
                    # Log the updated content
                    logging.info(f"Content after replacement:\n{updated_content}")

                    # Update the project files dictionary
                    project_files[file_path] = updated_content

        except Exception as e:
            logging.error(f"Error replacing image for prompt '{prompt}': {str(e)}")

    # Replace placeholder video URLs with real video URLs
    for prompt in video_prompts:
        try:
            # Fetch video from Pexels
            video_url = fetch_from_pexels.fetch_video_from_pexels(prompt, api_key)
            logging.info(f"Fetched video URL for prompt '{prompt}': {video_url}")

            # Replace placeholder video URLs in the project files
            for file_path, content in project_files.items():
                if f'alt="{prompt}"' in content:  # Find the <video> tag with the matching alt text
                    # Log the file and content before replacement
                    logging.info(f"Replacing video placeholder in file: {file_path}")
                    
                    # Case 1: Replace <video> tags with a `src` attribute
                    if 'src="https://via.placeholder.com/' in content:
                        updated_content = re.sub(
                            r'src="https://via\.placeholder\.com/[^"]*"',
                            f'src="{video_url}"',
                            content
                        )
                    # Case 2: Replace <video> tags with a <source> element
                    elif '<source src="https://via.placeholder.com/' in content:
                        updated_content = re.sub(
                            r'<source[^>]*src="https://via\.placeholder\.com/[^"]*"[^>]*>',
                            f'<source src="{video_url}" type="video/mp4">',
                            content
                        )
                    else:
                        logging.warning(f"No placeholder found for video with alt='{prompt}' in file: {file_path}")
                        continue
                    
                    # Log the updated content
                    logging.info(f"Content after replacement:\n{updated_content}")

                    # Update the project files dictionary
                    project_files[file_path] = updated_content

        except Exception as e:
            logging.error(f"Error replacing video for prompt '{prompt}': {str(e)}")

    return project_files