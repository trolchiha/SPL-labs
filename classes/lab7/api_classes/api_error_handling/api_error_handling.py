"""
APIRequest Module

This module provides a class for handling API requests and errors. The `APIRequest` class
is designed to simplify making HTTP requests to an API, handling common errors, and providing
a consistent interface for making requests
"""
import json
from requests import get, exceptions

class APIError(Exception):
    """Exception raised for errors in the API.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class APIRequest:
    """
    Class for handling API requests and errors.

    Attributes:
        base_url (str): The base URL of the API.
    """

    def __init__(self, base_url):
        """
        Initializes an instance of the APIRequest class.

        Args:
            base_url (str): The base URL of the API.
        """
        self.base_url = base_url

    def make_request(self, endpoint, params=None, headers=None):
        """
        Makes an API request and handles errors.

        Args:
            endpoint (str): The API endpoint.
            params (dict): The parameters to include in the request.
            headers (dict): The headers to include in the request.

        Returns:
            dict or None: The JSON response if the request is successful, None otherwise.
        """
        try:
            url = f"{self.base_url}{endpoint}"
            result = get(url, params=params, headers=headers)

            result.raise_for_status()  # Raises an HTTPError for bad responses

            json_result = json.loads(result.content)
            return json_result

        except exceptions.RequestException as request_exception:
            error_message = f"Error making API request: {request_exception}"
            raise APIError(error_message)

        except json.JSONDecodeError as decode_exception:
            error_message = f"Error decoding JSON response: {decode_exception}"
            raise APIError(error_message)
        
        except exceptions.HTTPError as http_error:
            error_message = f"HTTP error: {http_error}"
            raise APIError(error_message)
        
        except KeyError as key_error:
            error_message = f"Unexpected response format: {key_error}"
            raise APIError(error_message)

        except Exception as unexpected_error:
            error_message = f"An unexpected error occurred: {unexpected_error}"
            raise APIError(error_message)

# Example usage:
# api_request = APIRequest(BASE_URL)
# try:
#     album_data = api_request.make_request("search", params={"q": album_name, "type": "album", "limit": 1})
# except APIError as api_error:
#     print(f"API Error: {api_error.message}")
