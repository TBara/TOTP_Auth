import os
import pyotp
import qrcode

env_domain = 'DOMAIN'
env_issuer = 'ISSUER'
env_key = 'TOTP_KEY'


def gen_qr():
    qr = pyotp.totp.TOTP(os.environ[env_key]).provisioning_uri(\
        name=os.environ[env_domain], \
        issuer_name=os.environ[env_issuer])
    img = qrcode.make(qr)
    img.save('./img_' + os.environ[env_domain] + '.jpg')
    return img