from utils.http_methods import Http_methods

"""Методы для тестирования Google Maps API"""

base_url = "https://rahulshettyacademy.com"  # base url
key = "?key=qaclick123"  # parameter for all requests


class GoogleMapsApi:

    """New location creation method"""

    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # POST method resource
        post_url = base_url+post_resource+key
        print(post_url)

        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Checking new location method"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"  # GET method resource
        get_url = base_url+get_resource+key+"&place_id="+place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Update new location method"""

    @staticmethod
    def update_new_place(place_id):

        put_resource = "/maps/api/place/update/json"  # PUT method resource
        put_url = base_url+put_resource+key
        print(put_url)

        json_for_update_location = {

                "place_id": place_id,
                "address": "100 Lenina street, RU",
                "key": "qaclick123"
                }
        result_put = Http_methods.put(put_url, json_for_update_location)
        print(result_put.text)
        return result_put

    """Delete new location method"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url+delete_resource+key
        print(delete_url)

        json_for_delete_new_location = {
            "place_id": place_id
        }

        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete
