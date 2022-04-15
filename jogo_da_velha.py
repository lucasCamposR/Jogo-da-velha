





#tentando fazer um jogo da velha 
#os valores do jogo da velha é x e y
    


  
novoTabela=[0,0,0]
SengundaLinha=[0,0,0]
TerceiraLinha=[0,0,0]

def reiniciar():
    novoTabela.clear()
    SengundaLinha.clear()
    TerceiraLinha.clear()
    print(novoTabela)
    print(SengundaLinha)
    print(TerceiraLinha) 
           


def ganharAgora(indice,valor ):
    novoTabela.insert(indice,valor)
    for i in range(0,3):
        print(novoTabela)
    

def jogarPrimeiralinha(indice,valor):
    if jogarPrimeiralinha!=0:
        novoTabela.pop(indice)
        novoTabela.insert(indice,valor)
        print('jogada do jogador com o:',valor)
        print(novoTabela)
        print(SengundaLinha)
        print(TerceiraLinha)
            
 
def jogarSegundalinha(indice,valor):
       if jogarSegundalinha!=0:
        SengundaLinha.pop(indice)
        SengundaLinha.insert(indice,valor)
        print('jogada do jogador com o:',valor)
        print(novoTabela)
        print(SengundaLinha)
        print(TerceiraLinha)
        
 
def jogarTerceiralinha(indice,valor):
       if jogarTerceiralinha!=0:
        TerceiraLinha.pop(indice)
        TerceiraLinha.insert(indice,valor)
        print('jogada do jogador com o:',valor)
        print(novoTabela)
        print(SengundaLinha)
        print(TerceiraLinha)        
        
        

def SetarTabuleiro(numeroColocado):
      novoTabela.clear()
      SengundaLinha.clear()
      TerceiraLinha.clear()
      novoTabela.extend([numeroColocado,numeroColocado,numeroColocado])
      SengundaLinha.extend([numeroColocado,numeroColocado,numeroColocado])
      TerceiraLinha.extend([numeroColocado,numeroColocado,numeroColocado])
      print(novoTabela)
      print(SengundaLinha)
      print(TerceiraLinha)      
        
def avaliar():
        if(SengundaLinha[0]=='x'and novoTabela[0]=='x' and TerceiraLinha[0]=='x'): 
            print( 'jogador do x ganhou')
        elif (SengundaLinha[0]=='y'and novoTabela[0]=='y' and TerceiraLinha[0]=='y'): 
            print( 'jogador do y ganhou')
        elif (novoTabela[0]=='x' and novoTabela[1]=='x' and novoTabela[2]=='x'):
             print('jogador do x ganhou') 
        elif (novoTabela[0]=='y' and novoTabela[1]=='y' and novoTabela[2]=='y'):
               print('jogador do y ganhou')   
        elif (SengundaLinha[0]=='y' and SengundaLinha[1]=='y' and SengundaLinha[2]=='y'):
            print('jogador do y ganhei')         
        elif ( SengundaLinha[0]=='x' and SengundaLinha[1]=='x' and SengundaLinha[2]=='x'):
             print('jogador do x ganhou') 
        elif ( TerceiraLinha[0]=='x' and TerceiraLinha[1]=='x' and TerceiraLinha[2]=='x'):
             print('jogador do x ganhou')
        elif ( TerceiraLinha[0]=='y' and TerceiraLinha[1]=='y' and TerceiraLinha[2]=='y'):
             print('jogador do y ganhou')
        elif ( novoTabela[1]=='x' and SengundaLinha[1]=='x' and TerceiraLinha[1]=='x'):
             print('jogador do x ganhou') 
        elif ( novoTabela[1]=='y' and SengundaLinha[1]=='y' and TerceiraLinha[1]=='y'):
                 print('jogador do y ganhou')     
        elif ( novoTabela[2]=='y' and SengundaLinha[2]=='y' and TerceiraLinha[2]=='y'):
                 print('jogador do y ganhou')
        elif ( novoTabela[2]=='x' and SengundaLinha[2]=='x' and TerceiraLinha[2]=='x'):
                 print('jogador do x ganhou')  
        elif ( novoTabela[0]=='y' and SengundaLinha[1]=='y' and TerceiraLinha[2]=='y'):
                 print('jogador do y ganhou') 
        elif ( novoTabela[0]=='x' and SengundaLinha[1]=='x' and TerceiraLinha[2]=='x'):
                 print('jogador do x ganhou')
        elif ( novoTabela[2]=='x' and SengundaLinha[1]=='x' and TerceiraLinha[0]=='x'):
                 print('jogador do x ganhou') 
        elif ( novoTabela[2]=='y' and SengundaLinha[1]=='y' and TerceiraLinha[0]=='y'):
                 print('jogador do y ganhou')                            
                                                                                                               
        else:
            print("Deu velha")    
            








#jogarPrimeiralinha(0,'y')
#jogarPrimeiralinha(1,'y')
#jogarPrimeiralinha(2,'y')
#avaliar
#reiniciar







