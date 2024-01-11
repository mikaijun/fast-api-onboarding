import requests

from firebase_admin import auth

def create_user():
    auth.create_user(
      email='user@example.com',
      password='secretPassword',
  )

def firebase_login(api_key: str):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={api_key}"
    data = {"email": "user@example.com" , "password": "secretPassword", "returnSecureToken": True}
    result = requests.post(url=uri, data=data).json()
    return result["idToken"]
