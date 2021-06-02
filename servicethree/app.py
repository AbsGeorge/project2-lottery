from flask import Flask, request
import random, string 

app = Flask(__name__) 


@app.route('/get_lotteryalpha', methods=['GET'])
def get_noise():
    letters = string.ascii_lowercase
    alphabet = [random.choice(letters) for i in range(2)]
    alphabet_string = "".join(alphabet)

    return alphabet_string


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)