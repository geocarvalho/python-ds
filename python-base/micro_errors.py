#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ask forgiveness than permission

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: use retry
else:
    print("Success!")
finally:
    print("Run anyways.")

try:
    print(names[2])
except:
    print("[ERROR] Missing name in the list")
    sys.exit(1)