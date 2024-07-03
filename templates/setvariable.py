import scratchattach as scratch3
import flask

app = flask.Flask(__name__)

@app.route('/set-variable', methods=['GET'])
def set_variable():
    # GETリクエストの値を取得
    data1 = flask.request.args.get('data1')
    data2 = flask.request.args.get('data2')
    data3 = flask.request.args.get('data3')

    # Scratch 3.0にログイン
    session = scratch3.login("splatoon-clips", "756851")

    # クラウドに接続
    conn = session.connect_cloud(data1)

    # 変数を設定
    conn.set_var("data2", data3)

    # 結果を返す
    return flask.jsonify({
        'status': 'success',
        'message': 'Variable set successfully'
    })

if __name__ == '__main__':
    app.run(debug=True)
