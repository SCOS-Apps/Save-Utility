import sys
import configparser
import subprocess

global config

config = configparser.ConfigParser()

try:
    sys.argv[2]
except IndexError:
    print("File has not been set. Proceed with caution.")
else:
    config.read(sys.argv[2])
    print("MEM Set")

global read
global write
global open

def read(direct, variable):
    print(config[direct][variable])
def write(direct, variable, change):
    config[direct][variable] = change
def open(file):
    try:
        print(file)
    except:
        print("File not found or not specified.")
    else:
        try:
            config.read(file)
        except:
            print("File does not exist or something else happend.")
        else:
            config.read(file)

try:
    sys.argv[1]
except IndexError:
    subprocess.run("py " + input("File to execute: "))
else:
    subprocess.run("py " + sys.argv[1])
    print("MEM Set")