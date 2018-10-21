from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('conf.json', 'r') as fp:
        confDict = json.load(fp)
        return render_template('confpage.html', confDict=confDict)

@app.route('/submit', methods=['POST'])
def processData():
    openerIp = request.form.get('openerIp')
    botAuthCode = request.form.get('botAuthCode')
    confDict = {"openerIp": openerIp, "botAuthCode": botAuthCode}
    with open('conf.json', 'w') as fp:
        json.dump(confDict, fp)
    return render_template('ok.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
