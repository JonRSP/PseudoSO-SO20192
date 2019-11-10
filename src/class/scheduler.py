# -*- coding: utf-8 -*-
'''
O escalonador
'''

from queue import FifoQueue, PriorityQueue

class Scheduler:
    def __init__(self):
        self.fifo_queue = FifoQueue()
        self.priority_queue = PriorityQueue()

    # enfileira processo se a fila nao estiver lotada (1000)
    def queueProcess(self, process):
        if (process.priority == 0):
            result = self.fifo_queue.push(process)
        else:
            result = self.priority_queue.push(process)
        return result


    # escalona o processo com maior prioridade para a CPU
    def scheduleProcess(self):
        if (not self.fifo_queue.is_empty()):
            process = self.fifo_queue.pop()
        else:
            process = self.priority_queue.pop()
        return process


    def preemptProcess(self, process, globalTime):
        if ((process.priority > 0) and (not self.fifo_queue.is_empty()) and (globalTime >= self.fifo_queue.pick().timeOfArrival)): #se chegou um processo de tempo real
            if (process.priority > 1): # se o processo puder ser preemptado, ou seja, é de usuário
                process.priority -= 1 # aumenta a prioridade
                self.priority_queue.push(process) # volta pra fila com sua respectiva prioridade
                process = self.fifo_queue.pop() # pega o processo de tempo real prioritario
        return process
