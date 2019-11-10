# -*- coding: utf-8 -*-
'''
O escalonador
'''

from queue import FifoQueue, PriorityQueue

class Scheduler:
    def __init__(self):
        self.fifo_queue = FifoQueue()
        self.priority_queue = PriorityQueue()

    #  coloca um processo memoria principal
    def insertProcessInMemory(self, process):
        self.primaryMemory.addProcess(process, process.id) # coloca o processo de tempo real na memoria
        return 0

    # enfileira processo se a fila nao estiver lotada (1000)
    def queueProcess(self, process):
        if (process.priority == 0):
            result = self.fifo_queue.push(process)
        else:
            result = self.priority_queue.push(process)
        return result


    # escalona o processo com maior prioridade para a CPU
    def scheduleProcess(self):
        if (not fifo_queue.is_empty):
            process = fifo_queue.pop()
        elif (not priority_queue.is_empty):
            process = priority_queue.pop()
        return process


    def preemptProcess(self, process, globalTime):
        if ((process.priority > 0) and (not self.fifo_queue.is_empty()) and (globalTime >= self.fifo_queue.pick().timeOfArrival)): #se chegou um processo de tempo real
            if (process.priority > 1): # se o processo puder ser preemptado, ou seja, é de usuário
                process.priority -= 1 # aumenta a prioridade
                self.priority_queue.push(process) # volta pra fila com sua respectiva prioridade
                process = self.fifo_queue.pop() # pega o processo de tempo real prioritario
        return process
    # def __int__(self):
    #     return self.size

    # def __str__(self):
    #     return str(self.timeOfArrival)+', '+str(self.priority)+', '+str(self.timeOfProcessing)+', '+str(self.size)+', '+str(self.requestPrinter)+', '+str(self.requestScanner)+', '+str(self.requestModem)+', '+str(self.requestDisk)

    # def __eq__(self, other):
    #     if isinstance(other, Process):
    #         return self.timeOfArrival == other.timeOfArrival and self.priority == other.priority and self.timeOfProcessing == other.timeOfProcessing and self.size == other.size and self.requestPrinter == other.requestPrinter and self.requestScanner == other.requestScanner and self.requestModem == other.requestModem and self.requestDisk == other.requestDisk
