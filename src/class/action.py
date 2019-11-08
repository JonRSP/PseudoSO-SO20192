# -*- coding: utf-8 -*-
'''
A ação é um elemento da execução de um processo, aparentemente envolve a manipulação de arquivos

" partir da linha n + 3: cada linha representa uma operação a ser efetivada pelo sistema de arquivos do
 pseudo-SO.  Para  isso,  essas  linhas  vão  conter:  <ID_Processo>,  <Código_Operação>,
 <Nome_arquivo>, <se_operacaoCriar_numero_blocos>, <Numero_Operacao_Processo>. "
'''
from file import File
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

    def doAction(self, action, process, secondaryMemory):
        if (action.operationCode == 0):
            # cria
            added = secondaryMemory.addFile(File(action.fileName, action.numberOfBlocks))
            if(added == 1):
                print("Não há espaço para criar o arquivo "+action.fileName)
            elif(added == 2):
                print("O arquivo "+ action.fileName + " já existe")
            else:
                print('Arquivo '+ action.fileName +' criado com sucesso.')
        else:
            # deleta 
            deleted = secondaryMemory.removeFile(action.fileName)
            if(deleted == 1):
                print('O processo ' + process.id  + ' não pode deletar o arquivo' + action.fileName + 'porque não existe esse arquivo.')
            else:
                print('Arquivo '+ action.fileName +' deletado com sucesso.')