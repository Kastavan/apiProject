"""Requests code checking methods"""
import json

from requests import Response


class Checking:

    """Status code check method"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success!! Status code = " + str(response.status_code))
        else:
            print("Fail!! Status code = " + str(response.status_code))


    """Method to check required fields in request response"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields present")

    """Method to check value of required fields in request response"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " correct!")

    """Method to check a word in value of required fields in request response"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + " present!")
        else:
            print("Word " + search_word + " absent!")

