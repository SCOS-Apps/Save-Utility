import sys
import configparser

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


def sopen(file):
    try:
        print(file)
    except:
        print("File not found or not specified.")
    else:
        try:
            config.read(file)
        except:
            print("File does not exist or something else happened.")
        else:
            config.read(file)


try:
    sys.argv[1]
except IndexError:
    file = open(input("File to execute: ")).read()
    exec(file)
else:
    file = open(sys.argv[1]).read()
    exec(file)
