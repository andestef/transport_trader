import os
from copy import deepcopy
m = list("""
              Quadrant Charlie
            F101              R25
    Z=========X=========E1-----------NJ
    ||  1      130Mi     | 1  60Mi  1 |
  F ||  4              R | 2        0 |  R
  1 XX  0              7 | 0        0 |  2
  0 ||  M              4 | M        M |  5            
  1 ||  i                | i   R25  i |      
    ||       R50         |   /--------ID
    MT-------------------ZC--  80Mi
     | 1    120Mi       /
  R  | 5             i /            |                  KEY                      |
  5  | 0            M / R           | Z: Zenith; E1: Echelon One                |
  0  | M           0 / 8            | NJ: Nova Junction; ID: Ionvale Depot      |
     | i         20 / 8             | ZC: Zeroton Creek; DM: Dustmarch          |
    DM--------------                | MT: Muckspur Terminal                     |
            R88                     | R: Route F: Freeway  [X]Mi: Distance (Mi) |
                                    | X Through Highway Indicates Closed        |
                                    | NOTE: Map Not to Scale. Distances Approx. | 
""")
d = []
z = ''
saved = []
possible_chars = ["=",'X',"|","-",'/',"M","R","F","Z","E","N","I","D","C","T","H","L",'1',"J"]
cl = 0
rvs = {"1":['freeway','F101','Zenith','Echelon One',0],'2':['route','R25','Echelon One','Nova Junction',0],'3':['route','R25','Nova Junction',"Ionvale Depot",0],"4":['route','R25','Zeroton Creek','Ionvale Depot',0],'5':['route','R74','Echelon One','Zeroton Creek',0],'6':['route','R50','Muckspur Terminal','Zeroton Creek',0],'7':['route','R50','Muckspur Terminal','Dustmarch',0],'8':['route','R88','Dustmarch','Zeroton Creek',0],'9':['freeway','F101','Zenith','Muckspur Terminal',0],"z":['town','Zenith',"","",0],"e1":['town','Echelon One',"","",0],'nj':['town','Nova Junction',"","",0],'id':['town','Ionvale Depot',"","",0],'zc':['town','Zeroton Creek',"","",0],'dm':['town','Dustmarch',"","",0],'mt':['town','Muckspur Terminal',"","",0]}
for i in m:
    if i not in possible_chars:
        d.append(i)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        nl = deepcopy(m)
        nl.insert(cl,"(")
        nl.insert(cl+2,")")
        for ch in nl:
            print(ch, end="")
        if saved == []:
            z = input()
            if z == 's':
                d.append(i)
                cl += 1
                continue
            else:
                saved = rvs[z.lower()]
                d.append(saved)
        else:
            print(saved)
            val = input('accept')
            if val == '':
                d.append(saved)
            elif val == 's':
                d.append(i)
                cl += 1
                continue
            else:
                z = val
                if not z in rvs:
                    d.append(["UNKNOWN ROUTE", z, "UNKNOWN", "UNKNOWN", 0])
                    continue
                saved = rvs[z.lower()]
                d.append(saved)
        rvs[z.lower()][4] += 1
        saved = rvs[z.lower()]
    cl += 1
open("mdm.txt", "w").write(str(d))