# -*- coding: utf-8 -*-
from .process import Process
from .file import File
from .primaryMemory import PrimaryMemory
from .secondaryMemory import SecondaryMemory
from .action import Action
import sys

class SO:
    self.processes = []
    self.primaryMemory = PrimaryMemory(64, 960)
    self.secondaryMemory = 0
    self.actions = []


    def __init__(self, file_location):
        self.readProcess(file_location)
        self.readConfiguration(file_location)

    def readProcess(file_location):
        processCounter = 0 # Contador do ID do processo
        try:
            file = open(file_location+"processes.txt", "r") # Tente abrir
            for line in file: # Para cada linha no arquivo
                elements = line.split(', ') # Divida na vírgula
                self.processes.append([processCounter, Process(elements)]) # Crie um novo processo na lista de processos
                processCounter += 1 # Aumenta o contador do ID
            file.close() # Tente fechar
        except:
            sys.exit("'processes.txt' file does not exist") # Se não existir saia

    def readConfiguration(file_location):
        lineCounter = 0
        flag = 0
        try:
            file = open(file_location+"files.txt", "r") # Tente abrir
            for line in file: # Para cada linha no arquivo
                if (lineCounter == 0):
                    self.secondaryMemory = SecondaryMemory(int(line)) # Número de blocos de memória
                elif(lineCounter == 1):
                    numberOfFiles = int(line) # Grava quantos arquivos serão inicializados
                    flag = 1
                elif(flag == 1 and (lineCounter-2) < numberOfFiles):
                    elements = line.split(', ') # Divida na vírgula
                    self.secondaryMemory.addFile(File(elements)) # Crie um novo arquivo na memória secundária
                else:
                    elements = line.split(', ') # Divida na vírgula
                    self.actions.append(Action(elements)) # Crie uma nova ação de um processo
                lineCounter += 1
        except:
            sys.exit("'files.txt' file does not exist") # Se não existir saia
