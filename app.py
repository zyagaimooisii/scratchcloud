from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    # 入力欄1の値を取得
    input1 = request.form['input1']

    # 入力欄2の値を取得
    input2 = request.form['input2']

    # コマンドを実行
    command = ["python", "main.py", input1, input2]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, _ = process.communicate()

    # 結果を出力
    return render_template('index.html', result=output.decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
