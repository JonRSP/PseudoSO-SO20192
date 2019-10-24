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
        self.userSize = userSize
