from flask import Flask, request, jsonify
from factorial_imperative import factorial_imperative
from factorial_declarative import factorial_declarative

app = Flask(__name__)

@app.route('/factorial_imperative', methods=['GET'])
def calculate_imperative():
    number = int(request.args.get('number', 0))      # Get the 'number' parameter from the query string
    result = factorial_imperative(number)            # Calculate factorial using the imperative function
    return jsonify(result=result)                    # Return the result as a JSON response


@app.route('/factorial_declarative', methods=['GET'])
def calculate_declarative():
    number = int(request.args.get('number', 0))
    result = factorial_declarative(number)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)     # Run the Flask app on localhost at port 5000