from flask import Flask, request, jsonify
from calculator import add

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    numbers = data.get('numbers', '')
    try:
        result = add(numbers)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
