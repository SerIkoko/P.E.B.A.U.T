# B.U.R.P.P.R
# Bulk User Registration via Python POST Requests

This Python script automates the creation of multiple user accounts by sending HTTP POST requests to a specified server endpoint. It is ideal for testing or populating a development environment with dummy user data.

## 🚀 Features

- Creates 500 unique users (`user0` to `user499`)
- Sends POST requests with form data to a given URL
- Handles server response and exceptions gracefully
- Useful for stress testing or batch user provisioning in test environments

## 📌 Important

⚠️ **Use this script only on servers you own or have explicit permission to test. Unauthorized usage may be illegal or violate terms of service.**

## 🧪 Example Usage

Edit the `url` variable to point to your server's user creation endpoint.

```python
url = "http://your-server-ip/path-to-user-creation.php"
