# -*- coding: utf-8 -*-
from sostructure import SOStructure


structure = SOStructure('')
print("Processos:")
for process in structure.processes:
    print ("id "+ str(process[0])+' dados '+str(process[1]))
print("secondary total size: "+str(structure.secondaryMemory.totalSize))
print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
print("Memória:")
for block in structure.secondaryMemory.memoryList:
    print(block)
print("Recursos disponíveis:")
print(str(structure.resources))
print("Ações a serem realizadas:")
for action in structure.actions:
    print(str(action))
