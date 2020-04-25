# -*- coding: utf-8 -*-
"""Converting matrix to simetric matrix considering max value between mtx[i][j] and mtx[j][i]

@author: catia(souz.kti@gmail.com)
"""

import pandas as pd

def main(filename):
    dados = pd.read_csv(filename, header=0)
#    dados = dados.drop('ID' , axis='columns')
    dados.index = dados.columns
    
    for i in range(len(dados.columns)): 
      for j in range(len(dados.columns)):
        if(dados.iloc[i,j]>dados.iloc[j,i]):
          dados.iloc[j,i] = dados.iloc[i,j]
        elif (dados.iloc[j,i]>dados.iloc[i,j]):
          dados.iloc[i,j] = dados.iloc[j,i]
    
    dados.to_csv('simetric.csv')
    
if __name__ == '__main__':
    main('input.csv')
        