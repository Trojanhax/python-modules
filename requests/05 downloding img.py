from PIL import Image
from io import BytesIO
import requests

# Provide a direct link to the image you want to download
image_url = 'https://upload.wikidia.org/'

# Make a GET request to the image URL
r = requests.get(image_url)

if r.status_code == 200:
    # Open the image from the response content
    i = Image.open(BytesIO(r.content))
    print(i)

    # Save the image to a file
    with open('img.jpg', 'wb') as fp:
        i.save(fp)
else:
    print("Failed to download the image. HTTP status code:", r.status_code)
