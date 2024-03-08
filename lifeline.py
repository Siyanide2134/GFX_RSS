import os

# Path to the file
file_path = '/usr/lib/python3/dist-packages/cap1xxx.py'

# Read the file
with open(file_path, 'r') as file:
    filedata = file.read()

# Replace 'isAlive' with 'is_alive'
filedata = filedata.replace('isAlive', 'is_alive')

# Write the file out again
with open(file_path, 'w') as file:
    file.write(filedata)
