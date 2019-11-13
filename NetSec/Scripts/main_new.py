import os,pandas as pd
from xml.dom.minidom import parseString
#import xml.etree.ElementTree as ET
opcode_dict={}
mnemonic_dic={}
opcode_file=open("processed.txt")
for line in opcode_file:                    
    val,key=line.split()               
    opcode_dict[key]=val.strip()
    mnemonic_dic[val]=0
# =============================================================================
# f1 = open("test.csv", "w")
# writer = csv.DictWriter(f1, opcode_dict.values())
# writer.writeheader()
# f1.close()
# =============================================================================
exten =  ".smali"
INTERNET={}
CALENDAR		={}
CAMERA        ={}
CONTACTS        ={}
LOCATION        ={}
PHONE           ={}
RECORD_AUDIO    ={}
SENSORS         ={}
SMS             ={}
STORAGE         ={}
for folder in next(os.walk('.'))[1]:
    try:
        opcode_dic = {**mnemonic_dic}
        for dname, names, files in os.walk(os.getcwd()+"/"+folder):
            for name in files:
                if name.lower().endswith(exten):
                    #print(os.path.join(dname, name))
                    f2=open(os.path.join(dname, name), encoding="utf8")
                    for line in f2:
                        opcode1=line.lstrip()
                        if len(opcode1)==0 or not opcode1[0].isalpha():
                            continue    
                        else:
                            opcode=opcode1.split()[0]
                            if opcode in opcode_dict:
                                mnemonic=opcode_dict[opcode];
                                opcode_dic[mnemonic]=opcode_dic[mnemonic]+1
                    f2.close()

        data = ''
        with open(os.getcwd()+"/"+folder+"/"+"AndroidManifest.xml", encoding="utf8") as mfest:
            data = mfest.read()
        dom = parseString(data)
        nodes = dom.getElementsByTagName('uses-permission')
        # Iterate over all the uses-permission nodes
        for node in nodes:
           pp=node.getAttribute('android:name')
           if 'android.permission' in pp:
                permi=pp.split('.')[2]
                if 'INTERNET' in permi:
                    INTERNET[folder]=opcode_dic
                if 'CALENDAR' in permi:
                    CALENDAR[folder]=opcode_dic
                if 'CAMERA' in permi:
                    CAMERA[folder]=opcode_dic
                if 'CONTACTS' in permi:
                    CONTACTS[folder]=opcode_dic
                if 'LOCATION' in permi:
                    LOCATION[folder]=opcode_dic
                if 'PHONE' in permi:
                    PHONE[folder]=opcode_dic
                if 'RECORD_AUDIO' in permi:
                    RECORD_AUDIO[folder]=opcode_dic
                if 'SENSORS' in permi:
                    SENSORS[folder]=opcode_dic
                if 'SMS' in permi:
                    SMS[folder]=opcode_dic
                if 'STORAGE' in permi:
                    STORAGE[folder]=opcode_dic
    except FileNotFoundError:
        continue
    except UnicodeDecodeError:
        continue
    print("Apk",folder,"Done !!")
df_INTERNET = pd.DataFrame.from_dict(INTERNET, orient='index').fillna(0)
df_INTERNET.to_csv("INTERNET.csv", sep=',')
df_CALENDAR = pd.DataFrame.from_dict(CALENDAR, orient='index').fillna(0)
df_CALENDAR.to_csv("CALENDAR.csv", sep=',')
df_CAMERA = pd.DataFrame.from_dict(CAMERA, orient='index').fillna(0)
df_CAMERA.to_csv("CAMERA.csv", sep=',')
df_CONTACTS = pd.DataFrame.from_dict(CONTACTS, orient='index').fillna(0)
df_CONTACTS.to_csv("CONTACTS.csv", sep=',')
df_LOCATION = pd.DataFrame.from_dict(LOCATION, orient='index').fillna(0)
df_LOCATION.to_csv("LOCATION.csv", sep=',')
df_PHONE = pd.DataFrame.from_dict(PHONE, orient='index').fillna(0)
df_PHONE.to_csv("PHONE.csv", sep=',')
df_RECORD_AUDIO = pd.DataFrame.from_dict(RECORD_AUDIO, orient='index').fillna(0)
df_RECORD_AUDIO.to_csv("RECORD_AUDIO.csv", sep=',')
df_SENSORS = pd.DataFrame.from_dict(SENSORS, orient='index').fillna(0)
df_SENSORS.to_csv("SENSORS.csv", sep=',')
df_SMS = pd.DataFrame.from_dict(SMS, orient='index').fillna(0)
df_SMS.to_csv("SMS.csv", sep=',')
df_STORAGE = pd.DataFrame.from_dict(STORAGE, orient='index').fillna(0)
df_STORAGE.to_csv("STORAGE.csv", sep=',')
                
