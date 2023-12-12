from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        shift = int(request.form['shift'])
        ciphertext = caesar_cipher_encrypt(plaintext, shift)
        return render_template('index.html', ciphertext=ciphertext)

    return render_template('index.html', ciphertext='')

if __name__ == '__main__':
    app.run(debug=True)
