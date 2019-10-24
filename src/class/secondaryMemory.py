# -*- coding: utf-8 -*-
'''
Esta classe representa a memória secundária, I.E. disco.
O tamanho é "alocado" em sua criação, durante a leitura do segundo arquivo
'''
class SecondaryMemory:
    def __init__(self, size):
        self.totalSize = int(size)
        self.sizeNow = int(size)
        self.memoryList = []
        for i in range(0, size):
            self.memoryList.append((None, 'free')) # preenche a lista de memória secundária, com tuplas (vazio, livre), vazio vai armazenar qual arquivo

    def addFile(self, file, initialConfig): # initialConfig >= 0 implica que é configuração inicial e corresponde à posição inicial do SO
        if(self.sizeNow < int(file)): # O espaço total disponível não armazena o arquivo
            print("Não há espaço para criar o arquivo "+str(file))
        else:
            position = self.fileFit(file, initialConfig) # Verificar se nos espaços disponíveis há espaço contíguo para armazenar o arquivo
            if(position >= 0):
                for i in range(position, position+int(file)):
                    self.memoryList[i] = (str(file), 'busy')
                self.sizeNow -= int(file)
            else: # não há posição inicial que caiba o arquivo
                print("Não há espaço para criar o arquivo "+str(file))

    def fileFit(self, file, initialConfig): # Retorna a posição em que o arquivo cabe, -1 caso não caiba
        if(initialConfig >= 0):
            for i in range(initialConfig, initialConfig+int(file)):
                if self.memoryList[i][1] is not 'free':
                    return -1
            return initialConfig
        else:
            pass # pensar em uma forma eficiente de verificar a memória pra ver se cabe (mapa de bits?)
