from flask import Flask, request
import xmltodict
from timeit import timeit, default_timer
import os
from avro import schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json
import msgpack
import yaml
import pickle

app = Flask(__name__)

convert_data = dict(root=dict(
    fstr="-" * 1000,
    sstr="-" * 100,
    tstr="-" * 10,
    fint=1000,
    sint=100,
    tint=10,
    flist=[1] * 1000,
    slist=["-"] * 1000,
    tlist=[0.1] * 1000
))


def xml_serialization():
    with open("test.xml", "w") as f:
        xmltodict.unparse(convert_data, f)


def xml_deserialization():
    with open("test.xml", "r") as f:
        xmltodict.parse(''.join(f.readlines()))


def avro_serialization():
    writer = DataFileWriter(open("test.avro", "wb"), DatumWriter(),
                            schema)
    writer.append(convert_data)
    writer.close()


def avro_deserialization():
    DataFileReader(open("test.avro", "rb"), DatumReader())


def json_serialization():
    with open("test.json", "w") as f:
        json.dump(convert_data, f)


def json_deserialization():
    with open("test.json", "r") as f:
        json.load(f)


def mpk_serialization():
    with open("test.mpk", "wb") as f:
        msgpack.dump(convert_data, f, use_bin_type=True)


def mpk_deserialization():
    with open("test.mpk", "rb") as f:
        msgpack.load(f)


def yml_serialization():
    with open("test.yml", "w") as f:
        yaml.dump(convert_data, f)


def yml_deserialization():
    with open("test.yml", "r") as f:
        yaml.load(f, Loader=yaml.FullLoader)


def pickle_serialization():
    with open("test.pickle", "wb") as f:
        pickle.dump(convert_data, f)


def pickle_deserialization():
    with open("test.pickle", "rb") as f:
        pickle.load(f)


serialization = {"xml": (xml_serialization, xml_deserialization),
                 "avro": (avro_serialization, avro_deserialization),
                 "json": (json_serialization, json_deserialization),
                 "mpk": (mpk_serialization, mpk_deserialization),
                 "yml": (yml_serialization, yml_deserialization),
                 "pickle": (pickle_serialization, pickle_deserialization)}


@app.route('/get_result/<stype>', methods=['POST'])
def get_result(stype: str):
    if stype not in serialization.keys():
        return "Unknown type"

    serialization_func, deserialization_func = serialization[stype]

    stime = round(timeit(serialization_func, default_timer, number=100), 3)
    dtime = round(timeit(deserialization_func, default_timer, number=100), 3)

    file_size = os.path.getsize(f'test.{stype}')
    result = f"File size: {file_size}; " \
             f"Serialization time: {stime}ms; " \
             f"Deserialization time: {dtime}ms\n"
    return result


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)
