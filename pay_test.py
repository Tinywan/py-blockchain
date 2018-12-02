#!/usr/bin/python3


import time
import hashlib


def show_time():
    print("1111111")


time.sleep(1)
show_time()
print("22222222222")

m = hashlib.md5(b"22222")
print(m.hexdigest())

str = "€20"
print(str.encode("utf-8"))
print(str.encode("utf-8").decode("utf-8"))
