from flask import Flask, request, jsonify
import os
import fastavro

app = Flask(__name__)


@app.route('/get_result', methods=['POST'])
def get_result():
    avro_file = request.files['file']
    if not avro_file:
        return jsonify({'error': 'No file provided'})

    file_name = avro_file.filename
    file_ext = os.path.splitext(file_name)[1]

    if file_ext != '.avro':
        return jsonify({'error': 'Invalid file format'})

    try:
        with open(avro_file, 'rb') as f:
            data = f.read()
            fastavro.schemaless_reader(data)
    except Exception as e:
        return jsonify({'error': f'Invalid Avro format: {e}'})

    return jsonify({'message': 'Avro file is valid'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
