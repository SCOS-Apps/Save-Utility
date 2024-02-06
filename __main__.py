import sys
import configparser
import os

global config

config = configparser.ConfigParser()

try:
    sys.argv[2]
except IndexError:
    print("File has not been set. Proceed with caution.")
else:
    config.read(sys.argv[2])
    print("MEM Set")

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
    sys.argv[3]
except IndexError:
    fileExecution = input("File to execute: ")
else:
    fileExecution = sys.argv[3]
    print("MEM Set")
finally:
    os.system(fileExecution)