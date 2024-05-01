from flask import Flask, jsonify
from collections import deque

app = Flask(__name__)

# Constants
WINDOW_SIZE = 10
TEST_SERVER_BASE_URL = "http://20.244.56.144/test/"
TIMEOUT = 0.5  # 500 milliseconds

# Data storage
number_window = deque(maxlen=WINDOW_SIZE)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def calculate_average(numbers):
    if not numbers:
        return 0.0
    return round(sum(numbers) / len(numbers), 2)

@app.route('/e')
def even_numbers():
    numbers = [num for num in range(2, 2 + WINDOW_SIZE * 2, 2)]  # Generate even numbers
    return jsonify({"numbers": numbers})

@app.route('/p')
def prime_numbers():
    prime_nums = [num for num in range(2, 2 + WINDOW_SIZE * 10) if is_prime(num)]  # Generate prime numbers
    return jsonify({"numbers": prime_nums})

@app.route('/fibo/<int:n>')
def fibonacci_series(n):
    fib_sequence = fibonacci(n)
    return jsonify({"numbers": fib_sequence})

@app.route('/numbers')
def get_numbers():
    avg = calculate_average(number_window)
    return jsonify({
        "numbers": list(number_window),
        "avg": avg,
        "windowCurrState": list(number_window),
        "windowPrevState": []
    })

if __name__ == '__main__':
    app.run(debug=True)
