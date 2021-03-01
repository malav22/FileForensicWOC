#This program will print the hexdump of the input file.

import subprocess 

filename=input("Enter the name of file : ")

p0=subprocess.run(['exif',filename],stdout=subprocess.PIPE,text=True)
print(p0.stdout)

p1=subprocess.run(['binwalk','-w','--hexdump',filename],stdout=subprocess.PIPE,text=True)
print(p1.stdout)