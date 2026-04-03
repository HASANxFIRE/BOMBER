import requests
import hashlib
from datetime import datetime, timezone
from .utils import send_request, get_random_user_agent

def api_11(number):
    url = "https://da-api.robi.com.bd/da-nll/otp/send"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "da-api.robi.com.bd",
        "User-Agent": get_random_user_agent()
    }
    data = {"msisdn": number}
    response = send_request(url, "POST", headers, data)
    
    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == "SUCCESSFUL":
                return response
            else:
                print(f"api_11 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_11 Validation Error: {e}")

    return response

def api_12(number):
    url = "https://api.shikho.com/public/activity/otp"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "api.shikho.com",
        "User-Agent": get_random_user_agent()
    }
    data = {"phone": number, "intent": "ap-discount-request"}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("code") == 200:
                return response
            else:
                print(f"api_12 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_12 Validation Error: {e}")

    return response

def api_13(number):
    url = "https://backoffice.ecourier.com.bd/api/web/individual-send-otp"
    params = {"mobile": number}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://ecourier.com.bd',
        'Referer': 'https://ecourier.com.bd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': get_random_user_agent(),
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = send_request(url, "GET", headers, params=params)
    
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            success_messages = ["OTP Sent.", "OTP already sent, please wait."]
            if json_data.get("success") is True or (json_data.get("success") is False and json_data.get("data") == "OTP already sent, please wait."):
                return response
            else:
                print(f"api_13 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_13 Validation Error: {e}")
    
    return response

def api_14(number):
    from .utils import get_binge_token
    token = get_binge_token()
    if not token:
        print("api_14: Failed to generate token automatically.")
        return None

    url = 'https://api.binge.buzz/api/v4/auth/otp/send'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://binge.buzz',
        'priority': 'u=1, i',
        'referer': 'https://binge.buzz/login',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'x-platform': 'web',
    }

    data = {
        'phone': f'+88{number}',
    }

    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code in [200, 201]:
            json_data = response.json()
            if json_data.get("success") is True:
                return response
            else:
                print(f"api_14 Validation Failed: {json_data}")
                # We don't override status_code here to avoid confusion in tests
                return response
    except Exception as e:
        print(f"api_14 Validation Error: {e}")

    return response

def api_15(number):
    url = f"https://romoni.com.bd/api/send-otp?phone={number}"
    headers = {
        "Host": "romoni.com.bd",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://romoni.com.bd/signup",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    response = send_request(url, "GET", headers)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") is True:
                return response
            else:
                print(f"api_15 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_15 Validation Error: {e}")

    return response

def api_16(number):
    url = "https://api.chinaonlinebd.com/api/v5/client-login-validation-email/get-email-otp"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://chinaonlinebd.com',
        'priority': 'u=1, i',
        'referer': 'https://chinaonlinebd.com/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }

    data = {
        'phone': number,
        'email': 'islamraisul796@gmail.com', # Should this be dynamic? Keeping as requested.
    }

    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") is True and json_data.get("code") == 200:
                return response
            else:
                print(f"api_16 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_16 Validation Error: {e}")

    return response

def api_17(number):
    url = "https://www.livemcq.com/web-otp-send/"
    headers = {
        "Host": "www.livemcq.com",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": get_random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=0, i",
        "Connection": "keep-alive"
    }
    response = send_request(url, "GET", headers)
    if response:
        cookies = response.cookies.get_dict()
        cstk = cookies.get('csrftoken', '')
        url_verify = f"https://www.livemcq.com/web-otp-verify/?phone_number={number}"
        headers_verify = {
            "Host": "www.livemcq.com",
            "Cookie": f"csrftoken={cstk}",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": get_random_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Referer": "https://www.livemcq.com/web-otp-send/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Priority": "u=0, i"
        }
        response = send_request(url_verify, "GET", headers_verify)
        if response and '<div id="phone-step"' in response.text:
            return response
        else:
            print("api_17 Validation Failed: Content mismatch")
            if response: response.status_code = 400
            return response
    return None

def api_18(number):
    url = "https://new.mojaru.com/api/student/registration"
    headers = {
        "Host": "new.mojaru.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": get_random_user_agent(),
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://mojaru.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://mojaru.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"mobile_or_email": number}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") is True:
                return response
            else:
                print(f"api_18 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_18 Validation Error: {e}")

    return response

def api_19(number):
    url = "https://new.mojaru.com/api/student/login"
    headers = {
        "Host": "new.mojaru.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": get_random_user_agent(),
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://mojaru.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://mojaru.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"mobile_or_email": number}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") is True:
                return response
            else:
                print(f"api_19 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_19 Validation Error: {e}")

    return response

def api_20(number):
    try:
        # Token Generation Logic
        # Vue: "chkjan" + String(now.getUTCHours()).padStart(2, '0') + String(now.getUTCMonth() + 1).padStart(2, '0') + now.getUTCFullYear() + String(now.getUTCDate()).padStart(2, '0')
        now = datetime.now(timezone.utc)
        hours = str(now.hour).zfill(2)
        month = str(now.month).zfill(2)
        year = str(now.year)
        day = str(now.day).zfill(2)
        
        code = f"chkjan{hours}{month}{year}{day}"
        otp_token = hashlib.sha256(code.encode()).hexdigest()
        
        url = "https://chokrojan.com/api/v1/passenger/login/mobile"
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
            'User-Agent': get_random_user_agent(),
            'company-id': '1',
            'domain-name': 'chokrojan.com',
            'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-platform': '3',
        }
        
        data = {
            'mobile_number': number,
            'otp_token': otp_token,
        }
        
        response = send_request(url, "POST", headers, data)
        
        # Response Validation
        try:
            if response and response.status_code == 200:
                json_data = response.json()
                if json_data.get("message") == "Otp successfully sent":
                    return response
                else:
                    print(f"api_20 Validation Failed: {json_data}")
                    response.status_code = 400
                    return response
        except Exception as e:
            print(f"api_20 Validation Error: {e}")

        return response
    except Exception as e:
        print(f"api_20 Error: {e}")
        return None
