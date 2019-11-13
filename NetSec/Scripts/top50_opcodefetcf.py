import numpy as np
import pandas as pd
import os

data = pd.read_csv('PHONE_malicious.csv')
# print(data)
columns = data.columns[1:]
# print(columns)
rows =len(data.index)
normalised_frq = {}
for i in columns:
    normalised_frq[i] = data[i].sum()/1000
normalised_frequency_opcode_malicious = pd.DataFrame([normalised_frq])
# print(normalised_frequency_opcode.as_matrix)
# for k, v in normalised_frq.items():
#     print(k, v)b
normalised_frequency_opcode_malicious = normalised_frequency_opcode_malicious.transpose()
normalised_frequency_opcode_malicious =  normalised_frequency_opcode_malicious.rename(columns={normalised_frequency_opcode_malicious.columns[0]:'malicious'})
# print(normalised_frequency_opcode_malicious)
normalised_frequency_opcode_malicious.to_csv('normalised_frequency_opcode_malicious.csv',sep =',', encoding='utf-8')

result = pd.concat([normalised_frequency_opcode, normalised_frequency_opcode_malicious], axis=1)
# print(result)

result['differnce'] = abs(result['benign'] - result['malicious'].astype(float))
result = result.sort_values(['differnce'], ascending=False)
result =  result.head(50)
print(result.head(50))
result.to_csv('OP_TOP50_DIFF.csv',sep =',', encoding='utf-8')
#there is an opcode 0.1, at 99th index.
# columns = list(data.columns[1:])
# print(columns.index('0.1'))