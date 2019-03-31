#Created By Sripranav Mannepalli
print("-----Decryption-----")
print("Enter the file name if the file is in same folder",end=(" (or) "))
print("Enter the total file path including file name--",end=("\n"))
file3name=input()
print("Specify the name of the file in which you want your decrypted data--",end=("\n"))
file4name=input()
vcdkey=input("Enter the key to decrypt your data(\"only alphabets(a to z)\"), (which is entered during encryption)--")
vcdkey.lower()
file3=open(file3name)
file3.seek(0)
file3content=file3.read()
file3content.lower()
file3.close()
nv=0 #number of characters in given key
nc=0 #number of characters in given file
for char in file3content:
    nc+=1
    if char=="\n":
        nc-=1
for char in vcdkey:
    nv+=1
newkey=""
i=0
j=0
if nv>=nc:
    for char in vcdkey:
        if i<nc:
            newkey=newkey+char
            i+=1
elif nv<nc:
    while j!=nc:
        if i<nv:
            newkey=newkey+vcdkey[i]
            i+=1
            j+=1
        else:
            i=i-nv
file4=open(file4name,"w")
i=0  
for char in file3content:
    if char!="\n" and char!=" ":
        newd=(ord(char)-ord(newkey[i])+26)%26
        newd=newd+ord("a")
        newd=chr(newd)
        file4.write(newd)
        i+=1
    else:
        if char=="\n":
            file4.write("\n")
        elif char==" ":
            file4.write(" ")
file4.close()