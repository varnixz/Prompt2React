import re

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