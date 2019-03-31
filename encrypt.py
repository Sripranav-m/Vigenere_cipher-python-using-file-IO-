#Created By Sripranav Mannepalli
print("-----Encryption-----")
print("Enter the file name if the file is in same folder",end=(" (or) "))
print("Enter the total file path including file name--",end=("\n"))
file1name=input()
print("Specify the name of the file in which you want your encrypted data--",end=("\n"))
file2name=input()
vckey=input("Enter the key to encrypt your data(\"only alphabets(a to z)\"), (which must be entered again to decrypt your data)--")
vckey.lower()
file1=open(file1name)
file1.seek(0)
file1content=file1.read()
file1content.lower()
file1.close()
nv=0 #number of characters in given key
nc=0 #number of characters in given file
for char in file1content:
    nc+=1
    if char=="\n":
        nc-=1
for char in vckey:
    nv+=1
newkey=""
i=0
j=0
if nv>=nc:
    for char in vckey:
        if i<nc:
            newkey=newkey+char
            i+=1
elif nv<nc:
    while j!=nc:
        if i<nv:
            newkey=newkey+vckey[i]
            i+=1
            j+=1
        else:
            i=i-nv 
file2=open(file2name,"w")
i=0  
for char in file1content:
    if char!="\n" and char!=" ":
        new=(ord(char)+ord(newkey[i])-(2*ord('a')))%26
        new=new+ord("a")
        new=chr(new)
        file2.write(new)
        i+=1
    else:
        if char=="\n":
            file2.write("\n")
        elif char==" ": 
            file2.write(" ")
file2.close()