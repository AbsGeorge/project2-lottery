from flask import Flask, render_template
import requests 

app = Flask(__name__)


@app.route('/')
def home():
    lotterynumber = requests.get('http://lottery_number_api:5000/get_lotterynumbers')
    lotteryalpha = requests.post('http://lottery_alpha_api:5000/get_lotteryalpha', data=lotterynumber.text)
    return render_template('index.html', lotterynumber=lotterynumber.text, lotteryalpha=lotteryalpha.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)