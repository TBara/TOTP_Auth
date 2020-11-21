import sys
import os
from sys import argv
from project.gen_otp import gen_otp as otp
from project.gen_qr import gen_qr as qr

env_domain = 'domain'
env_issuer = 'issuer'
env_key = 'totp_key'

domain = 'Barabast@oregonstte.edu'
issuer = 'My OTP App'
totp_key = ''

def set_env_var():
    if os.environ[env_domain] != domain:
        os.environ[env_domain] = domain
    
    if os.environ[env_issuer] != issuer:
        os.environ[env_issuer] = issuer

    if env_key not in os.environ:
        pass

# Main driver function. Accepts two comman line arguments
# The second argument indicateds which function to execute
if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        set_env_var()
        if str(sys.argv[1]) == 'get-otp':
            otp()
        elif str(sys.argv[1]) == 'generate-qr':
            qr()
        else:
            print("Invalid command " + str(sys.argv[1]))
    else:
        print("Invalid arguments")