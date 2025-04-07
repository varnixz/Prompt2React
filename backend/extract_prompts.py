import re

def extract_image_prompts(project_files: dict) -> list:
    """Extract image-related prompts from the generated code using the `alt` attribute and Array.fill()."""
    image_prompts = []

    # Regex to find <img> tags and extract the `alt` attribute
    img_tag_regex = r'<img[^>]*alt="([^"]*)"[^>]*>'

    # Regex to find alt text from Array.fill() objects
    array_fill_img_regex = r'fill\(\{\s*(?:[^{}]*?)alt:\s*["\']([^"\']+)["\'][^{}]*?\}\)'

    for file_path, content in project_files.items():
        # <img> tags
        matches = re.findall(img_tag_regex, content)
        for alt_text in matches:
            if alt_text:
                image_prompts.append(alt_text)

        # Array.fill({ src: ..., alt: ... }) usage
        fill_matches = re.findall(array_fill_img_regex, content)
        for alt_text in fill_matches:
            if alt_text:
                image_prompts.append(alt_text)

    return image_prompts


def extract_video_prompts(project_files: dict) -> list:
    """Extract video-related prompts from the generated code using the `alt` attribute and Array.fill()."""
    video_prompts = []

    # Regex to find <video> tags and extract the `alt` attribute
    video_tag_regex = r'<video[^>]*alt="([^"]*)"[^>]*>'

    for file_path, content in project_files.items():
        # <video> tags
        matches = re.findall(video_tag_regex, content)
        for alt_text in matches:
            if alt_text:
                video_prompts.append(alt_text)

    return video_prompts
