#head:
from flask import Flask
import time
import datetime
import os
os.system("clear")

red="\033[31m"
green="\033[32m"
yellow="\033[33m"
blue="\033[34m"
purple="\033[35m"
cyan="\033[36m"
white="\033[37m"
def w() :
	time.sleep(0.5)
	print("\n")
####################################
#script:
print(red,"""  ___ ___ __  __ 
 / __/ __|  \/  |""")
print(green,"""\__ \__ \ |\/| |""")
print(cyan,"""|___/___/_|  |_|1.1""")
print(blue,"simple server maker(localhost), by REVENGE©®,REISS CLAN©®")
w()
print("NOTICE: THIS SERVER WILL BE ACTIVE ON YOUR",purple,"LOCAL HOST")
w()

print(yellow,"INSERT A HTML SOURCE CODE TO ACTIVATE THE SERVER.")
w()
w()
print(green)
htmlcode=input("INSERT THE HTML SOURCE CODE HERE: ")
w()
print(purple,"THE SERVER STARTING...")
time.sleep(4)
print(green,"THE SERVER STARTED")
w()
app=Flask(__name__)
@app.route("/")
def home():
	return(htmlcode)
try:
	app.run()
except:
	print(red,"oh, your",purple,"adress",red,"seem is already in use,sooo go to the page that running the server or restart th phone.")
