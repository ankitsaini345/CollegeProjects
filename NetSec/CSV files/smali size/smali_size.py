import os,csv
Sum_smali={}
for folder in next(os.walk('.'))[1]:
	sum=0
	for dname, names, files in os.walk(os.getcwd()+"/"+folder):
			for name in files:
				if name.lower().endswith(".smali"):
					sum=sum+round(os.path.getsize(os.path.join(dname, name))/1024,0)
	Sum_smali[folder]=sum
	print(folder+" done")

with open('smali.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    for row in Sum_smali.items():
        writer.writerow(row)
print("done open smali.csv now")