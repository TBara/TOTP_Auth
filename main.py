import sys
import os
import pyotp
from sys import argv
from project.gen_otp import gen_otp as otp
from project.gen_qr import gen_qr as qr
from settings import load_dotenv

# Main driver function. Accepts two comman line arguments
# The second argument indicateds which function to execute
if __name__ == '__main__':
    
    # Load .env environment variables
    load_dotenv()

    # Readf command line args
    if len(sys.argv) == 2:
        if str(sys.argv[1]) == 'get-otp':
            otp()
        elif str(sys.argv[1]) == 'generate-qr':
            qr()
        else:
            print("Invalid command " + str(sys.argv[1]))
    else:
        print("Invalid arguments")