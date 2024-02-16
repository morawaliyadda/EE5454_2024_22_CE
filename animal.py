import sys
def dognew():
    print('BawBaw')
def default():
    print('Hello')

def main():
    if sys.argv[1]=='dognew':
        dognew()

    else:
        default()
    

if __name__ == '__main__':
    main()


