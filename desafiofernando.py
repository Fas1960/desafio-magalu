
# Montagem inicial do grafo pode ser qualquer arquivo de input
dict_grafo = {
            'Carlos': ['Ana'],
            'Ana': ['Maria','Vinicius','Carlos','Joao'],
            'Maria': ['Ana','Vinicius'],
            'Vinicius': ['Ana','Maria'],
            'Joao': ['Ana','Luiza'],
            'Luiza': ['Joao'],
}

dict_grafo

#criação inicial dos nos do grafo e dos relacionamentos entre os nos
def monta_relacionamentos_nos(dicionario):

    relacionamentos = []
   
    for chave in dicionario.keys():
                
        for vertice in dicionario[chave]:
            relacionamentos.append((chave, vertice))

    return relacionamentos

relacionamentos = monta_relacionamentos_nos(dict_grafo)


#criação da classe Grafo
class Grafo(object):
    
    def __init__(self, relacionamentos):
        # Adjacencias
        self.adj = {}
        self.relacionamentos = relacionamentos
        self.adiciona_relacionamentos(relacionamentos)
        
    def cria_relacionamentos(self, u, v):

            if u not in list(self.adj.keys()):
                self.adj[u] = [v]
            else:
                if v not in self.adj[u]:
                    self.adj[u].append(v)
                    
    def adiciona_relacionamentos(self, relacionamentos):

        for u, v in relacionamentos:
            self.cria_relacionamentos(u, v)
            
    def mostra_nos(self):
        return list(self.adj.keys())

 # identifica todos os relacionamentos da pessoa informada não importando se tem letra maiúscula e minúsculas   
    def conhecidos_pessoa (self,pessoa):
        lista_relacionamentos=list()
        encontrou=0
        for pesquisa in relacionamentos:
            pessoa_minusculo=pesquisa[0]
            if pessoa_minusculo.lower() == pessoa.lower():
                lista_relacionamentos.append (pesquisa[1])
                encontrou=1
        
        if encontrou==0:
            lista_relacionamentos ="ERRO RELACIONAMENTOS NÃO ENCONTRADOS"
                
        return lista_relacionamentos    
    
 # Cadastra novas pessoas e seus respectivos relacionamento
    def incluir_nova_pessoa (self):
        
        trata_nova_pessoa ="1"
        
        while trata_nova_pessoa == "1":
            lista_pessoas = list()
            nova_pessoa = str (input ("Informe nome da pessoa ser cadastrada => "))
            lista_pessoas = grafo.mostra_nos()
            if nova_pessoa in list(lista_pessoas):
                print ("\n Pessoa informada já faz parte do cadastro\n")
                trata_nova_pessoa="0"
            else:
                novos_relacionamentos = list()
                nova_relacao ="1"
                while nova_relacao!="":
                    nova_relacao= str(input ("Informe o nome  do relacionamento ou enter para encerrar => "))
                    if nova_relacao !="":
                        if nova_relacao not in list(lista_pessoas):
                            print ("Amigo ainda não cadastrado")
                        else:
                            novos_relacionamentos.append (nova_relacao)
                    else:
                        if novos_relacionamentos =="":
                            print ("Nenhum relacionamento foi informado")
                            trata_nova_pessoa="0"
                        else:
                            for indice in novos_relacionamentos:
                                self.cria_relacionamentos(nova_pessoa, indice)
                                self.relacionamentos.append((nova_pessoa, indice))
                            
                            lista_nos = grafo.mostra_nos()
                            print ("\n Nós do grafo ==> ",lista_nos)
                            retorno =grafo.conhecidos_pessoa(nova_pessoa)
                            print(f"\n Relacionamentos de {nova_pessoa} encontrados => {retorno} \n")
                            
            trata_nova_pessoa="0"  
    
#busca amigos dos amigos de uma pessoa informada e quenão façam parte do relacionamento dela

    def busca_amigos_dos_amigos (self):
        
        nao_amigos = list()
        pessoa=str(input ("Informe o nome da pessoa para buscar amigos fora do relacionamentos ==> "))
        lista_nos = grafo.mostra_nos()
        retorno =grafo.conhecidos_pessoa(pessoa)
        
        for indice in lista_nos:
            if indice.lower() != pessoa.lower() and indice not in retorno:
                nao_amigos.append(indice)
        
        return pessoa,nao_amigos
    
# criação de menu para direcionar o processo
    def menu(self):
        opcao="1"
        while opcao != "0":
            print('1. Mostra nós do grafo')
            print('2. Mostra conhecidos de determinada pessoa')
            print('3. Mostra pessoas que os amigos da pessoa conhecem e ela não')
            print('4. Cadastrar novas pessoas')
            print('0. Sair')
            opcao = str(input('Digite a sua opcao: '))

            if opcao == "1":
                lista_nos= list()
                lista_nos = grafo.mostra_nos()
                print ("\n Nós do grafo ==> ",lista_nos)
                
            elif opcao == "2":
                pessoa=str(input ("Informe o nome da pessoa que deseja buscar relacionamentos ==> "))
                retorno =grafo.conhecidos_pessoa(pessoa)
                print(f"\n Relacionamentos de {pessoa} encontrados => {retorno} \n")
            elif opcao == "3":
                pessoa,amigos_dos_amigos=grafo.busca_amigos_dos_amigos()
                print(f"\n Relacionamentos de {pessoa} ainda não amigo => {amigos_dos_amigos} \n")
            elif opcao == "4":
                grafo.incluir_nova_pessoa()
            elif opcao != "0":
                print('Opção inválida!')

                
# chama menu de direcionamento
grafo=Grafo(relacionamentos)

grafo.menu()