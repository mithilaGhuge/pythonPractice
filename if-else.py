#!/bin/python3

import math
import os
import random
import re
import sys


def main():
    n = int(input().strip())
    numMod = n%2

    print(numMod)
    if n in range(1,100):
        print(n)
        if numMod != 0 :
            print("Weird")
        elif numMod==0 and (n in range(2,5)):
            print("Not Weird")
        elif numMod==0 and (n in range(6,20)):
            print("Weird")
        elif numMod==0 and n>20:
            print("Not Weird")

main()