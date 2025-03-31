from flask import Flask, jsonify
import requests
from flask_cors import CORS  # Allow CORS to enable cross-origin API access

app = Flask(__name__)
CORS(app)  # Enables CORS globally for all routes

@app.route('/api/space-debris', methods=['GET'])
def get_space_debris():
    """
    Fetches space debris data from ESA's DISCOS API.
    
    Returns:
        JSON response containing space debris data or an error message.
    """
    token = "IjUxNDg2NGJhLTE4YzYtNGMyNi1hYjhiLWY2NWQ2ZWI2ZmZjNSI.oPVneREPBKjxLTPiXxoNoSL1Q0U"
    url = 'https://discosweb.esoc.esa.int/api/objects'
    
    headers = {
        'Authorization': f'Bearer {token}',  # API authentication using Bearer token
        'DiscosWeb-Api-Version': '2',        # Specify API version
    }
    
    params = {
        'filter': "eq(objectClass,Payload)&gt(reentry.epoch,epoch:'2020-01-01')",  # Filter: Only payloads with reentry after 2020
        'sort': '-reentry.epoch',  # Sort results by most recent reentry first
    }

    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        return jsonify(response.json())  # Return API response if successful
    else:
        return jsonify({"error": "Failed to fetch data"}), 500  # Return error if request fails

if __name__ == '__main__':
    app.run(debug=True)  # Start Flask app in debug mode
