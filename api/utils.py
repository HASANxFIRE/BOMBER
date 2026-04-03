import requests
import random
import string

def random_string(pattern):
    result = ''
    i = 0
    while i < len(pattern):
        if i + 1 < len(pattern) and pattern[i:i+2] == '?n':
            result += str(random.randint(0, 9))
            i += 2
        elif i + 1 < len(pattern) and pattern[i:i+2] == '?l':
            result += random.choice(string.ascii_lowercase)
            i += 2
        elif i + 1 < len(pattern) and pattern[i:i+2] == '?i':
            result += random.choice(string.ascii_letters + string.digits)
            i += 2
        else:
            result += pattern[i]
            i += 1
    return result

def get_random_user_agent():
    """Generates a dynamic random User-Agent string."""
    chrome_version = f"{random.randint(120, 145)}.0.{random.randint(0, 5000)}.{random.randint(0, 200)}"
    return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'

def send_request(url, method, headers, data=None, cookies=None, params=None):
    try:
        if method == "POST":
            if headers.get("Content-Type") == "application/x-www-form-urlencoded":
                response = requests.post(url, headers=headers, data=data, cookies=cookies, params=params, timeout=None)
            else:
                response = requests.post(url, headers=headers, json=data, cookies=cookies, params=params, timeout=None)
        else:
            response = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=None)
        return response
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

def get_binge_token():
    try:
        firebase_key = 'AIzaSyDKtOJpkYEDnQVKNnyCeyoN1DjajMW7o9g'
        signup_url = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={firebase_key}'
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': get_random_user_agent()
        }
        signup_res = requests.post(signup_url, headers=headers, json={'returnSecureToken': True})
        if signup_res.status_code != 200:
            return None
            
        signup_data = signup_res.json()
        uid = signup_data.get('localId')
        firebase_token = signup_data.get('idToken')
        
        if not uid or not firebase_token:
            return None
            
        verify_url = 'https://api.binge.buzz/api/v4/auth/anon/verify'
        verify_res = requests.post(verify_url, headers=headers, json={'uid': uid, 'firebaseAccessToken': firebase_token})
        if verify_res.status_code not in [200, 201]:
            return None
            
        verify_data = verify_res.json()
        return verify_data.get('data', {}).get('accessToken')
    except Exception as e:
        print(f"Error fetching Binge token: {e}")
        return None
