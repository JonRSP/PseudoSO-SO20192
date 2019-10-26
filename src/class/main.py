# -*- coding: utf-8 -*-
from sostructure import SOStructure
from file import File


structure = SOStructure('')
print("Processos:")
for process in structure.processes:
    print ("id "+ str(process[0])+' dados '+str(process[1]))
print("secondary total size: "+str(structure.secondaryMemory.totalSize))
print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
print("Memória:")
print( structure.secondaryMemory.freeMemory)
print(structure.secondaryMemory.busyMemory)
print("Recursos disponíveis:")
print(str(structure.resources))
print("Ações a serem realizadas:")
for action in structure.actions:
    print(str(action))

structure.secondaryMemory.addFile(File(['A', 2]), -1)
print( structure.secondaryMemory.freeMemory)
print(structure.secondaryMemory.busyMemory)
print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
structure.secondaryMemory.addFile(File(['A', 2]), -1)

structure.secondaryMemory.removeFile('Y')
print( structure.secondaryMemory.freeMemory)
print(structure.secondaryMemory.busyMemory)
print("secondary size now: "+str(structure.secondaryMemory.sizeNow))

structure.secondaryMemory.removeFile('X')
print( structure.secondaryMemory.freeMemory)
print(structure.secondaryMemory.busyMemory)
print("secondary size now: "+str(structure.secondaryMemory.sizeNow))

structure.secondaryMemory.addFile(File(['B', 3]), -1)
print( structure.secondaryMemory.freeMemory)
print(structure.secondaryMemory.busyMemory)
print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
