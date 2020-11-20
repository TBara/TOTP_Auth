import sys
from sys import argv
from project.gen_otp import gen_otp as otp
from project.gen_qr import gen_qr as qr


# Main driver function. Accepts two comman line arguments
# The second argument indicateds which function to execute
if __name__ == '__main__':
    if len(sys.argv) == 2:
        if str(sys.argv[1]) == 'get-otp':
            otp()
        elif str(sys.argv[1]) == 'generate-qr':
            qr()
        else:
            print("Invalid command " + str(sys.argv[1]))
    else:
        print("Invalid arguments")