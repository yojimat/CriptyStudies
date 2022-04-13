import base64
import codecs
from Crypto.Util import number

integer_array = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("".join(chr(o) for o in integer_array))

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
bytes_string = bytes.fromhex(hex_string).decode("utf-8")
print(bytes_string)

base64_hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
base64_string = bytes.fromhex(base64_hex_string)
base64_string = base64.b64encode(base64_string).decode("utf-8")
print(base64_string)

interger_message = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
bytes_message = number.long_to_bytes(interger_message)
print(bytes_message.decode("utf-8"))

encoding_challenge_message = "66726573636f5f64656661756c7465725f656e747279776179"
bytes_challenge_message = bytes.fromhex(encoding_challenge_message)
print(bytes_challenge_message)

decoded_stream = number.long_to_bytes(int("0x726f776572735f736172636f6d615f636f75706c6564", 16)).decode("utf-8")
decoded_stream = codecs.decode("jbbyl_Naxnen_zvfsbeghar", 'rot_13')
decoded_stream = base64.b64decode("b3B0aW1pc3RpY19WaWNrc2J1cmdfS2FyYWNoaXM=").decode("utf-8")
print(decoded_stream)


