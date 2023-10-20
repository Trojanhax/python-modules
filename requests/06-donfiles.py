from io import BytesIO
import requests

# Provide a direct link to the image you want to download
url = 'https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png'

# Make a GET request to the image URL
r = requests.get(url)

if r.status_code == 200:
    # Open the image from the response content
    i = BytesIO(r.content)

    # Save the image to a file with the appropriate image extension
    with open('img2.jpg', 'wb') as fp:
        fp.write(i.read())
else:
    print("Failed to download the image. HTTP status code:", r.status_code)
