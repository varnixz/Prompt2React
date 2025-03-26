import requests

def fetch_image_from_pexels(prompt: str, api_key: str, output_file: str = "pexels_image.jpg") -> str:
    """
    Fetch an image from Pexels based on a prompt and save it to a file.

    Args:
        prompt (str): The search prompt (e.g., "futuristic cityscape").
        api_key (str): Your Pexels API key.
        output_file (str): The filename to save the fetched image.

    Returns:
        str: The path to the saved image file.
    """
    try:
        # Pexels API endpoint
        url = "https://api.pexels.com/v1/search"
        headers = {"Authorization": api_key}  # Use the API key in the headers
        params = {"query": prompt, "per_page": 1}  # Fetch only 1 image

        # Send request to Pexels API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the response
        data = response.json()
        if not data.get("photos"):
            raise Exception("No images found for the given prompt.")

        # Get the image URL
        image_url = data["photos"][0]["src"]["original"]

        # Download the image
        image_data = requests.get(image_url).content
        with open(output_file, "wb") as f:
            f.write(image_data)

        print(f"✅ Image saved to: {output_file}")
        return output_file

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
        raise Exception(f"HTTP error: {str(http_err)}")
    except Exception as e:
        print(f"❌ Error fetching image from Pexels: {e}")
        raise Exception(f"Error fetching image from Pexels: {str(e)}")


# Example usage
if __name__ == "__main__":
    prompt = "futuristic cityscape"  # Replace with your desired prompt
    api_key = "d9WgxN9rFSJOXh5CTa906SFfyjgzdHCCR01rq9QGQ0lnvxnWwDI3x2gT"  # Your Pexels API key
    output_file = "pexels_image.jpg"  # Output file name
    fetch_image_from_pexels(prompt, api_key, output_file)