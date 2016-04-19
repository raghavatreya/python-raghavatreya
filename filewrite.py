'''
File write
and file append

'''
text = "hello world !\n New Line!"
saveFile=open("example.txt",'w')
## open and clear the file

saveFile.write(text)
saveFile.close()

## appending a file
##open("example.txt",'a')

##readMe = open("example.txt",'a').read()  // readlines()

##
