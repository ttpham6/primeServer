from flask import Flask, request, jsonify
import PrimeCalculator
from PrimeCalculator import miller_rabin, sieveOfAtkin
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# CORS(app, supports_credentials=True, origins=["http://127.0.0.1:42755"]) # Allow credentials and specify the origin
CORS(app, supports_credentials=True, origins=["http://127.0.0.1:*"]) # Allow credentials and specify the origin

# minikube service api-service --url

@app.route('/')
def root():
    """Root endpoint with API information"""
    return jsonify({
        "name": "Prime Number API",
        "version": "1.0",
        "endpoints": [
            "/test-prime - Test primality of a number (POST)",
            "/generate-primes - Generate prime numbers up to a limit (POST)"
        ]
    })

@app.route('/test-prime', methods=['POST'])
def test_prime():
    """Test if a number is prime using Miller-Rabin primality test"""
    data = request.get_json()
    
    if not data or 'number' not in data:
        return jsonify({"error": "Missing number parameter"}), 400
    
    number = data['number']
    rounds = data.get('rounds', 5)  # default to 5 rounds if not specified
    
    try:
        number = int(number)
        rounds = int(rounds)
        if number <= 0:
            return jsonify({"error": "Number must be positive"}), 400
        if rounds <= 0 or rounds > 50:
            return jsonify({"error": "Rounds must be between 1 and 50"}), 400
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400
    
    result = miller_rabin(number, rounds)
    return jsonify({
        "number": number,
        "is_prime": result,
        "rounds": rounds
    })

@app.route('/generate-primes', methods=['POST'])
def generate_primes():
    """Generate prime numbers up to a limit using Sieve of Atkin"""
    data = request.get_json()
    
    if not data or 'limit' not in data:
        return jsonify({"error": "Missing limit parameter"}), 400
    
    try:
        limit = int(data['limit'])
        if limit <= 0:
            return jsonify({"error": "Limit must be positive"}), 400
    except ValueError:
        return jsonify({"error": "Invalid limit format"}), 400
    
    primes = PrimeCalculator.sieveOfAtkin(limit)
    return jsonify({
        "limit": limit,
        "count": len(primes),
        "primes": primes
    })
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    
