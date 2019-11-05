# -*- coding: utf-8 -*-
'''
O processo é uma entidade que realiza ações, pode ser do tipo tempo real ou de usuário.

Cada processo, portanto, cada linha, deve conter os seguintes dados:
<tempo de inicialização>, <prioridade>, <tempo de processador>, <blocos em memória>,
<númerocódigo da impressora requisitada>, <requisição do scanner>, <requisição do modem>, <númerocódigo do disco>
'''
class Process:
    def __init__(self, elements):
        self.timeOfArrival = elements[0]
        self.priority = elements[1]
        self.timeOfProcessing = elements[2]
        self.size = elements[3]
        self.requestPrinter = elements[4]
        self.requestScanner = elements[5]
        self.requestModem = elements[6]
        self.requestDisk = elements[7]

    def __int__(self):
        return self.size

    def __str__(self):
        return str(self.timeOfArrival)+', '+str(self.priority)+', '+str(self.timeOfProcessing)+', '+str(self.size)+', '+str(self.requestPrinter)+', '+str(self.requestScanner)+', '+str(self.requestModem)+', '+str(self.requestDisk)

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.timeOfArrival == other.timeOfArrival and self.priority == other.priority and self.timeOfProcessing == other.timeOfProcessing and self.size == other.size and self.requestPrinter == other.requestPrinter and self.requestScanner == other.requestScanner and self.requestModem == other.requestModem and self.requestDisk == other.requestDisk
