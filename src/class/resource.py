# -*- coding: utf-8 -*-
'''
Esta entidade representa os recursos que podem ser utilizados
'''

class Resources():

    def __init__(self):
        self.availableResourceDic = {}
        self.listOfResourcesToCreate = ['printer', 'printer', 'scanner', 'modem', 'disk', 'disk']
        for item in self.listOfResourcesToCreate:
            if item in self.availableResourceDic:
                self.availableResourceDic[item] += 1
            else:
                self.availableResourceDic[item] = 1

    def __str__(self):
        returnString = ''
        for item in self.availableResourceDic:
            returnString += item+' '+str(self.availableResourceDic[item])+'\n'
        return returnString
