import os
import zipfile
import logging
import re
import requests
import shutil  # For deleting directories and files
import random
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get the Pexels API key from the .env file
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

# Design templates (unchanged)
design_templates = [
    {
        "name": "1",
        "description": "Design a fully responsive, modern minimalist website with a clean aesthetic, structured layout, and smooth interactions using React with Tailwind CSS. Ensure a modular and scalable structure with sections including a fixed Header (80px height, white background, black text, Montserrat/Poppins font) featuring a centered text-based logo (not an image), navigation links (uppercase, spaced, 16px font), and a responsive hamburger menu for mobile. The Hero Section or a related section based on the prompt should have a full-width 1920x800px banner with an overlay effect, a large uppercase heading (48px font), a subtitle (20px font), and smooth fade-in animation. The About Section or equivalent should be centered, with a white background, a max width of 800px, a 32px italic heading, 16px body text, and a 50px divider line. The Portfolio Section or related section should use a grid-based layout on a white background, displaying responsive 400x400px images with hover effects including scale-up and box-shadow. The Clients Section or related section should be full-width with a white background, featuring an auto-scrolling testimonial slider every 5 seconds if needed and client logos (150x100px, grayscale turning full color on hover) in a responsive grid. The Contact Section should have centered text on a white background, a 32px italic heading, an email form with input fields (border-radius: 5px), and a ‘Subscribe Now’ button with hover effects. The Features Section should be dark-themed, showcasing key offerings such as Free Shipping, 24/7 Availability, and Best Prices (or adjusted content based on the prompt) in a three-column grid with icons, short descriptions, and star ratings. The Footer Section should have centered text on a soft background, including copyright information and social media icons with hover opacity effects. Ensure full responsiveness for different screen sizes, including desktop (1920px layout), tablet (768px, 2x2 grid), and mobile (375px, single-column with a hamburger menu), with smooth fade-in animations on page load, smooth scrolling, and hover effects on buttons, images, and social icons. Maintain accessibility compliance and write clean, scalable code. Provide the Tailwind CSS configuration file along with all necessary files for the React app to function, including index.css containing Tailwind base, components, and utilities, a public folder, and index.html, ensuring all images strictly include an alt tag."
    },
    {
        "name": "2",
        "description": "Create a fully responsive website with a modern design using a clean font and structured layout, styled with Tailwind CSS. The website should include a horizontal top navigation bar with proper spacing, a hero section featuring a large heading, a responsive hamburger menu for mobile, and a background color of `#F5F5F5` with font color `#333333`. Add a Services Section or a relevant section based on the prompt, containing three service cards with a background color of `#FFFFFF` and font color `#333333`. Include a Portfolio or 'Our Work' section or its equivalent, utilizing a grid layout to display images (each with a title, description, and alt tag) with a background color of `#F5F5F5` and font color `#333333`, ensuring the section title dynamically adjusts based on the prompt. The 'About Us' section or its alternative should follow a two-column layout with text on the left and a placeholder image on the right, using a background color of `#FFFFFF` and font color `#333333`, with a customizable title. Add a dark-themed Features Section or its equivalent, designed as a three-column grid showcasing key offerings such as Free Shipping, 24/7 Availability, and Best Prices, or other relevant features according to the website’s purpose, with icons, short descriptions, and star ratings. The Contact Section should include a form with fields for First Name, Last Name, Email, Subject, and Message, along with a submit button, using a background color of `#F5F5F5` and font color `#333333`. Lastly, incorporate a footer with a background color of `#333333` and font color `#FFFFFF`. Ensure full responsiveness across all devices, implement modern typography, and strictly include alt tags for all images. Provide all necessary files for the React app, including the Tailwind CSS configuration file, an index.css file containing Tailwind base, utilities, and components, a public folder, and an index.html file to ensure proper functionality."
    },
    {
        "name": "3",
        "description": "Create a fully responsive modern website with a minimalist and elegant UI using a black, white, and pastel green color scheme, built with Tailwind CSS. The website should include sections such as Header, Hero, Content, Booking, and Contact, with section titles dynamically adjusted based on the prompt. Ensure a full-width layout, consistent padding, and a scalable structure. The Header (80px height, full width, flexbox layout) should contain a text-based logo (150px width) on the left, evenly spaced menu links (uppercase, 16px font) in the center, and social media icons, a cart icon, and a login button on the right. The Hero Section or its equivalent (full-screen height, flex layout, centered alignment) should feature a grayscale image (100% width, 80vh height), an overlay text box (400px width, 250px height, semi-transparent background, bold uppercase text, 36px font), and a call-to-action button (200px width, rounded corners, hover animation). The Content Section or its equivalent (two-column flex layout, 60vh height) should include a background image on the left (60% width, 100% height, with overlay stripes), while the right side contains a text block (500px width, 24px font, justified text) with a fade-in animation. The Booking Section or its equivalent (full-width, 500px height, black background) should include a calendar UI (300px width, 400px height, grid layout, selectable dates with hover effects), a dropdown for service selection or a relevant input based on the website's title (250px width, white background, rounded edges), and a confirmation button (180px width, green color, hover transition). The Contact Section (black background, 400px height, grid layout) should display address details on the left (300px width, white text, 18px font) and a contact form on the right (400px width, input fields with 100% width, white borders, 14px font, and a submit button with a hover effect). Additionally, include a Features Section or equivalent, styled with a dark theme, showcasing a three-column grid highlighting key offerings such as Free Shipping, 24/7 Availability, or Best Prices using icons, short descriptions, and star ratings. The Footer (full width, 60px height) should be center-aligned with copyright text and social media icons. Ensure full responsiveness across all devices, use a modern font, and include alt tags for all images. Provide all necessary files for the React app, including the Tailwind CSS configuration file, an index.css file with Tailwind base, utilities, and components, a public folder, and an index.html file to ensure proper functionality."
    },
    {
        "name": "4",
        "description": "Create a fully responsive modern website with a clean, professional UI using a black, white, and gold color scheme, built with React and Tailwind CSS. The website should feature sections like Header, Hero, Services, Features, Highlights, and Testimonials, with section titles adjusted based on the prompt, ensuring a full-width layout, modular components, scalable structure, and full responsiveness across devices. The Header (80px height, full width, flexbox layout, white background) should include a text-based logo on the left, evenly spaced navigation links (uppercase, 16px font) in the center, and a call-to-action button or contact details on the right. The Hero Section or equivalent (full-screen height, two-column grid layout) should feature a dark background text box (600px width, 300px height, bold uppercase text, 36px font) with a call-to-action button (200px width, gold background, rounded corners, hover effect) on the left, and an image or grid-style gallery (600px width, 300px height) on the right, ensuring that the image has a higher z-index so it does not get overlapped by other sections. The Services Section or equivalent (two-row, three-column grid, 500px height, white background) should include six service cards (250px width, 200px height, gray background, black icons, title text 20px, description 14px font). The Features Section or equivalent (two-column flex layout, 500px height, light gray background) should contain a text block (500px width, 24px font, left-aligned) on the left and an image block (500px width, full height) on the right. The Highlights Section or equivalent (two-row, two-column grid, 600px height, white background) should display four cards (300px width, 250px height, images with overlay gold text boxes, title in bold 18px, description 14px font), with fixed cards having a z-index higher than the text below to avoid overlap issues. The Testimonials Section or equivalent (full-width, 400px height, white background) should feature three testimonial cards (400px width, 150px height, italicized text, client name in bold 16px, arrows for navigation). Additionally, include a Features Section or equivalent with a dark theme, showcasing a three-column grid highlighting key offerings (e.g., Free Shipping, 24/7 Availability, Best Prices per prompt) using icons, short descriptions, and star ratings. The Footer (black background, 300px height, flex layout) should display the business name in gold on the left, contact details (phone, email, social icons) in the center, and navigation links (categories or pages) on the right, with a centered copyright notice at the bottom. Ensure all images include alt tags for accessibility. Use proper z-index handling to prevent text overlap in the home image and highlight page, ensuring a smooth user experience. Provide all necessary React app files, including a Tailwind CSS configuration file, an index.css file with Tailwind base, utilities, and components, a public folder, and an index.html file to ensure proper functionality."
    },
    {
        "name": "5",
        "description": "Create a fully responsive modern website using React and Tailwind CSS, featuring an elegant serif typography, soft neutral color palette, and a grid-based layout with full-width elements, split-screen designs, hover animations, and smooth scrolling effects. The website should include modular components and a scalable structure with sections like Header, Hero, About, Expertise, Gallery, and Footer (section titles adjustable per prompt). The Header (80px height, transparent background, fixed on scroll) should have a minimal logo centered as text, navigation links (uppercase, spaced, 16px font) on the left, and social media icons on the right. The Hero Section or equivalent (full-screen height, centered text, soft gray background) should showcase a large serif heading (48px font, black text), subtext (18px font), and a carousel of high-quality images (600px width) with navigation buttons. The About Section or equivalent (two-column layout, 600px height, alternating text and images, white background) should feature a left-aligned image and a right-aligned text block (serif font, 20px size, italics for emphasis), followed by a signature-style image. The Expertise Section or equivalent (full-width, beige background, stacked text format) should display large uppercase words (bold, 36px font, black text) with smooth hover effects and a subtle shadow. The Gallery Section or equivalent (grid layout, white background) should present curated images (300px width, soft shadows, hover zoom effect) with captions in a clean serif font. Additionally, include a dark-themed Features Section or equivalent with a three-column grid highlighting key offerings (e.g., Free Shipping, 24/7 Availability, Best Prices, or per prompt), using icons, short descriptions, and star ratings. The Footer (soft beige background, 300px height, split into three columns) should contain navigation links, contact details (email, phone, location), and social media icons, ending with a centered brand name (elegant serif, 40px font). Ensure all images include alt tags for accessibility. Provide all necessary React app files, including a Tailwind CSS configuration file, an index.css file with Tailwind base, utilities, and components, a public folder with an index.html file, and other essential assets to ensure full functionality."
    },
    {
        "name": "6",
        "description": "Develop a fully responsive, modern minimalist website using React and Tailwind CSS, featuring a disappearing top navigation bar (80px height, white background, black text, Montserrat/Poppins font) with links like Home, About, Portfolio, Clients, and Contact (modifiable per prompt) along with a hamburger menu. The navigation bar should disappear on scroll down and reappear on scroll up. The website should include a full-width Hero Section or equivalent (1920x800px banner, overlay effect, centered title in 48px uppercase, subtitle in 20px, smooth fade-in animation), an About Section or equivalent (32px italic heading, max-width 800px paragraph, 50px divider line), a Portfolio Section or equivalent (32px italic heading, responsive grid of 400x400px images with hover scale-up and box-shadow effect, number of images as required), a Clients Section or equivalent (32px italic heading, auto-scrolling testimonial slider every 5s if needed, 150x100px client logos (not images) in a grid with grayscale filter turning full color on hover if applicable), and a Contact Section or equivalent (32px italic heading, email form with 5px border-radius input field, ‘Subscribe Now’ or relevant button with hover effect, and necessary contact details). Additionally, include a dark-themed Features Section or equivalent with a three-column grid highlighting key offerings such as Free Shipping, 24/7 Availability, and Best Prices (modifiable per prompt), using icons, short descriptions, and star ratings. The Footer should contain centered copyright text and social media icons with a hover opacity effect if required. The website must be fully responsive, adapting to desktop (1920px full layout), tablet (768px 2x2 grid), and mobile (375px single-column with a hamburger menu). Typography should use Montserrat/Poppins, with headings in 32px and body text in 16px, complemented by clean background colors and interactive buttons. Implement smooth interactions, including fade-in on page load, smooth scrolling, and hover effects on buttons, images, and social icons. Ensure a well-structured React project with modular components (e.g., Categories.js, Footer.js, Feature.js), generating them before importing into App.js if they do not exist. Follow clean, scalable coding practices using flexbox/grid for layouts, CSS animations for interactions, and maintain accessibility standards. Deliverables should include a Tailwind CSS configuration file, an index.css file with Tailwind base, components, and utilities, a public folder with an index.html file, and all necessary React app files, ensuring all images have appropriate alt tags for accessibility."
    },
    {
        "name": "7",
        "description": "Develop a fully responsive, modern website with a bold and energetic aesthetic, structured layout, and engaging interactions using React and Tailwind CSS for scalability. The website should be divided into six main sections such as Header, Hero, Features, Best Sellers, Categories, and Footer, with section names adjustable based on the website’s purpose. The Header should be fixed at the top (80px height, white background, black text, Montserrat/Poppins font) and include a text-based logo, navigation links (e.g., Home, Shop, Sale, Contact, Search—modifiable according to the website’s theme), and a responsive hamburger menu for mobile. The Hero Section or equivalent should feature a full-width split-screen layout with dynamic images (1920x800px), an overlay effect, a bold uppercase heading (48px), a 20px subtitle, and a smooth fade-in animation. The Features Section or equivalent should be dark-themed with a three-column grid highlighting key offerings (e.g., Free Shipping, 24/7 Availability, Best Prices—modifiable per context) using icons, short descriptions, and star ratings. The Best Sellers Section or equivalent should showcase a carousel grid of top products with responsive 400x400px images, hover effects, pricing, and an 'Add to Cart' or similar button. The Categories Section or equivalent should use a grid layout (3-column on desktop, 2-column on tablets, 1-column on mobile) featuring clickable images representing major categories, each with hover effects. A Call-to-Action Section or equivalent should include a full-width banner with engaging imagery, bold uppercase text (32px), and a prominent button (e.g., 'Order Now') with hover animation. The Footer should contain a newsletter subscription form (email input, subscribe button with hover effects), social media icons with hover opacity effects, contact details, and navigation links. The site must be fully responsive for desktop (1920px), tablet (768px 2x2 grid), and mobile (375px single-column with a hamburger menu), using Montserrat/Poppins typography (headings 32px, body text 16px) with interactive buttons. Smooth animations should include fade-in on page load, smooth scrolling, and hover effects on buttons, images, and social icons while ensuring accessibility. The design should leverage flexbox/grid for layouts, CSS animations for interactions, and maintain a clean, structured codebase. Deliverables should include the Tailwind CSS configuration file, an index.css file incorporating Tailwind base, components, and utilities, a public folder with an index.html file, and all necessary React app files, ensuring all images have appropriate alt tags for accessibility."
    },
    {
        "name": "8",
        "description": "Create a fully responsive, modern, and minimalist website with a fullscreen video background on the homepage using tailwind for styling. The video should autoplay, be muted, and include an alt attribute describing the video content that remains static while content scrolls over it, utilising ‘z’-index. The top navigation bar (80px height, transparent initially, turning black on scroll, Montserrat/Poppins font) should include links (e.g. Home, Stream/Buy, Coming Soon, Catalog, About Us, Contact—adjust names as per the prompt) and should disappear when scrolling down but reappear when scrolling up, with a responsive hamburger menu on mobile. The homepage hero section should prominently display a movie/show title (48px uppercase), a brief description (20px), and a call-to-action button ('Stream/Buy' in bold, orange with a hover effect). Below the hero, a grid of different movie/show posters (400x600px each) should be displayed, where hovering over an image reveals a small description via a fade-in effect. Each image should have a unique alt tag for accessibility. The About section should include a centered heading (32px italic), a concise paragraph (max-width 800px), and a '+ More Info' expandable option. The 'Releases Coming Soon' section should feature a background image with a dark overlay, a centered heading (32px italic), and a play button to preview upcoming releases. The newsletter section should include a prominent heading ('See it First'), an email input field (border-radius 5px), a checkbox for newsletter subscription, and a 'Subscribe' button with a hover effect. The footer should contain centered copyright text, social media icons with a hover opacity effect, and quick links to privacy policies. The website must be fully responsive, adapting to desktop (1920px full layout), tablet (768px 2x2 grid), and mobile (375px single-column with a hamburger menu). Typography should use Montserrat/Poppins, with headings in 32px, body text in 16px, and clean background colors with interactive buttons. Smooth interactions should include fade-in page load, smooth scrolling, and hover effects on buttons, images, and social icons. The React project should be modular, ensuring separate React component files (e.g. VideoHero.js, ImageGrid.js, About.js, Releases.js, Newsletter.js, Footer.js, it should be changed according to website title), which should be created if they do not exist before being imported into App.js.. Provide all necessary files for the React app to function, a public folder with an index.html file, and a Tailwind CSS configuration file with index.css containing tailwind base, utilities and components. Ensure that every image and video includes an appropriate alt tag for accessibility."
    },
    {
        "name": "9",
        "description": "Develop a modern React website using Tailwind CSS with a fixed background image that remains static while content scrolls over it, utilizing `z-index`. The color scheme should feature dark blue (#1E2732) as the primary background, light gray (#A0AAB3) for text, and neon green (#32E67A) for highlights, with 'Poppins' for headings and 'Open Sans' for body text. The navigation bar should be fixed at the top (70px height), initially transparent but darkening slightly on scroll, containing a left-aligned logo inside a neon green circle and right-aligned uppercase navigation links (e.g., ‘Home’, ‘Portfolio’, ‘Contact’—adjust names based on the website type) in 16px font with a hover underline effect. The hero section should feature a large centered heading (64px, bold) with select letters in neon green, a subtitle (18px, light gray), and a semi-transparent grayscale profile image on the right. The about section should include a darkened text box (600px width, 18px font) and a neon green button with a hover glow effect. The skills section (rename according to the website's purpose) should showcase skills with green progress bars on a dark blue background. The portfolio section (rename as needed) should display three image cards (350x250px) with a dark overlay that reveals ‘See More’ text on hover. The experience section (rename accordingly) should incorporate a vertical timeline with green dots connected by a neon green line, displaying an 18px bold neon green title, a 20px uppercase white name, a 16px gray title, and a 14px light gray description. The contact section should consist of a left-side contact details area (400px width, 18px, light gray) and a right-side form with two input fields (First Name, Last Name), two full-width fields (Phone, Message), and a neon green ‘Send’ button. The footer should include white social media icons (LinkedIn, Twitter, GitHub, Facebook) with a hover opacity effect, centered copyright text, and a small left-side logo identical to the navbar logo. The website must be fully responsive, adjusting heading sizes and using full-width skill bars on tablets (768px), while shifting to a single-column layout with a hamburger menu and reduced title sizes (28px) on mobile (375px). Implement the site using modular React components (e.g., `Navbar.js`, `HeroSection.js`, `About.js`, `Skills.js`, `Portfolio.js`, `Experience.js`, `Contact.js`, `Footer.js`—ensuring names align with the website's theme), utilizing flexbox/grid layouts, CSS animations for hover effects, and accessibility standards. Apply `z-index` to maintain the fixed background while content scrolls. Provide all essential files for the React app, including `index.css` with Tailwind base, utilities, and components, a public folder with `index.html`, and a Tailwind CSS configuration file, ensuring all images and videos include appropriate `alt` tags for accessibility."
    },
    {
        "name": "10",
        "description": "Design a professional yet engaging website using Tailwind CSS for styling, featuring a muted background video on the homepage with a structured layout that remains static while content scrolls over it, utilizing ‘z’- index, distinct sections, and a fully functional navigation bar. The primary color palette should include deep blue (#1E3A8A) for headers and buttons, warm beige (#F4C87A) for content boxes, and white (#FFFFFF) for text and background areas. Use 'Montserrat' for headings and 'Lato' for body text. The fixed top navigation bar (80px height) should have a deep blue background, a left-aligned logo inside a rectangular button with a white icon (not an image) and text, and right-aligned uppercase navigation links (e.g. ‘About,’ ‘Admission,’ ‘Learning,’ ‘News & Events,’ ‘Contact’: note that these should be strictly according to website title), each 16px, evenly spaced, turning bold on hover, with a ‘Log In’ button featuring a subtle border at the far right. The navigation should smoothly scroll to corresponding sections of the page, and on mobile, it should collapse into a hamburger menu with an animated dropdown. The hero section should have a full-width muted video background with a dark gradient overlay for contrast, a 64px bold white heading centered on the left, and a 20px italicized tagline below. The two-column ‘Welcome’ section should include a left-aligned 32px bold deep blue heading with an 18px dark gray paragraph inside a warm beige card (500px width, 20px padding), and a right-aligned 400px height full-width image with a subtle drop shadow. Vertical navigation icons (e.g. ‘Academic Programs,’ ‘Student Services,’ ‘Apply Now’, change them according to website title) should be positioned on the left in deep blue with hover effects. The ‘Upcoming Events’ section should have a white background with a 32px bold deep blue heading and display six event cards (350x250px) in a flexbox grid, each containing an image, title (20px, deep blue), date, location, and a ‘Register Now’ button with a blue border. The ‘Latest News’ section should follow a similar layout with three warm beige cards (350x250px), each featuring a bold title (20px, deep blue), a date (14px, gray), a short description (16px, dark gray), and a ‘Read More’ button in deep blue with white text. The footer should have a dark blue background with a three-column layout: the left column containing the logo (not an image) and institution name, the center featuring quick links (14px, white, uppercase) in two rows, and the right displaying contact details (14px, white) alongside white social media icons (20px) with hover opacity effects. A thin top border should separate the footer from the main content. Ensure full responsiveness by adjusting text sizes (H1: 48px, H2: 28px, P: 16px) on tablets (768px) and using a single-column layout with a collapsible hamburger menu on mobile (375px). The website should be implemented in React using modular components (e.g. `Navbar.js`, `HeroSection.js`, `Welcome.js`, `Events.js`, `News.js`, `Footer.js`, change these on the basis of website title), leveraging flexbox and grid layouts, smooth hover animations, and ensuring accessibility compliance. Provide all necessary files for the React app, including Tailwind CSS configuration file and `index.css` with tailwind base, utilities and components, a public folder with `index.html`. Ensure every image and video includes an appropriate alt tag for accessibility."
    }
]

def generate_code_from_azure_ai(prompt: str) -> dict:
    """Generate code using Azure AI Inference SDK."""
    try:
        selected_template = random.choice(design_templates)
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
        i = random.randint(0, 9)
        messages = [
            SystemMessage("You are an expert React developer. Generate a complete React project structure with separate files for components, styles, and entry points. For any images or videos in your components, follow these guidelines:\n\n1. Use responsive techniques:\n   - Set images/videos to have width='100%' (or appropriate percentage) and height='auto'\n   - Use CSS classes for proper sizing and responsive behavior\n   - Include max-width properties to prevent oversizing\n\n2. For each <img> or <video> tag:\n   - Include descriptive alt attributes (use a single word that best describes the image/video)\n   - Include className attributes for styling\n   - Use 'https://via.placeholder.com/800x600' as placeholder URLs\n\n3. Include responsive design principles in your CSS\n\nUse the following format for each file:\n\n```src/components/Header.js\n// Header.js code here\n```\n\n```src/components/Hero.js\n// Hero.js code here\n```\n\n```src/App.js\n// App.js code here\n```\n\n```src/index.js\n// index.js code here\n```\n\n```src/App.css\n// App.css code here\n```\n\n```public/index.html\n// index.html code here\n```\n\n```package.json\n// package.json code here\n```"),
             UserMessage(f"Create a React project for: {prompt}. Use the following design template:\n\n{design_templates[i]['description']}\n\nEnsure all components are placed in the 'src/components' folder which are imported into App.js and also include index.js inside src. Make sure to include relevant images and videos with descriptive alt tags (single word) and placeholder URLs. Provide the folder structure and file paths in the response."),
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


def extract_image_prompts(project_files: dict) -> list:
    """Extract image-related prompts from the generated code using the `alt` attribute."""
    image_prompts = []

    # Regex to find <img> tags and extract the `alt` attribute
    img_tag_regex = r'<img[^>]*alt="([^"]*)"[^>]*>'

    # Look for <img> tags in the project files
    for file_path, content in project_files.items():
        matches = re.findall(img_tag_regex, content)
        for alt_text in matches:
            if alt_text:  # Only add non-empty alt text
                image_prompts.append(alt_text)

    return image_prompts


def extract_video_prompts(project_files: dict) -> list:
    """Extract video-related prompts from the generated code using the `alt` attribute."""
    video_prompts = []

    # Regex to find <video> tags and extract the `alt` attribute
    video_tag_regex = r'<video[^>]*alt="([^"]*)"[^>]*>'

    # Look for <video> tags in the project files
    for file_path, content in project_files.items():
        matches = re.findall(video_tag_regex, content)
        for alt_text in matches:
            if alt_text:  # Only add non-empty alt text
                video_prompts.append(alt_text)

    return video_prompts


def fetch_image_from_pexels(prompt: str, api_key: str) -> str:
    """Fetch an image from Pexels based on a prompt."""
    try:
        # Pexels API endpoint
        url = "https://api.pexels.com/v1/search"
        headers = {"Authorization": api_key}
        params = {"query": prompt, "per_page": 5}  # Fetch up to 5 images

        # Send request to Pexels API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        # Parse the response
        data = response.json()
        if not data.get("photos"):
            raise Exception(f"No images found for prompt: {prompt}")

        # Iterate through the photos and try each URL until one works
        for photo in data["photos"]:
            image_url = photo["src"]["original"]
            try:
                # Check if the image URL is valid by making a HEAD request
                head_response = requests.head(image_url)
                if head_response.status_code == 200:
                    return image_url
                else:
                    logging.warning(f"Image URL returned {head_response.status_code}: {image_url}")
            except Exception as e:
                logging.warning(f"Error checking image URL {image_url}: {str(e)}")

        # If no valid image URL is found, raise an exception
        raise Exception(f"No valid image URLs found for prompt: {prompt}")

    except Exception as e:
        raise Exception(f"Error fetching image for prompt '{prompt}': {str(e)}")


def fetch_video_from_pexels(prompt: str, api_key: str) -> str:
    """Fetch a video from Pexels based on a prompt."""
    try:
        # Pexels API endpoint for videos
        url = "https://api.pexels.com/videos/search"
        headers = {"Authorization": api_key}
        params = {"query": prompt, "per_page": 5}  # Fetch up to 5 videos

        # Send request to Pexels API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        # Parse the response
        data = response.json()
        if not data.get("videos"):
            raise Exception(f"No videos found for prompt: {prompt}")

        # Iterate through the videos and try each URL until one works
        for video in data["videos"]:
            video_files = video.get("video_files", [])
            for video_file in video_files:
                video_url = video_file.get("link")
                try:
                    # Check if the video URL is valid by making a HEAD request
                    head_response = requests.head(video_url)
                    if head_response.status_code == 200:
                        return video_url
                    else:
                        logging.warning(f"Video URL returned {head_response.status_code}: {video_url}")
                except Exception as e:
                    logging.warning(f"Error checking video URL {video_url}: {str(e)}")

        # If no valid video URL is found, raise an exception
        raise Exception(f"No valid video URLs found for prompt: {prompt}")

    except Exception as e:
        raise Exception(f"Error fetching video for prompt '{prompt}': {str(e)}")

def replace_placeholders(project_files: dict, api_key: str) -> dict:
    """Replace placeholder image and video URLs with real URLs from Pexels."""
    # Extract image-related prompts from <img> tags
    image_prompts = extract_image_prompts(project_files)
    logging.info(f"Extracted image prompts: {image_prompts}")

    # Extract video-related prompts from <video> tags
    video_prompts = extract_video_prompts(project_files)
    logging.info(f"Extracted video prompts: {video_prompts}")

    # Replace placeholder image URLs with real image URLs
    for prompt in image_prompts:
        try:
            # Fetch image from Pexels
            image_url = fetch_image_from_pexels(prompt, api_key)
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
            video_url = fetch_video_from_pexels(prompt, api_key)
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


def create_zip_from_code(project_files: dict, zip_filename="react_project.zip") -> str:
    """Create a ZIP file with the generated React project, following the folder structure provided by the API."""
    project_dir = "./react_project"
    zip_path = os.path.join("./", zip_filename)

    # Delete existing project directory and ZIP file if they exist
    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)  # Delete the entire directory
        logging.info(f"Deleted existing project directory: {project_dir}")
    if os.path.exists(zip_path):
        os.remove(zip_path)  # Delete the existing ZIP file
        logging.info(f"Deleted existing ZIP file: {zip_path}")

    # Create the project directory
    os.makedirs(project_dir, exist_ok=True)

    # Write all files to the project directory
    for file_path, content in project_files.items():
        # Skip empty file paths
        if not file_path:
            continue
            
        full_path = os.path.join(project_dir, file_path)

        # Skip if the path is a directory (ends with "/" or is exactly a directory name)
        if file_path.endswith("/") or os.path.isdir(full_path):
            os.makedirs(full_path, exist_ok=True)
            continue

        # Create parent directories if they don't exist
        parent_dir = os.path.dirname(full_path)
        if parent_dir:  # Only create if there is a parent directory
            os.makedirs(parent_dir, exist_ok=True)

        # Write the file content
        with open(full_path, "w") as f:
            f.write(content)

    # Create a ZIP file from the project directory
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(project_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, project_dir))

    return zip_filename
