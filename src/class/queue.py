# -*- coding: utf-8 -*-
'''
Teremos 4 filas para processos

Para processos de tempo real, teremos uma única fila, a qual será regida pela política FIFO. Esta fila tem maior 
prioridade que as filas de processos de usuário

Para procesos de usuário, teremos 3 filas com múltiplas prioridades e com realimentação.
'''

from collections import deque
import heapq # This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm

class FifoQueue(deque):
    def __init__(self):
		self.fifo_queue = []

    def push(self,process):
        self.fifo_queue.append(process)
    
    def pop(self):
        return self.fifo_queue.popleft()

    def is_empty(self,process):
        return len(self.fifo_queue) == 0

class PriorityQueue(deque):
    def __init__(self):
		self.first_queue = []
        self.second_queue = []
        self.third_queue = []

	def push(self,process):
        if (process.priority==1):
            self.first_queue.append(process)
        elif (process.priority==2):
            self.second_queue.append(process)
        else:
            self.third_queue.append(process)

	def pop(self, process):
        if (process.priority==1):
            return self.first_queue.popleft()
        elif (process.priority==2):
            return self.second_queue.popleft()
        else:
                return self.third_queue.popleft()

    def is_empty(self,queue):
        if (queue==1):
            return len(self.first_queue)  == 0
        elif (queue==2)::
            return len(self.second_queue) == 0
        else:
            return len(self.third_queue)  == 0
