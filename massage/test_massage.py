from flask import Flask, request, jsonify
import os
import msgpack

app = Flask(__name__)


@app.route('/get_result', methods=['POST'])
def get_result():
    msgpack_file = request.files['file']
    if not msgpack_file:
        return jsonify({'error': 'No file provided'})

    file_name = msgpack_file.filename
    file_ext = os.path.splitext(file_name)[1]

    if file_ext != '.msgpack':
        return jsonify({'error': 'Invalid file format'})

    try:
        with open(msgpack_file, 'rb') as f:
            data = f.read()
            msgpack.unpackb(data)
    except Exception as e:
        return jsonify({'error': f'Invalid MessagePack format: {e}'})

    return jsonify({'message': 'MessagePack file is valid'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
