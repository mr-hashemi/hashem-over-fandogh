import os 
import time
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tmp_fname = f"./tmp/code-{time.time()}.hashem"
        code = request.form['code']
        with open(tmp_fname, 'w') as f:
            f.write(code)
        
        with os.popen(f'./hashem {tmp_fname}') as res:
            value = res.read()
        return render_template('index.html', code=code, value=value)
    return render_template('index.html')
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
