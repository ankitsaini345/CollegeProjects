import pandas as pd
import os

for dname, names, files in os.walk(os.getcwd()+"\\Benign"):
	for name in files:
		if name.lower().endswith(".csv"):
			f2=open(os.path.join(dname, name))
			data = pd.read_csv(f2)
			# print(data)
			columns = data.columns[1:]
			# print(columns)
			rows =len(data.index)
			normalised_frq = {}
			for i in columns:
				normalised_frq[i] = data[i].sum()/1000
			normalised_frequency_opcode = pd.DataFrame([normalised_frq])
			# print(normalised_frequency_opcode.as_matrix)
			# for k, v in normalised_frq.items():
			#     print(k, v)
			normalised_frequency_opcode = normalised_frequency_opcode.transpose()   
			normalised_frequency_opcode =  normalised_frequency_opcode.rename(columns={normalised_frequency_opcode.columns[0]:'benign'})
			# print(normalised_frequency_opcode)
			normalised_frequency_opcode.to_csv(os.getcwd()+"\\Normalised\\"+"Benign_"+name,sep =',', encoding='utf-8')

for dname, names, files in os.walk(os.getcwd()+"\\Malware"):
	for name in files:
		if name.lower().endswith(".csv"):
			f2=open(os.path.join(dname, name))
			data = pd.read_csv(f2)
			# print(data)
			columns = data.columns[1:]
			# print(columns)
			rows =len(data.index)
			normalised_frq = {}
			for i in columns:
				normalised_frq[i] = data[i].sum()/1000
			normalised_frequency_opcode = pd.DataFrame([normalised_frq])
			# print(normalised_frequency_opcode.as_matrix)
			# for k, v in normalised_frq.items():
			#     print(k, v)
			normalised_frequency_opcode = normalised_frequency_opcode.transpose()   
			normalised_frequency_opcode =  normalised_frequency_opcode.rename(columns={normalised_frequency_opcode.columns[0]:'benign'})
			# print(normalised_frequency_opcode)
			normalised_frequency_opcode.to_csv(os.getcwd()+"\\Normalised\\"+"Malware_"+name,sep =',', encoding='utf-8')
	