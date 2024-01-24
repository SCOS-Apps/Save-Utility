import sys
import configparser

global config

config = configparser.ConfigParser()

try:
    sys.argv[1]
except IndexError:
    config.read(input("File Path: "))
else:
    print("MEM Set")

def read(direct, variable):
    print(config[direct][variable])
def write(direct, variable, change):
    config[direct][variable] = change