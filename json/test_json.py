from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/get_result', methods=['POST'])
def get_result():
    json_file = request.files['file']
    try:
        data = json.load(json_file)
        # проверяем корректность JSON
        if data is not None:
            return 'JSON--документ корректный!'
        else:
            return 'JSON -документ некорректный!', 400
    except Exception as e:
        return f'JSON -документ некорректный!', 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
