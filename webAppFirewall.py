
from flask import Flask, request, jsonify
app = Flask(__name__)
def is_header_conflict(headers):

    ''' Check if the request has conflicting headers.'''
    
    content_length = headers.get("Content-Length")
    transfer_encoding = headers.get("Transfer-Encoding")

    # Check if both headers are present

    if content_length and transfer_encoding:
        return True
    
    return False

@app.route("/process", methods=["POST"])
def process_request():
    request_headers = request.headers

    # Check for header conflicts

    if is_header_conflict(request_headers):

        return jsonify({"error": "Invalid request with conflicting headers."}), 400
    
    return jsonify({"message": "Request processed successfully"}), 200

if __name__ == "__main__":
    app.run(debug = True)

    
