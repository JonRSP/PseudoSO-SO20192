# -*- coding: utf-8 -*-
from resource import Resources
'''
O processo é uma entidade que realiza ações, pode ser do tipo tempo real ou de usuário.

Cada processo, portanto, cada linha, deve conter os seguintes dados:
<tempo de inicialização>, <prioridade>, <tempo de processador>, <blocos em memória>,
<númerocódigo da impressora requisitada>, <requisição do scanner>, <requisição do modem>, <númerocódigo do disco>
'''
class Process:
    def __init__(self, elements, processID = 0):
        self.id = int(processID)
        self.timeOfArrival = int(elements[0])
        self.priority = int(elements[1])
        self.timeOfProcessing = int(elements[2])
        self.timeOfProcessingAux = self.timeOfProcessing
        self.size = int(elements[3])
        self.requestPrinter = int(elements[4])
        self.requestScanner = int(elements[5])
        self.requestModem = int(elements[6])
        self.requestDisk = int(elements[7])
        self.inMemory = 0
        self.tried = 0

    def requestResources(self, resources):
        auxlist = [self.requestPrinter, self.requestScanner, self.requestModem, self.requestDisk]
        return resources.requestResources(auxlist, self.id)

    def freeResources(self, resources):
        return resources.freeResources(self.id)

    def __int__(self):
        return self.size

    def __str__(self):
        return str(self.timeOfArrival)+', '+str(self.priority)+', '+str(self.timeOfProcessing)+', '+str(self.size)+', '+str(self.requestPrinter)+', '+str(self.requestScanner)+', '+str(self.requestModem)+', '+str(self.requestDisk)

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.timeOfArrival == other.timeOfArrival and self.priority == other.priority and self.timeOfProcessing == other.timeOfProcessing and self.size == other.size and self.requestPrinter == other.requestPrinter and self.requestScanner == other.requestScanner and self.requestModem == other.requestModem and self.requestDisk == other.requestDisk
