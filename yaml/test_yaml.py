from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)


@app.route('/get_result', methods=['POST'])
def get_result():
    yaml_file = request.files['file']
    try:
        yaml.safe_load(yaml_file.stream)
        return 'Yaml--документ корректный!'
    except Exception as e:
        return 'Yaml--документ некорректный!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
