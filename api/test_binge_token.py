import requests
import json

def get_binge_token():
    """
    Investigates and fetches the guest token for Binge.
    This mimics the behavior of the Binge website on load.
    """
    url = "https://api.binge.buzz/api/v4/auth/guest"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://binge.buzz',
        'referer': 'https://binge.buzz/login',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'x-platform': 'web',
    }
    
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            token = data.get("data", {}).get("token")
            print(f"Successfully fetched Binge token: {token}")
            return token
        else:
            print(f"Failed to fetch token. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error fetching Binge token: {e}")
    
    return None

if __name__ == "__main__":
    token = get_binge_token()
    if token:
        # Example test call with the fetched token
        print("\nTesting OTP send with fetched token...")
        test_number = "01775179605"
        otp_url = "https://api.binge.buzz/api/v4/auth/otp/send"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'authorization': f'Bearer {token}',
            'content-type': 'application/json',
            'origin': 'https://binge.buzz',
            'referer': 'https://binge.buzz/login',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
            'x-platform': 'web',
        }
        data = {'phone': f'+88{test_number}'}
        res = requests.post(otp_url, headers=headers, json=data)
        print(f"OTP Send Response: {res.status_code} - {res.text}")
