import subprocess
p1=subprocess.run(['cat','ReportOutput.md'],capture_output=True,text=True)
print(p1.stdout)