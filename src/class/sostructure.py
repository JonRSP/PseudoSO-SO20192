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
                self.processes[processCounter] = Process(elements) # Crie um novo processo no dicionário de processos
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
                    self.actions[elements[0]].append(Action(elements)) # Crie uma nova ação de um processo
                else:
                    self.actions[elements[0]] = [Action(elements)]
            lineCounter += 1
        file.close()
