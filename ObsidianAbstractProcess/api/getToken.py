import requests


def get_access_token(
    api_key: str,
    secret_key: str
) -> str:
    '''
    Get Access Token by API Key and Secret Key 
    '''
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers)
    return response.json().get("access_token")
