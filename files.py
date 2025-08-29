file = input("Enter the file name: ")

try:
    with open(file, 'r'):
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename")
    file.close()
