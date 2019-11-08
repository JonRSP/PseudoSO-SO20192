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
import sys

class SOStructure:

    def __init__(self, file_location):
        self.processes = {} # algo no padrão {idProcesso:Processo,....}
        self.primaryMemory = PrimaryMemory(64, 960)
        self.actions = {} # algo no formato {idProcesso: [ação1, ação2, ...], ...}
        self.resources = Resources()
        self.readProcess(file_location)
        self.readConfiguration(file_location)

    def readProcess(self,file_location):
        processCounter = 0 # Contador do ID do processo
        try:
            file = open(file_location+"processes.txt", "r") # Tente abrir
            for line in file: # Para cada linha no arquivo
                elements = line.split(', ') # Divida na vírgula
                self.processes[processCounter] = Process(elements, processCounter) # Crie um novo processo no dicionário de processos
                self.primaryMemory.addProcess(self.processes[processCounter], processCounter)
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
                    if (elements[-1] - self.actions[elements[0]][-1].numberOfOperation) > 1:
                        for i in range(self.actions[elements[0]][-1].numberOfOperation+1, elements[-1]):
                            self.action[elements[0]].append(Action([elements[0],2,'CPU',0,i])) # caso pule o numero da operacao, será da CPU
                        self.actions[elements[0]].append(Action([elements]))
                    self.actions[elements[0]].append(Action(elements)) # Crie uma nova ação de um processo
                else:
                    self.actions[elements[0]] = [Action(elements)]
            lineCounter += 1
        file.close()

    def execActions(self, actions, process, secondaryMemory):
        for action in actions:
            if (process.timeOfProcessing > 0):
                if (action.finishedAction == 0): # se a action ainda nao foi executada
                    if (action.operationCode == 0): # Criar arquivo
                        # cria
                        added = secondaryMemory.addFile(File([action.fileName, action.numberOfBlocks]))
                        if(added == 1):
                            print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - FALHA ')
                            print("Não há espaço para criar o arquivo "+action.fileName)
                        elif(added == 2):
                            print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - FALHA ')
                            print("O arquivo "+ action.fileName + " já existe")
                        else:
                            blocks = secondaryMemory.busyMemory[action.fileName]
                            print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - SUCESSO ')
                            if blocks[1] > 1:
                                print('O processo ' + str(process.id) + ' criou arquivo ' + action.fileName + ' (blocos '+str(blocks[0]) + ' a ' + str(blocks[0] + blocks[1]-1) + ').')
                            else:
                                print('O processo ' + str(process.id) + ' criou arquivo ' + action.fileName + ' (bloco ' + str(blocks[0]) + ').')
                    elif (action.operationCode == 1): # Deletar arquivo
                        # deleta
                        deleted = secondaryMemory.removeFile(action.fileName)
                        if(deleted == 1):
                            print('O processo ' + str(process.id)  + ' não pode deletar o arquivo' + action.fileName + 'porque não existe esse arquivo.')
                        else:
                            print('O processo '+ str(process.id)+ ' deletou o arquivo '+ action.fileName +'.')
                    else:
                        print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - SUCESSO CPU') # dummy action pro CPU (operationCode=2)
                    process.timeOfProcessing -= 1
                    action.finishedAction = 1
                    #if preemptProcess(process):
                    #    return 2
            else:
                print('P'+ str(process.id) +' instruction '+ str(action.numberOfOperation) +' - FALHA ')
                print("O processo "+ str(process.id) + ' esgotou seu tempo de CPU.')
                return 1
        print('P'+ str(process.id) +' return SIGINT')
        return 0
