"""Author: Julian Bartolone
This code verifies the first test in the Vivado simulation code for the AES-128
core of the author's senior design project. It verifies that the desired
inputs/outputs of to the FPGA AES tool match the inputs written in this Python
code and the output of the Python AES engine. It also provides an average for
the time it takes to perform the encryption on the single-block input with a
sample size of 10000000.
"""

from Crypto.Cipher import AES
import time

def AES128Verification():
    key = 0b00101011011111100001010100010110001010001010111011010010101001101010101111110111000101011000100000001001110011110100111100111100
    state = 0b00110010010000111111011010101000100010000101101000110000100011010011000100110001100110001010001011100000001101110000011100110100
    out = 0b00111001001001011000010000011101000000101101110000001001111110111101110000010001100001011001011100011001011010100000101100110010
    out = out.to_bytes(16, 'big')
    start = time.time()
    cipher = AES.new(key.to_bytes(16, 'big'), AES.MODE_ECB)
    message = cipher.encrypt(state.to_bytes(16, 'big'))
    end = time.time()
    if out != message:
        print("Python AES output does not match FPGA AES output")
    return end - start

print("True if Python key matches FPGA simulation key:", 0b00101011011111100001010100010110001010001010111011010010101001101010101111110111000101011000100000001001110011110100111100111100 == 0x2b7e151628aed2a6abf7158809cf4f3c)
print("True if Python state matches FPGA simulation state:", 0b00110010010000111111011010101000100010000101101000110000100011010011000100110001100110001010001011100000001101110000011100110100 == 0x3243f6a8885a308d313198a2e0370734)

lst = []
for i in range(10000000):
    element = AES128Verification()
    lst.append(element)

s = sum(lst)
avg = s/len(lst)
print("Average time to encrypt one 128-bit block with Python:", avg, "seconds")

