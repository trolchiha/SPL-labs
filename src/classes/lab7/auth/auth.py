"""
Authentication Module

This module manages the authentication process to obtain access tokens from the authentication server.
It provides functions to retrieve tokens and generate authorization headers required for API requests.
"""
import os
import base64
import json

from dotenv import load_dotenv
from requests import post
from shared.settings import get_lab_settings

settings = get_lab_settings("lab7")
URLS = settings["urls"]
TOKEN_URL = URLS["token_url"]

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_token():
    """
    Retrieves an access token from the authentication server.

    Returns:
        str: The access token.
    """
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type":"client_credentials"}

    result = post(TOKEN_URL, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token


def get_auth_header(token):
    """
    Generates the authorization header using the provided access token.

    Args:
        token (str): The access token.

    Returns:
        dict: The authorization header.
    """
    return { "Authorization": "Bearer " + token }
