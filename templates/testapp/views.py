from flask import render_template  # 追加
from testapp import app


@app.route('/')
def index():
    return render_template('testapp/index.html')
    @app.route('/sampleform')
def sample_form():
    return render_template('testapp/sampleform.html')
