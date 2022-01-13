#!/usr/bin/env python3

import os
import time

def banner():
    print("PRANAOS DEVELOPER CONSOLE")

def main():
    banner()

    print('checking requirements')
    os.system("nasm; gcc; g++")
    

if __name__ == "__main__":
    main()
