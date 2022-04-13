import telnetlib
import json
import codecs
import base64
from Crypto import number
import sys
from binascii import unhexlify

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def decrypt(type, encoded_stream):
    if type == "base64":
        decoded_stream = base64.b64decode(encoded_stream).decode("utf-8")
    elif type == "hex":
        decoded_stream = bytes.fromhex(encoded_stream).decode("utf-8")
    elif type == "rot13":
        decoded_stream = codecs.decode(encoded_stream, 'rot_13')
    elif type == "bigint":
        decoded_stream = number.long_to_bytes(int(encoded_stream, 16)).decode("utf-8")
    elif type == "utf-8":
        decoded_stream = "".join(chr(o) for o in encoded_stream)

    return decoded_stream

def execute():
    received = json_recv()

    try:
        print(received["flag"]) 
        sys.exit(0)
    except KeyError:
        print("No flag")

    try:
        print(received["error"]) 
        sys.exit(1)
    except KeyError:
        print("No decoding errors")

    print(received)
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    
    decoded = decrypt(received["type"], received["encoded"])
    print("Decoded value:")
    print(decoded)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

for index in range(0, 101):
    print("Index:", index)
    execute()
    print("--------------------------------------")
