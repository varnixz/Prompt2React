import requests
import logging
import time

def fetch_image_from_pexels(prompt: str, api_key: str) -> str:
    """
    Continuously fetch images from Pexels based on a prompt
    until a valid (status code 200) image URL is found.
    """
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": api_key}
    params = {"query": prompt, "per_page": 3}  # Limit to 3 for quicker retries

    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if not data.get("photos"):
                raise Exception(f"No images found for prompt: {prompt}")

            for photo in data["photos"]:
                image_url = photo["src"]["original"]
                try:
                    image_response = requests.get(image_url, stream=True, timeout=5)
                    if image_response.status_code == 200:
                        return image_url
                    else:
                        logging.warning(f"Received status {image_response.status_code} for URL: {image_url}")
                except Exception as e:
                    logging.warning(f"Error accessing image URL {image_url}: {e}")

            # Wait before retrying
            logging.info("No valid image URL found, retrying...")
            time.sleep(2)

        except Exception as e:
            logging.error(f"Error fetching image for prompt '{prompt}': {str(e)}")
            time.sleep(2)


def fetch_video_from_pexels(prompt: str, api_key: str) -> str:
    """
    Continuously fetch videos from Pexels based on a prompt
    until a valid (status code 200) video URL is found.
    """
    url = "https://api.pexels.com/videos/search"
    headers = {"Authorization": api_key}
    params = {"query": prompt, "per_page": 3}  # limit results to avoid hitting API limits

    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if not data.get("videos"):
                raise Exception(f"No videos found for prompt: {prompt}")

            # Iterate through videos and check their URLs
            for video in data["videos"]:
                for video_file in video.get("video_files", []):
                    video_url = video_file.get("link")
                    try:
                        video_response = requests.get(video_url, stream=True, timeout=5)
                        if video_response.status_code == 200:
                            return video_url
                        else:
                            logging.warning(f"Received status {video_response.status_code} for URL: {video_url}")
                    except Exception as e:
                        logging.warning(f"Error accessing video URL {video_url}: {e}")
            
            # Sleep before trying again to avoid hammering API
            logging.info("No valid video URL found, retrying...")
            time.sleep(2)

        except Exception as e:
            logging.error(f"Error fetching video for prompt '{prompt}': {str(e)}")
            time.sleep(2)  # wait before retrying
