import pyotp


def gen_otp():
    print("Generating OTP")
    key = pyotp.random_base32()
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    print("Current OTP:", totp.now())