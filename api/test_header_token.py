import requests
import base64
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_random_user_agent

def check_headers():
    session = requests.Session()
    session.headers.update({
        'User-Agent': get_random_user_agent(),
        'Accept': '*/*',
        'Origin': 'https://cartup.com',
        'Referer': 'https://cartup.com/'
    })
    
    endpoints = [
        "https://api.cartup.com/product/api/v1/homepage-layouts/get-desktop-homepage-layouts-config",
        "https://api.cartup.com/customer/api/v1/customer/auth/new-onboard/signup" # Valid endpoint, might 401 but return header
    ]
    
    token = None
    
    for url in endpoints:
        print(f"Checking headers from {url}...")
        try:
            resp = session.get(url) if "get" in url else session.post(url)
            print(f"Status: {resp.status_code}")
            print(f"Headers: {resp.headers}")
            
            # Case insensitive search
            for k, v in resp.headers.items():
                if k.lower() == "cf-ray-status-id-tn":
                    print(f"FOUND TOKEN: {v}")
                    token = v
                    break
            
            if token:
                break
        except Exception as e:
            print(f"Error: {e}")

    if token:
        # Construct sxsrf
        t1 = base64.b64encode(token.encode('utf-8')).decode('utf-8')
        sxsrf = base64.b64encode(t1.encode('utf-8')).decode('utf-8')
        print(f"Constructed sxsrf: {sxsrf}")
        
        # Test final API call
        target_url = "https://api.cartup.com/customer/api/v1/customer/auth/new-onboard/signup"
        json_data = {'email_or_phone': "01752126415"}
        
        headers = {
            'accept': '*/*',
            'content-type': 'application/json; charset=utf-8',
            'origin': 'https://cartup.com',
            'referer': 'https://cartup.com/',
            'sxsrf': sxsrf,
            'user-agent': session.headers['User-Agent']
        }
        
        print(f"Testing target API with constructed sxsrf...")
        resp = session.post(target_url, headers=headers, json=json_data)
        print(f"Final Status: {resp.status_code}")
        print(f"Final Body: {resp.text}")

if __name__ == "__main__":
    check_headers()
