# -*- coding: utf-8 -*-
'''
Esta classe representa a memória secundária, I.E. disco.
O tamanho é "alocado" em sua criação, durante a leitura do segundo arquivo
'''
class SecondaryMemory:
    self.totalSize = 0
    self.sizeNow = 0
    self.memorylist = [] #acho melhor usar dicionário aqui, vou tentar pensar melhor nisso

    def __init__(self, size):
        self.totalSize = size
        self.sizeNow = size
        for i in range(): # lembrar como faz range
            self.memorylist((None, 'free')) # preenche a lista de memória secundária, com tuplas (vazio, livre), vazio vai armazenar qual arquivo

    def addFile(self, file):
        if(self.sizeNow < int(file)): # O espaço total disponível não armazena o arquivo
            print("Não há espaço para criar o arquivo "+str(file))
        else:
            self.fileFit(file) # Verificar se nos espaços disponíveis há espaço contíguo para armazenar o arquivo

    def fileFit(self,file):
        pass
