import requests

# Server URL
url = "http://your-server-ip/path-to-user-creation.php"

# Loop to send 500 POST requests
for i in range(500):
    username = "ruffoni" + str(i)
    data = {
        "username": username,
        "password": "HELLO",
        "SubmitCredentials": "SubmitCredentials"
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"User {username} created successfully.")
        else:
            print(f"Failed to create user {username} with status code: {response.status_code}")
            print(f"Response content: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to create user {username} with exception: {e}")
