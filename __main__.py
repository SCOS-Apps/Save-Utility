import configparser
import __read__ as read
import sys

config = configparser.ConfigParser()

try:
    sys.argv[2]
except IndexError:
    config.read(input("File Path: "))
else:
    print("MEM Set")

print("SCOS Config & Save Editor and reader.")

print("NOTE: Do NOT close the program while in write function.")

print("Functions:\n1. Read\n2. Write\n3. Exit")

selection = input("Selection: ")
if selection == "1" or "read":
    N1 = input("Define Class: ")
    N2 = input("Define Class Variable: ")
    print(read.read(N1, N2))
elif selection == "2" or "write":
    N1 = input("Define Class: ")
    N2 = input("Define Class Variable: ")
    N3 = input("Define Change: ")
    read.write(N1, N2, N3)
    print