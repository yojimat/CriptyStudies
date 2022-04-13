#!/usr/bin/env python3
'''
PICO CTF Mod26
'''
FLAG = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
newFlag = []
for i, v in enumerate(FLAG):
    if v.isalpha():
        if v.islower():
            decimalChar = ord(v) + 13
            if decimalChar > 122:
                difference = decimalChar - 122
                decimalChar = 96 + difference
            newFlag.append(chr(decimalChar))
        else:
            decimalChar = ord(v) + 13
            if decimalChar > 90:
                difference = decimalChar - 90
                decimalChar = 64 + difference
            newFlag.append(chr(decimalChar))
    else:
        newFlag.append(v)

print("".join(newFlag))
