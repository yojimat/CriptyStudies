'''
Given the string "label", XOR each character with the integer 13.
'''
from pwn import xor

print("pwn:", xor("label", 13).decode("utf-8"))

string_binary = []
for ch in "label":
    string_binary.append(chr(ord(ch) ^ 13))

print("".join(string_binary))
