#strings  command for hexdump data
import subprocess 

filename=input("Enter the name of file : ")

with open('hexdumpfile.txt','w') as f:
	p1=subprocess.run(['binwalk','-w','--hexdump',filename],stdout=f,text=True)
p2=subprocess.run(['strings','-a',f],stdout=subprocess.PIPE,text=True)
print(p2.stdout)