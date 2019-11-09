from options import *
from choices import *
import sys
sys.path.append('./options/crypt')
from message import start

def main():
    _choice = choice()
    if _choice == 0:
        start()


if __name__ == "__main__":
    main()