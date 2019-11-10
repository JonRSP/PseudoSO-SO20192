# -*- coding: utf-8 -*-
from sostructure import SOStructure
from file import File


structure = SOStructure('')
structure.run()
# print("Processos:")
# for process in structure.processes:
#     print ("id "+ str(process)+' dados '+str(structure.processes[process]))
# print("secondary total size: "+str(structure.secondaryMemory.totalSize))
# print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
# print("Memória secundária:")
# print( structure.secondaryMemory.freeMemory)
# print(structure.secondaryMemory.busyMemory)
# print("Recursos disponíveis:")
# print(str(structure.resources))
# print("Ações a serem realizadas:")
# for actionlist in structure.actions:
#     for action in structure.actions[actionlist]:
#         print(str(action))

# structure.secondaryMemory.addFile(File(['A', 2]))
# print( structure.secondaryMemory.freeMemory)
# print(structure.secondaryMemory.busyMemory)
# print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
# structure.secondaryMemory.addFile(File(['A', 2]))
#
# structure.secondaryMemory.removeFile('Y')
# print( structure.secondaryMemory.freeMemory)
# print(structure.secondaryMemory.busyMemory)
# print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
#
# structure.secondaryMemory.removeFile('X')
# print( structure.secondaryMemory.freeMemory)
# print(structure.secondaryMemory.busyMemory)
# print("secondary size now: "+str(structure.secondaryMemory.sizeNow))
#
# structure.secondaryMemory.addFile(File(['B', 3]))
# print( structure.secondaryMemory.freeMemory)
# print(structure.secondaryMemory.busyMemory)
# print("secondary size now: "+str(structure.secondaryMemory.sizeNow))

# structure.run()
