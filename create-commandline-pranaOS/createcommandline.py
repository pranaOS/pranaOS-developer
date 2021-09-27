import os
import time

Y = (['yes', 'y', 'YES', 'Y'])
N = (['no', 'n', 'NO', 'N'])

def createCommandLineApplication():
    createcliapp = input("hey you need to create a application for pranaOS Y / N ")

    if createcliapp in Y:
        createApplication()    
    else:
        print('OK BYE')


def createApplication():
    nameofapp = input("name your app >> ")
    os.system('cd userland/utilities')
    os.system('mkdir' + nameofapp)
    os.system('cd' + nameofapp)
    os.system('touch main.cpp; touch BUILD.gn; touch .info.mk')
    print('created files writing a simple code in it')
    time.sleep(1)
    print('writing some code to files')
    time.sleep(1)
    f = open("main.cpp")
    f.write("#include <stdio.h> int main() { /* code /* } return 0;")
    f.close()
    print('added some code to the file')
    time.sleep(1)
    print(f.read())

def banner():
    print("CREATE COMMAND LINE APPLICATION FOR pranaOS :) ")

def main():
    banner()

if __name__ == "__main__":
    main()


