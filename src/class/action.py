# -*- coding: utf-8 -*-
'''
A ação é um elemento da execução de um processo, aparentemente envolve a manipulação de arquivos

" partir da linha n + 3: cada linha representa uma operação a ser efetivada pelo sistema de arquivos do
 pseudo-SO.  Para  isso,  essas  linhas  vão  conter:  <ID_Processo>,  <Código_Operação>,
 <Nome_arquivo>, <se_operacaoCriar_numero_blocos>, <Numero_Operacao_Processo>. "
'''
class Action:
    self.processID = 0
    self.operationCode = 0
    self.fileName = 0
    self.numberOfBlocks = 0
    self.numberOfOperation = 0

    def __init__(self, elements):
        self.processID = elements[0]
        self.operationCode = elements[1]
        self.fileName = elements[2]
        if(len(elements) == 4):
            self.numberOfOperation = elements[3]
        elif(len(elements) == 5):
            self.numberOfBlocks = elements[3]
            self.numberOfOperation = elements[4]
