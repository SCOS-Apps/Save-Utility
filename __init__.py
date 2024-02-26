import sys
import configparser
import easy

config = configparser.ConfigParser()
print("SCOS Save Utility is Included.")
config.read("data.ini")
print(config.read("Info", "Version"))

try:
    sys.argv[1]
except IndexError:
    print("No file in sys.argv[1].")
else:
    easy.sopen(sys.argv[1])