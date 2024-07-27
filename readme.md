# Python-DB
A database I created for my AP CSP create task in March 2024. (I got a 4 out of 5 lol)

https://github.com/ZarmDev/Python-DB/assets/80705328/6d0f22e7-38e2-4dc3-9fd2-9e0348bddf98

# How to run?
It runs normally unless you use the encrypted version, which means you have to set a environment variable to a fernet key.
I honestly don't know how I did it but I just used fernet_create_key or something like that and then it worked.
It should look like this in env:
```
key=thefernetcreatekeythingy
```

# What does it look like in db.txt?
Example of db.txt:
{"value": "gAAAAABmAZbAvrkthgsGlL8BUbScAh_lKfd67Ic9FzfunTyalfBy42tP_xI_GhEmE-bJM7lUer1O2Qc5pXtCDRqnT1o8yTc3fg=="}

# Benchmarks
2 seconds for 10,000 encrypted items
26 seconds for 100,000 encrypted items

# Stuff I wrote
2 seconds for 10,000 encrypted items!!!!
26 seconds for 100,000 encrypted items
also pls don't switch from encrypted to unencrypted with a existing db.txt b/cuz
it will definitely break :(
also there is no error handling so good luck 🫡
