import os
import fnmatch

Extension = str(input("Extension (ecd,inp,txt) ?"))
Command = str(input("Command ?"))
Name = str(input("Name of end file?"))

FileList = os.listdir()
FileListNew = []

for x in FileList:
	if fnmatch.fnmatch(x,'*.'+Extension):
		y = Command + " " + str(x)
		FileListNew.append(y)

with open(Name,"x") as output:
	for item in FileListNew:
		output.write("%s\n" % item)
