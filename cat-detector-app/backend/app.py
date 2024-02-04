from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock TensorFlow model for cat detection
@app.route('/detect_cat', methods=['POST'])
def detect_cat():
    # Mock detection result
    result = {'result': 'Cat detected'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
