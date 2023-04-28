from flask import Flask, request
from lxml import etree

app = Flask(__name__)


@app.route('/get_result', methods=['POST'])
def get_result():
    xml_file = request.files.get('file')

    # Проверяем, что был отправлен файл
    if not xml_file:
        return 'Файл не был отправлен', 400

    # Проверяем, что файл является XML-документом
    try:
        root = etree.fromstring(xml_file.read())
    except etree.XMLSyntaxError:
        return 'Некорректный XML-документ', 400

    return 'XML-документ корректный'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
