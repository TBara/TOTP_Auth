# TOTP_Auth
Time-based One Time Password sample application

How to run the app
1. Install required packages by running commands: 
    a. pip install qrcode[pil]
    b. pip install python-dotenv
    c. pip install qrcode
    d. pip install pyotp
2. Run command: python3 main.py generate-qr
3. QR image file will be generated in root directory
4. Use the image to create an account in Google Authenticator app
5. Run command: python3 main.py get-otp
6. Comapre the codes. They will match.

This program was successfully tested on Google Authenticator and Authy. The underlying assumptions are that this program will 
generate codes for one domain and one issuer where the secret key remains constant. These constants are listed in the .env file.
The TOTP code and the provisioning URI are generated with the help of pyotb library. The qr code is generated by qrcode library. 
File containing environment variables is provided with the project. Accessing it requires the use of python-dotenv library. 