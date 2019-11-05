# -*- coding: utf-8 -*-
'''
Esta classe representa a memória secundária, I.E. disco.
O tamanho é "alocado" em sua criação, durante a leitura do segundo arquivo
'''
class SecondaryMemory:
    def __init__(self, size):
        self.totalSize = int(size)
        self.sizeNow = int(size)
        self.freeMemory = {0:size} # algo no formato {posição:tamanhoLivre, ....}
        self.busyMemory = {} # algo no formato {"nomeArquivo":(posição, tamanho), ....}

    def addFile(self, file, initialConfig = -1): # initialConfig >= 0 implica que é configuração inicial e corresponde à posição inicial do SO
        if(str(file) in self.busyMemory):
            print("O arquivo "+str(file) + " já existe")
            return 2
        if(self.sizeNow < int(file)): # O espaço disponível não armazena o arquivo
            print("Não há espaço para criar o arquivo "+str(file))
            return 1
        else:
            position = self.fileFit(file, initialConfig) # Verificar se nos espaços disponíveis há espaço contíguo para armazenar o arquivo
            if(position[0] >= 0):
                if(position[0] == position[1]):
                    if((self.freeMemory[position[1]] - (position[0] - position[1]) - int(file)) > 0): # Se sobra espaço
                        self.freeMemory[position[0] + int(file)] = self.freeMemory[position[0]] - int(file) # Cria nova entrada no dicionário
                    del self.freeMemory[position[1]] # Remove entrada anterior
                else: # apenas se é na configuração inicial e no meio de um grupo de blocos livres
                    if((self.freeMemory[position[1]] - (position[0] - position[1]) - int(file) ) > 0): # Se sobra espaço
                        self.freeMemory[position[0] + int(file)] = self.freeMemory[position[1]] - ((position[0] - position[1]) + int(file)) # Cria nova entrada no dicionário
                    self.freeMemory[position[1]] = position[0] - position[1]# Redefine o tamanho livre daquela entrada
                self.busyMemory[str(file)] = (position[0], int(file))
                self.sizeNow -= int(file)
                return 0
            else: # não há posição inicial que caiba o arquivo
                print("Não há espaço para criar o arquivo "+str(file))
                return 1

    def fileFit(self, file, initialConfig): # Retorna a posição em que o arquivo cabe, -1 caso não caiba
        if(initialConfig >= 0):
            for item in sorted(self.freeMemory.keys()):
                if(item <= initialConfig and int(file) <= (self.freeMemory[item]-initialConfig)):
                    return (initialConfig, item) # posição em que cabe + lugar que sofrerá alteração
            return (-1,-1)
        else:
            for item in sorted(self.freeMemory.keys()):
                if(int(file) <= (self.freeMemory[item])):
                    return (item, item) # posição em que cabe + lugar que sofrerá alteração
            return (-1,-1)

    def removeFile(self, fileToRemove):
        data = self.busyMemory[fileToRemove] #armazena os dados do bloco em memória e tamanho
        self.sizeNow += data[1] # aumenta o tamanho atual
        if((data[0] + data[1]) in self.freeMemory): # se a liberação alcança um novo bloco livre
            extra = self.freeMemory[(data[0] + data[1])]
            del self.freeMemory[(data[0] + data[1])] # apagar o bloco de memória livre
            data = (data[0], data[1] + extra) # somar o tamanho do arquivo deletado com o espaço do outro bloco de memória livre
        if(data[0] > 0): # se não é o bloco inicial
            flag = 0
            for item in sorted(self.freeMemory.keys(), reverse=True):
                if(item < data[0]):
                    index = item # acha qual é o bloco anterior
                    flag = 1
                    break
            if flag == 0:
                index = data[0]
                self.freeMemory[index] = 0
        else:
            index = data[0] # é o bloco inicial
            self.freeMemory[index] = 0 # cria o bloco inicial
        self.freeMemory[index] += data[1] # soma com o número de blocos liberados
        del self.busyMemory[fileToRemove] # remove da lista de memória ocupada
