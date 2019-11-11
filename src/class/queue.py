# -*- coding: utf-8 -*-
'''
Teremos 4 filas para processos

Para processos de tempo real, teremos uma única fila, a qual será regida pela política FIFO. Esta fila tem maior
prioridade que as filas de processos de usuário

Para procesos de usuário, teremos 3 filas com múltiplas prioridades.
'''

from collections import deque

class FifoQueue(deque):
    def __init__(self):
        self.fifo_queue = deque()

    def push(self,process):
        if(len(self.fifo_queue) < 1000):
            self.fifo_queue.append(process)
            return 0
        else:
            return 1

    def pop(self):
        try:
            return self.fifo_queue.popleft()
        except:
            return None

    def is_empty(self):
        return len(self.fifo_queue) == 0

    def pick(self):
        return self.fifo_queue[0]

class PriorityQueue(deque):
    def __init__(self):
        self.first_queue = deque()
        self.second_queue = deque()
        self.third_queue = deque()

    def push(self,process):
        if (process.priority==1):
            if(len(self.first_queue)<1000):
                self.first_queue.append(process)
                return 0
            else:
                return 1
        elif (process.priority==2):
            if(len(self.second_queue)<1000):
                self.second_queue.append(process)
                return 0
            else:
                return 1
        else:
            if(len(self.third_queue)<1000):
                self.third_queue.append(process)
                return 0
            else:
                return 1

    def pop(self):
        if(len(self.first_queue) > 0):
            try:
                return self.first_queue.popleft()
            except:
                return None
        elif(len(self.second_queue) > 0):
            try:
                return self.second_queue.popleft()
            except:
                return None
        else:
            try:
                return self.third_queue.popleft()
            except:
                return None

    def is_empty(self):
        return ((len(self.first_queue)  == 0) and (len(self.second_queue)  == 0) and (len(self.third_queue)  == 0))

    def pick(self):
        if (len(self.first_queue) > 0):
            return self.first_queue[0]
        elif (len(self.second_queue) > 0):
            return self.second_queue[0]
        else:
            return self.third_queue[0]
