from flask import Flask, request
import random, string 

app = Flask(__name__) 


# random number generator route here


@app.route('/get_lotterynumbers', methods=['GET'])
def lotterynumbers():
    winningnumber = []
    for i in range(1,7):
        n = random.randint(0,19)
        winningnumber.append(n)

    winningnumber_string = "".join(map(str,winningnumber))

    return winningnumber_string



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)