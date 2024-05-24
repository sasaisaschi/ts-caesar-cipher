from flask import Flask, request, jsonify, render_template
import string

alphabets = string.ascii_lowercase * 2
encode_inputs = ["encode", "encrypt"]
decode_inputs = ["decode", "decrypt"]
valid_inputs = encode_inputs + decode_inputs

def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    dir = "encrypting"
    # if the direction is valid, then make the shift amount negative
    if cipher_direction in decode_inputs:
        dir = "decrypting"
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            # get the index
            index = alphabets.index(char)
            # shift the index
            new_index = index + shift_amount
            # add the alphabet at the given index to the end string
            end_text += alphabets[new_index]
        else:
            # if the char is not an alphabet, then add it as it is without shifting
            end_text += char
    return end_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar', methods=['POST'])
def caesar_route():
    data = request.get_json()
    cipher_direction = data['cipher_direction']
    start_text = data['start_text']
    shift_amount = int(data['shift_amount'])
    result = caesar(cipher_direction, start_text, shift_amount)
    return jsonify(result=result)