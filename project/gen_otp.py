import os
import pyotp
import time


def gen_otp():
    totp = pyotp.TOTP(os.environ['TOTP_KEY'])
    print("Current TOTP:", totp.now())