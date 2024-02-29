import sys
import configparser

filepath = None
global config

config = configparser.ConfigParser()
print("SCOS Save Utility is Included.")

def read(direct, variable):
    print(config[direct][variable])

def write(direct, variable, change):
    try:
        config.set(direct, variable, change)
    except:
        try:
            config.add_section(direct)
            config.set(direct, variable, change)
        except:
            print("Unknown Error has Occurred.")


def sopen(file):
    global filepath
    filepath = file
    try:
        open(file).read()
    except:
        print("File not found or not specified.")
    else:
        try:
            config.read(file)
        except:
            print("File does not exist or something else happened.")

def create(filePath):
    try:
        open(filePath, "x")
    except:
        print("File exist or something else happend.")

try:
    len(sys.argv[1])
except:
    print("File not found or not specified.")
else:
    try:
        config.read(sys.argv[1])
    except:
        print("File does not exist or something else happened.")
    else:
        config.read(sys.argv[1])