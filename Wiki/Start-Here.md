# Using SSave

First thing firsts, use ```pip install ssave``` to install the module, then import it using:
```py
import ssave
```
After that, open your file with:
```py
ssave.open("Path/To/File.ini")
```
or include it as a in-line parament:
```cmd
py file.py Path/To/File.ini
```
and close it with:
```py
ssave.close()
```

## Working With Files

Now that we can open and close files, it's time to edit and read!

### Reading Files

To read files, use:
```py
ssave.read(N1, N2)
```
_N1 represents the class, N2 represents the variable._

### Writing Files

To write files, use:
```py
ssave.write(N1, N2, N3)
```
_N1 represents the class, N2 represents the variable and N3 representing the variable's value._