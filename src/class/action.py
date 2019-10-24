# -*- coding: utf-8 -*-
'''
A ação é um elemento da execução de um processo, aparentemente envolve a manipulação de arquivos

" partir da linha n + 3: cada linha representa uma operação a ser efetivada pelo sistema de arquivos do
 pseudo-SO.  Para  isso,  essas  linhas  vão  conter:  <ID_Processo>,  <Código_Operação>,
 <Nome_arquivo>, <se_operacaoCriar_numero_blocos>, <Numero_Operacao_Processo>. "
'''
class Action:


    def __init__(self, elements):
        self.info = len(elements)
        self.processID = elements[0]
        self.operationCode = elements[1]
        self.fileName = elements[2]
        if(self.info == 4):
            self.numberOfOperation = elements[3]
        elif(self.info == 5):
            self.numberOfBlocks = elements[3]
            self.numberOfOperation = elements[4]
    def __str__(self):
        if(self.info == 4):
            return str(self.processID)+', '+str(self.operationCode)+', '+str(self.fileName)+', '+str(self.numberOfOperation)
        else:
            return str(self.processID)+', '+str(self.operationCode)+', '+str(self.fileName)+', '+str(self.numberOfBlocks)+', '+str(self.numberOfOperation)
