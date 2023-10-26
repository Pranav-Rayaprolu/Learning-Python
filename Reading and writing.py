#writing in a file
f=open("meow.txt","w")
f.write("i love pussy cats so much")
f.close()
#appending in a file
f=open("meow.txt","a")
f.write("\nmeow!")
f.close()
#reading in a file
f=open("meow.txt","r")
print(f.read())
f.close()
9