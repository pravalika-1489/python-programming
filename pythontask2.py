'''to accept a filename from the user & print the extension of that'''
filename=input("enter the filename: ")
ext=filename.split(".")
print("extension of the file is: "+repr(ext[-1]))
