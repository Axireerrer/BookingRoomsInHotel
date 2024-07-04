import requests

"""
Check booking the chosen room by user who was authenticated by jwt token 
"""

url = "http://127.0.0.1:8000/api/v1/rooms/booking/32/"

"""
Generate token by url: "http://127.0.0.1:8000/token/jwt/create
"""

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwMDUyNjE2LCJpYXQiOjE3MjAwNTIzMTYsImp0aSI6IjdlMzA3YzliZDczNjQ4YWJhNGFlNzFjNTdiZTQxNGNmIiwidXNlcl9pZCI6MTN9.CZxY6-WjdVc1NxpKI2OXMF7RJo3Hc-BPQuL7b7VYukY"
}

data = {
    "user": 13
}

response = requests.patch(url, headers=headers, json=data)
print(response.json())
print(response.status_code)

if __name__ == "__main__":
    print(response.json())
    print(response.status_code)
