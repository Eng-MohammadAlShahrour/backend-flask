import requests

# Your token (replace this with the token you provided)
token = "IjUxNDg2NGJhLTE4YzYtNGMyNi1hYjhiLWY2NWQ2ZWI2ZmZjNSI.oPVneREPBKjxLTPiXxoNoSL1Q0U"
url = 'https://discosweb.esoc.esa.int/api/objects'

# Set headers with the token
headers = {
    'Authorization': f'Bearer {token}',  # Bearer token authentication
    'DiscosWeb-Api-Version': '2',        # API version header
}

# Example parameters (you can modify or remove these based on the API documentation)
params = {
    'filter': "eq(objectClass,Payload)&gt(reentry.epoch,epoch:'2020-01-01')",  # Filter example
    'sort': '-reentry.epoch',  # Sort example
}

# Make the request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.ok:
    print(response.json())  # Print JSON response if successful
else:
    print(response.json())  # Print error if something goes wrong
