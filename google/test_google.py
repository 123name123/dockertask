from flask import Flask, request, jsonify
import os
import protobuf

app = Flask(__name__)


@app.route('/get_result', methods=['POST'])
def get_result():
    protobuf_file = request.files['file']
    if not protobuf_file:
        return jsonify({'error': 'No file provided'})

    file_name = protobuf_file.filename
    file_ext = os.path.splitext(file_name)[1]

    if file_ext != '.proto':
        return jsonify({'error': 'Invalid file format'})

    try:
        with open(protobuf_file, 'rb') as f:
            data = f.read()
            protobuf_message = protobuf.message.Message()
            protobuf_message.ParseFromString(data)
    except Exception as e:
        return jsonify({'error': f'Invalid protobuf format: {e}'})

    return jsonify({'message': 'Protobuf file is valid'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
