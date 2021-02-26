import subprocess
filename=input("Enter the name of yout file: ")
p1 = subprocess.run(['file',filename],stdout=subprocess.PIPE,text=True)
print (p1.stdout)
