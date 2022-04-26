# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:20:33 2021

@author: HP
"""

def propagar(v):
    for i in range(0, len(v)):
        if i==0:                             #Considero el extremo izquierdo
            if v[i]==1 and v[i+1]==0:
                v[i+1]=1
            else:
                v[i]=v[i]
        elif i==(len(v)-1) and v[i]!=1:                 #Considero el extremo derecho
            break
        else:
            if v[i]==1:
                for j in range(i, len(v)):     #Propago hacia la derecha hasta encontrar un -1
                    if v[j]==-1:
                        break
                    else:
                        v[j]=1
                for j in range(0,i+1):         #Propago hacia la izquierda hasta encontrar un -1
                    if v[i-j]==-1:
                        break
                    else:
                        v[i-j]=1
                    
    return v
    
print(propagar([1] + [ 0 for _ in range(1000) ]))  

#Al ejecutar:   [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
        
            
        
            
            
            
    



            
        
            
            