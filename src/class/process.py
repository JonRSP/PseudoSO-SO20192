# -*- coding: utf-8 -*-
'''
O processo é uma entidade que realiza ações, pode ser do tipo tempo real ou de usuário.

Cada processo, portanto, cada linha, deve conter os seguintes dados:
<tempo de inicialização>, <prioridade>, <tempo de processador>, <blocos em memória>,
<númerocódigo da impressora requisitada>, <requisição do scanner>, <requisição do modem>, <númerocódigo do disco>
'''
class Process:
    '''
    self.timeOfArrival = 0
    self.priority = 0
    self.timeOfProcessing = 0
    self.size = 0
    self.requestPrinter = 0 # 0 (nao solicitou), 1 (solicitou impress 1) ou 2 (solicitou impress 2)
    self.requestScanner = 0 # 0 (nao solicitou) ou 1 (solicitou)
    self.requestModem = 0   # 0 (nao solicitou) ou 1 (solicitou)
    self.requestDisk = 0    # 0 (nao solicitou), 1 (solicitou disco 1) ou 2 (solicitou disco 2)
'''
    def __init__(self, elements):
        self.timeOfArrival = elements[0]
        self.priority = elements[2]
        self.timeOfProcessing = elements[1]
        self.size = elements[3]
        self.requestPrinter = elements[4]
        self.requestScanner = elements[5]
        self.requestModem = elements[6]
        self.requestDisk = elements[7]

    def __int__(self):
        return self.size

    def __str__(self):
        return str(self.timeOfArrival)+', '+str(self.priority)+', '+str(self.timeOfProcessing)+', '+str(self.size)+', '+str(self.requestPrinter)+', '+str(self.requestScanner)+', '+str(self.requestModem)+', '+str(self.requestDisk)
