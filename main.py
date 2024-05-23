from classdefintions import db
from termcolor import colored
from progress.bar import Bar
import tkinter as tk
from tkinter import *

# setup
database = db("db.txt", True)
# print(colored(database.initalize(), 'red'))

def setupBar(progressValue, steps):
  bar = Bar(progressValue, max=steps)
  
  status = None
  
  for i in range(steps):
    if i == 1:
      status = database.initalize()
    bar.next()

  bar.finish()

  print(colored(status, 'red', attrs=['reverse', 'blink']))

setupBar('Reading database file...', 2)

window = tk.Tk()
window.title("tk")
# window.geometry("800x400")

# TODO: add a font here
optionTitle = tk.Label(window, text = 'Add, remove or read an item: ')

key_var = tk.StringVar()
value_var = tk.StringVar()

lookupKeyLabel = tk.Label(window, text = 'Key: ', font=('calibre',10, 'bold'))
lookupKey = tk.Entry(window, textvariable = key_var, font = ('calibre',10,'normal'))
lookupValueLabel = tk.Label(window, text = 'Value: ', font=('calibre',10, 'bold'))
lookupValue = tk.Entry(window, textvariable = value_var, font = ('calibre',10,'normal'))

databaseDataTextWidget = Text(window, height = 5, width = 52)
databaseDataTextWidget.insert("end", str(database.data))
databaseReadTextWidget = Text(window, height = 5, width = 52)
databaseReadTextWidget.insert("end", 'Data will show up here after you press read item for a specific key or value. This exists because the values are encrypted.')

def reload():
  databaseDataTextWidget.delete(1.0, "end")
  databaseDataTextWidget.insert("end", str(database.data))

def readItem():
  databaseReadTextWidget.delete(1.0, "end")
  databaseReadTextWidget.insert("end", database.read_key(str(key_var.get())))

def findValueFromButtonPress():
  databaseReadTextWidget.delete(1.0, "end")
  valueFromTkinterGUI = value_var.get()
  val = database.findValue(valueFromTkinterGUI)
  if val != None:
    databaseReadTextWidget.insert("end", val)
  else:
    databaseReadTextWidget.insert("end", "Doesn't exist")
  
reloadValues = tk.Button(window, text='Reload values', width=25, command=reload)
addItem = tk.Button(window, text='Add Item', width=25, command=lambda: database.add_item(key_var.get(), value_var.get()))
removeItem = tk.Button(window, text='Remove Item', width=25, command=lambda: database.remove(key_var.get()))
readItem = tk.Button(window, text='Read Item', width=25, command=readItem)
findValueButton = tk.Button(window, text='Find Value', width=25, command=findValueFromButtonPress)
saveToDatabase = tk.Button(window, text='Save to database file', width=25, command=database.finish)

dataLabel = tk.Label(window, text = 'Data from the file: ', font=('calibre',10, 'bold'))
dataFromRead = tk.Label(window, text = 'From Read Item', font=('calibre',10, 'bold'))

dataLabel.grid(row=0, column=0)
dataFromRead.grid(row=0, column=1)
databaseDataTextWidget.grid(row=1, column=0)
databaseReadTextWidget.grid(row=1, column=1)
optionTitle.grid(row=2, column=0)
lookupKeyLabel.grid(row=3,column=0)
lookupKey.grid(row=3,column=1)
lookupValueLabel.grid(row=4, column=0)
lookupValue.grid(row=4, column=1)
addItem.grid(row=5, column=0)
removeItem.grid(row=5, column=1)
readItem.grid(row=6, column=0)
findValueButton.grid(row=6, column=1)
reloadValues.grid(row=7, column=0)
saveToDatabase.grid(row=7, column=1)

# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)

window.mainloop()

# while True:
#   wannasave = input("wanna save? (y/n)")
#   if wannasave == 'y':
#     database.finish()
#   print(database.data)
#   add = input("wanna add a key? ")
#   add2 = input("wanna add a value? ")
#   if add != '' and add2 != '':
#     database.add_item(add, add2)

# all commands
# print(database.data)

# for i in range(1000000):
#   database.add_item(str(i), f"World{i}")
  # print(database.read(str(i)))
# print(database.size())
# database.remove("Hello")
# print(database.data)

# you must run this at the end to update the db
# database.finish()