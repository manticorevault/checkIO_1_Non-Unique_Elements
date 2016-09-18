# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:45:43 2016

@author: Artur
"""


def noiseCounter(data):

    listaIn = data
    for i in listaIn[0:len(listaIn)]:
            occ = listaIn.count(i)
            if occ == 1:
                listaIn.remove(i)
                
    return data

x = noiseCounter([1, 2, 3, 1, 3])
print(x)
