fo = open("file.txt","r+")

fo.write("this the first file create using python")
print(fo.read(30))
fo.seek(0,0)
print(fo.tell())
print(fo.readable())

fo.close()