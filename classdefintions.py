import json
import os
from cryptography.fernet import Fernet

## NOTE TO GRADER ##
'''
I was assisted by generative AI to show me how to encrypt and decrypt strings using this code. I based off many procedures (read, add_item) on this code.

# Generate a Fernet key
key = Fernet.generate_key()
fernet = Fernet(key)

# Encrypt
plaintext = 'secret message'
encrypted_bytes = fernet.encrypt(plaintext.encode())
encrypted_string = encrypted_bytes.decode()

# Decrypt
decrypted_bytes = fernet.decrypt(encrypted_bytes)
decrypted_string = decrypted_bytes.decode()
print(decrypted_string)  # Output: "secret message"
'''

secret_key = bytes(os.environ['key'], 'utf-8')
fernet = Fernet(secret_key)

schema = {}

class db:
  def __init__(self, dbname, shouldencrypt):
    self.dbname = dbname
    self.data = {}
    self.shouldencrypt = shouldencrypt

  def initalize(self):
    try:
      f = open(self.dbname, "r")
      res = json.loads(f.read())
      self.data = res
    except:
      t = open(self.dbname, "w")
      t.write(json.dumps(schema))
      self.data = schema.copy()

    return "Successfully setup db"

  def add_item(self, key, value):
    if self.shouldencrypt:
      encryptedbytes = fernet.encrypt(value.encode())
      encrypted_value = encryptedbytes.decode()
      self.data[key] = encrypted_value
    else:
      self.data[key] = value

  def remove(self, key):
    del self.data[key]

  def read_key(self, key):
    if self.shouldencrypt:
      decryptedbytes = fernet.decrypt(self.data[key].encode())
      decrypted_value = decryptedbytes.decode()
      return decrypted_value
    else:
      return self.data.get(key)

  # bad practice - worse than using print(database.read(key) != None)
  def exists(self, key):
    return self.read_key(key) != None

  def clear(self):
    self.data = {}
  
  def size(self):
    return len(self.data)

  def finish(self):
    t = open(self.dbname, "w")
    t.write(json.dumps(self.data))

  def findValue(self, value):
    vals = list(dict.values(self.data))
    keys = list(dict.keys(self.data))
    for i in range(len(vals)):
      if self.read_key(keys[i]) == value:
        return list(dict.keys(self.data))[i]
    return None