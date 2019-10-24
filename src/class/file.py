# -*- coding: utf-8 -*-
'''
Esta entidade representa os arquivos criados durante a execução do pseudo SO
'''
class File:
    '''
    self.name = 0 # Nome representado por uma letra
    self.size = 0 # Tamanho do arquivo
'''
    def __init__(self, elements):
        self.name = elements[0]
        self.size = int(elements[2])

    def __str__(self): # Para utilizar a instrução str(x)
        return self.name

    def __int__(self): # Para utilizar a instrução int(x)
        return self.size
