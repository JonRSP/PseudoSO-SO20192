# -*- coding: utf-8 -*-
'''
Esta entidade simula a memória primária.
Ao inicializar é configurado o tamanho da memória reservada para processos em tempo real e processos de usuário;
o espaço total é dado pela soma dos dois elementos;
este espaço foi determinado na especificação.
'''
class PrimaryMemory:
    def __init__(self, realTimeSize, userSize):
        self.realTimeSize = realTimeSize
        self.realTimeSizeNow = realTimeSize
        self.userSize = userSize
        self.userSizeNow = userSize
        self.freeRealTimeMemory = {0:realTimeSize}
        self.busyRealTimeMemory = {}
        self.freeUserMemory = {0:userSize}
        self.busyUserMemory = {}
        self.notAllocatedProcess = []

    def addProcess(self, process, processID):
        if(process.priority == 0):
            freeMemory = self.freeRealTimeMemory
            sizeNow = self.realTimeSizeNow
            size = self.realTimeSize
            busyMemory = self.busyRealTimeMemory
        else:
            freeMemory = self.freeUserMemory
            sizeNow = self.userSizeNow
            size = self.userSize
            busyMemory = self.busyUserMemory
        if(size < int(process)): # O espaço total disponível não armazena o processo
            print("Tamanho total da memória é insuficiente para o processo")
            return 2
        if(sizeNow < int(process)): # O espaço livre disponível não armazena o processo
            print("Não há espaço para criar o processo " + str(processID) + ". Será tentado novamente mais tarde")
            if( (processID,process) not in self.notAllocatedProcess):
                self.notAllocatedProcess.append((processID, process))
            return 1
        else:
            position = self.processFit(process) # Verificar se nos espaços disponíveis há espaço contíguo para armazenar o processo
            if(position >= 0):
                if((freeMemory[position] - int(process)) > 0): # Se sobra espaço
                    freeMemory[position + int(process)] = freeMemory[position] - int(process) # Cria nova entrada no dicionário
                del freeMemory[position] # Remove entrada anterior
                busyMemory[processID] = (position, int(process))
                sizeNow -= int(process)
                if(process.priority == 0):
                    self.freeRealTimeMemory = freeMemory
                    self.realTimeSizeNow = sizeNow
                    self.busyRealTimeMemory = busyMemory
                else:
                    self.freeUserMemory = freeMemory
                    self.userSizeNow = sizeNow
                    self.busyUserMemory = busyMemory
                return 0
            else: # não há posição inicial que caiba o processo
                print("Não há espaço para criar o processo "+str(processID) + ". Será tentado novamente mais tarde")
                if( (processID,process) not in self.notAllocatedProcess):
                    self.notAllocatedProcess.append((processID, process))
                return 1

    def processFit(self, process): # Retorna a posição em que o arquivo cabe, -1 caso não caiba
        if(process.priority == 0):
            freeMemory = self.freeRealTimeMemory
        else:
            freeMemory = self.freeUserMemory
        for item in sorted(freeMemory.keys()):
            if(int(process) <= (freeMemory[item])):
                return item # posição em que cabe + lugar que sofrerá alteração
        return -1

    def removeProcess(self, process, processID):
        if(process.priority == 0):
            freeMemory = self.freeRealTimeMemory
            sizeNow = self.realTimeSizeNow
            busyMemory = self.busyRealTimeMemory
        else:
            freeMemory = self.freeUserMemory
            sizeNow = self.userSizeNow
            busyMemory = self.busyUserMemory
        data = busyMemory[processID] #armazena os dados do bloco em memória e tamanho
        sizeNow += data[1] # aumenta o tamanho atual
        if((data[0] + data[1]) in freeMemory): # se a liberação alcança um novo bloco livre
            extra = freeMemory[(data[0] + data[1])]
            del freeMemory[(data[0] + data[1])] # apagar o bloco de memória livre
            data = (data[0], data[1] + extra) # somar o tamanho do arquivo deletado com o espaço do outro bloco de memória livre
        if(data[0] > 0): # se não é o bloco inicial
            flag = 0
            for item in sorted(freeMemory.keys(), reverse=True):
                if(item < data[0]):
                    index = item # acha qual é o bloco anterior
                    flag = 1
                    break
            if flag == 0:
                index = data[0]
                freeMemory[index] = 0
        else:
            index = data[0] # é o bloco inicial
            freeMemory[index] = 0 # cria o bloco inicial
        freeMemory[index] += data[1] # soma com o número de blocos liberados
        del busyMemory[processID] # remove da lista de memória ocupada
        if(process.priority == 0):
            self.freeRealTimeMemory = freeMemory
            self.realTimeSizeNow = sizeNow
            self.busyRealTimeMemory = busyMemory
        else:
            self.freeUserMemory = freeMemory
            self.userSizeNow = sizeNow
            self.busyUserMemory = busyMemory
        if (len(self.notAllocatedProcess) > 0):
            self.retryAllocation()

    def retryAllocation(self):
        for item in self.notAllocatedProcess:
            flag = self.addProcess(item[1], item[0])
            if flag == 0: # sucesso ao tentar a alocação novamente
                self.notAllocatedProcess.remove(item)
