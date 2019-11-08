# -*- coding: utf-8 -*-
'''
O escalonador
'''

from queue import FifoQueue, PriorityQueue

class Scheduler(self):
    def __init__(self):
        self.fifo_queue = FifoQueue()
        self.priority_queue = PriorityQueue()
        self.time = 0

    def queueProcess(self, process):
        if (process.priority == 0):
            self.fifo_queue.push(process)
        else:
            self.priority_queue.push(process)


    def scheduleProcess(self, process, primaryMemory):
        # self.primaryMemory.addProcess(process, process.id)
        if (process.priority == 0):
            proc = self.fifo_queue.pop()
            execCPU(proc)
        else:
            pass
    
    def preemptProcess(self, process):

    # def __int__(self):
    #     return self.size

    # def __str__(self):
    #     return str(self.timeOfArrival)+', '+str(self.priority)+', '+str(self.timeOfProcessing)+', '+str(self.size)+', '+str(self.requestPrinter)+', '+str(self.requestScanner)+', '+str(self.requestModem)+', '+str(self.requestDisk)

    # def __eq__(self, other):
    #     if isinstance(other, Process):
    #         return self.timeOfArrival == other.timeOfArrival and self.priority == other.priority and self.timeOfProcessing == other.timeOfProcessing and self.size == other.size and self.requestPrinter == other.requestPrinter and self.requestScanner == other.requestScanner and self.requestModem == other.requestModem and self.requestDisk == other.requestDisk
