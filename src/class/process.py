# -*- coding: utf-8 -*-
'''
O processo é uma entidade que realiza ações, pode ser do tipo tempo real ou de usuário.

Quando a professora liberar a especificação completa eu complemento isso aqui
'''
class Process:
    self.timeOfArrival = 0
    self.type = 0
    self.priority = 0
    self.size = 0
    self.requestResource1 = 0 # Mudar para o nome do recurso quando a prof liberar a especificação
    self.requestResource2 = 0
    self.requestResource3 = 0
    self.requestResource4 = 0

    def __init__(self, elements):
        self.timeOfArrival = elements[0]
        self.type = elements[1]
        self.priority = elements[2]
        self.size = elements[3]
        self.requestResource1 = elements[4]
        self.requestResource2 = elements[5]
        self.requestResource3 = elements[6]
        self.requestResource4 = elements[7]

    def __int__(self):
        return self.size
