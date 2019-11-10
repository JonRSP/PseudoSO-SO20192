# -*- coding: utf-8 -*-
'''
Esta entidade armazena as estruturas para que o pseudo SO funcione
'''

from process import Process
from file import File
from primaryMemory import PrimaryMemory
from secondaryMemory import SecondaryMemory
from action import Action
from resource import Resources
from scheduler import Scheduler
import sys

class SOStructure:

    def __init__(self, file_location):
        self.processes = {} # algo no padrão {idProcesso:Processo,....}
        self.primaryMemory = PrimaryMemory(64, 960)
        self.actions = {} # algo no formato {idProcesso1: [ação1, ação2, ...],idProcesso2: [ação1, ação2, ...] ...}
        self.resources = Resources()
        self.globalTime = 0
        self.scheduler = Scheduler()
        self.readProcess(file_location)
        self.readConfiguration(file_location)

    def readProcess(self,file_location):
        processCounter = 0 # Contador do ID do processo
        try:
            file = open(file_location+"processes.txt", "r") # Tente abrir
            for line in file: # Para cada linha no arquivo
                elements = line.split(', ') # Divida na vírgula
                self.processes[processCounter] = Process(elements, processCounter) # Crie um novo processo no dicionário de processos
                # self.primaryMemory.addProcess(self.processes[processCounter], processCounter)
                processCounter += 1 # Aumenta o contador do ID
            file.close() # Tente fechar
        except:
            sys.exit("'processes.txt' file does not exist") # Se não existir saia


    def readConfiguration(self,file_location):
        lineCounter = 0
        flag = 0
        try:
            file = open(file_location+"files.txt", "r") # Tente abrir
        except:
            sys.exit("'files.txt' file does not exist") # Se não existir saia
        for line in file: # Para cada linha no arquivo
            if (lineCounter == 0):
                self.secondaryMemory = SecondaryMemory(int(line)) # Número de blocos de memória
            elif(lineCounter == 1):
                numberOfFiles = int(line) # Grava quantos arquivos serão inicializados
                flag = 1
            elif(flag == 1 and (lineCounter-2) < numberOfFiles):
                elements = line.split(', ') # Divida na vírgula
                newFile = File(elements)
                self.secondaryMemory.addFile(newFile, int(elements[1])) # Crie um novo arquivo na memória secundária
            else:
                elements = line.split(', ') # Divida na vírgula
                if(elements[0] in self.actions):
                    if (int(elements[-1]) - int(self.actions[elements[0]][-1].numberOfOperation)) > 1:
                        for i in range(int(self.actions[elements[0]][-1].numberOfOperation)+1, int(elements[-1])):
                            self.actions[elements[0]].append(Action([elements[0],2,'CPU',0,i])) # caso pule o numero da operacao, será da CPU
                        # self.actions[elements[0]].append(Action([elements]))
                    self.actions[elements[0]].append(Action(elements)) # Crie uma nova ação de um processo
                else:
                    self.actions[elements[0]] = [Action(elements)]
            lineCounter += 1
        file.close()



    def execAction(self, action, process, secondaryMemory):
        if (process.timeOfProcessing > 0): # se o processo ainda tem tempo de CPU
            if (action.operationCode == 0): # Se a action eh para Criar arquivo
                # cria
                added = secondaryMemory.addFile(File([action.fileName, action.numberOfBlocks]))
                if(added == 1):# erro nao tem espaço
                    print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - FALHA ')
                    print("Não há espaço para criar o arquivo "+action.fileName)
                elif(added == 2):# ja existe arquivo com mesmo noma
                    print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - FALHA ')
                    print("O arquivo "+ action.fileName + " já existe")
                else: #sucesso em criar arquivo
                    blocks = secondaryMemory.busyMemory[action.fileName]
                    print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - SUCESSO ')
                    if blocks[1] > 1:
                        print('O processo ' + str(process.id) + ' criou arquivo ' + action.fileName + ' (blocos '+str(blocks[0]) + ' a ' + str(blocks[0] + blocks[1]-1) + ').')
                    else:
                        print('O processo ' + str(process.id) + ' criou arquivo ' + action.fileName + ' (bloco ' + str(blocks[0]) + ').')
            elif (action.operationCode == 1): # Se a action eh para deletar arquivo
                # deleta
                deleted = secondaryMemory.removeFile(action.fileName)
                if(deleted == 1): # erro arquivo nao existe
                    print('O processo ' + str(process.id)  + ' não pode deletar o arquivo' + action.fileName + 'porque não existe esse arquivo.')
                else: # sucesso em deletar arquivo
                    print('O processo '+ str(process.id)+ ' deletou o arquivo '+ action.fileName +'.')
            else: # Se action eh da CPU (Dummy) Opcode = 2
                print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - SUCESSO CPU')
            process.timeOfProcessing -= 1
            action.finishedAction = 1
        else: # erro tempo de CPU do processo acabou
                print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - FALHA ')
                print("O processo "+ str(process.id) + ' esgotou seu tempo de CPU.')
                return 1

        return 0

    def run(self):
        flag = 0
        while (len(self.processes)>0): # Enquanto nao acabarem os processos
            for procID in self.processes: # percorre a lista de processos
                process = self.processes[procID]
                if (process.timeOfArrival <= self.globalTime):
                    added = self.primaryMemory.addProcess(process,process.id) # tenta adicionar processo na memoria
                    if (added == 0): #se conseguir adicionar na memoria
                        self.scheduler.queueProcess(process) # Adiciona processo na fila de pronto
                else:
                    break # break ou pass?
            if ((not self.scheduler.fifo_queue.is_empty()) or (not self.scheduler.priority_queue.is_empty())):
                if (flag == 0):
                    process = self.scheduler.scheduleProcess() # escalona processo mais prioritario
                    flag = 1
                while(not process.requestResources()): # checar ate encontrar um processo com recurso livre
                    self.scheduler.queueProcess(process) # processo volta pra fila
                    process = self.scheduler.scheduleProcess() # pega o proximo processo
                if (process.timeOfArrival <= self.globalTime):
                    self.execAction(self.actions[process.id][0], process, self.secondaryMemory) #executa acoes de um processo
                    self.actions[process.id].remove(self.actions[process.id][0])
                    self.globalTime += 1
                    if (len(self.actions[process.id]) == 0): # acabaram as acoes do processo
                        print('P'+ str(process.id) +' return SIGINT')
                        process.freeResources() # libera os recursos
                        addedProcessesAfterRemove = removeProcess(process,process.id) # remove da memoria principal
                        if (addedProcessesAfterRemove[0] == 0):
                            for processID in addedProcessesAfterRemove[1]:
                                self.scheduler.queueProcess(self.processes[processID])
                        del self.processes[process.id] # deleta o processo da lista de processos
                        flag = 0
                    else:
                        process = self.scheduler.preemptProcess(process,self.globalTime) # preempcao, caso tenha, haverá a troca de processo
            else:
                self.globalTime += 1
        return 0
