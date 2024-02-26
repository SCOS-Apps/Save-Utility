import sys
import configparser

config = configparser.ConfigParser()
print("SCOS Save Utility is Included.")
config.read("data.ini")
print(config.read("Info", "Version"))