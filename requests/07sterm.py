import requests

# Provide a direct link to the executable file you want to download
url = 'https://download.sqlitebrowser.org/SQLiteDatabaseBrowserPortable_3.12.2_English.paf.exe'

# Make a GET request to the executable file URL
r = requests.get(url, stream=True)

if r.status_code == 200:
    # Save the executable file to a file with the appropriate extension
    with open('SQLiteDatabaseBrowserPortable_3.12.2_English.paf.exe', 'wb') as fp:
        for chunk in r.iter_content(chunk_size=128):
            fp.write(chunk)
else:
    print("Failed to download the executable file. HTTP status code:", r.status_code)
