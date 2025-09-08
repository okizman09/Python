import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        #Allows program to handle multiple urls at once separated by spaces
        urls = url.split()
        
        for url in urls:
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            filename = "downloaded_image.jpg"
            
        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)

        #check content type to ensure it's an image
        content_type = response.headers.get('Content-Type')
        if content_type and 'image' not in content_type:
            print(f"✗ Not an image: {filename}")
            return
        
        #implementing cautions when downloading from unknown sources
        if response.status_code != 200:
            print(f"✗ Failed to fetch image: {filename}")
            return

        #prevents duplicate images from being saved
        if os.path.exists(filepath):
            print(f"✓ Image already exists: {filename}")
        else:
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("\nConnection strengthened. Community enriched.")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()