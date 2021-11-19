import requests
import json

def get_url():
    return 'https://test.jasgme.com/sgme/api'


def get_valid_credentials():
    return {
        'login': 'victor.alves@dellead.com',
        'password': 'a20021709'
    }


def get_token():
    url = get_url()
    credentials_body = get_valid_credentials()
    response = requests.post(f'{url}/authenticate/login', json=credentials_body)
    assert response.status_code == 200

    json_data = json.loads(response.text)
    token = json_data['token']

    auth = f'Bearer {token}'
    return auth
