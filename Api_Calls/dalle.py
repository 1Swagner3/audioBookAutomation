import openai
import requests
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

def generate_and_save_image(prompt, output_folder, file_name):
    # Set OpenAI API key
    load_dotenv()
    openai.api_key = os.environ.get("OPENAI_KEY")

    # Generate an image using DALL-E
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # Number of images to generate
        size="1024x1024"  # Image size
    )

    # Get the image URL from the response
    image_url = response['data'][0]['url']

    # Download the image
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, file_name)

    # Save the image
    image.save(output_file_path)

    print(f"Image saved to {output_file_path}")

# Example usage
prompt = "A futuristic cityscape"
output_folder = "path/to/output/folder"
file_name = "futuristic_cityscape.png"
generate_and_save_image(prompt, output_folder, file_name)
