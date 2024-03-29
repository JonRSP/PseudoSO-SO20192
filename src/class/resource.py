# -*- coding: utf-8 -*-
'''
Esta entidade representa os recursos que podem ser utilizados
'''

class Resources():

    def __init__(self):
        self.auxDic = {0:'printer', 1:'scanner', 2:"modem", 3:'disk'}
        self.processesWithResources = []
        self.busyResource = {'printer':[], 'scanner':[], 'modem':[], 'disk':[]}
        self.availableResource = {} # algo nesse formato {'recurso':quantidade}
        self.listOfResourcesToCreate = ['printer', 'printer', 'scanner', 'modem', 'disk', 'disk']
        for item in self.listOfResourcesToCreate:
            if item in self.availableResource:
                self.availableResource[item] += 1
            else:
                self.availableResource[item] = 1

    def requestResources(self, resourcesToAllocate, processID):
        if processID in self.processesWithResources:
            return True
        else:
            for resource in range(0,4):
                if self.availableResource[self.auxDic[resource]] > 0 and resourcesToAllocate[resource] == 1:
                    self.busyResource[self.auxDic[resource]].append(processID)
                    self.availableResource[self.auxDic[resource]] -= 1
                elif self.availableResource[self.auxDic[resource]] == 0:
                    # desalocar os alocados e colocar na fila de espera
                    for failed in range(0, resource):
                        if resourcesToAllocate[failed] == 1:
                            self.busyResource[self.auxDic[failed]].remove(processID)
                            self.availableResource[self.auxDic[failed]] += 1
                    return False
            self.processesWithResources.append(processID)
            return True

    def freeResources(self,processID):
        for resource in self.busyResource:
            try:
                self.busyResource[resource].remove(processID)
                self.availableResource[resource] += 1
                self.processesWithResources.remove(processID)
            except:
                pass

    def __str__(self):
        returnString = ''
        for item in self.availableResource:
            returnString += item+' '+str(self.availableResource[item])+'\n'
        return returnString
