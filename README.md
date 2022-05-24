# desafio-magalu
Projeto desafio Magalu Desenvolvedor de Recomendações visando uma vaga de Desenvolvedor no Luizalabs.

Arquivo Dockerfile - Contém a criação do container do docker
Arquivo desafiofernando.ipynb - Programa em Python 3 que permite expor nós de um grafo, originalmente em input manual na inicializaçao do programa, permitindo o manuseio através ações feitas na barra de comando. Programa foi escrito usando o Jupyter pois o VSCODE que possuo instalado é uma versão para windows 7 que não permite o uso de das frameworks (Flask, request, json).

Os relacionamento iniciais foram inseridos através de um dicionário criado dentro do programa;
dict_grafo = {
            'Carlos': ['Ana'],
            'Ana': ['Maria','Vinicius','Carlos','Joao'],
            'Maria': ['Ana','Vinicius'],
            'Vinicius': ['Ana','Maria'],
            'Joao': ['Ana','Luiza'],
            'Luiza': ['Joao'],
}

Executando desafiofernando.ipynb ele ira mostrar o seguinte resultado:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Clicando no endereço ele irá responder a primeira pergunta do desafio, mostrar todos os nós criados dentro do processo. resposta deve ser:
["Carlos","Ana","Maria","Vinicius","Joao","Luiza"]

Inserindo /relacionamentos/nome da pessoa a pesquisar ele irá responder a segunda pergunta do desafio que é mostrar as pessoas que uma determiunada pessoa conhece.
Exemplo:
            http://127.0.0.1:5000/relacionamentos/Ana
            
            resposta será:
            
            ["Maria","Vinicius","Carlos","Joao"]
            
Inserindo /naoamigos/nome da pessoa ele irá mostrar a resposta para a terceira pergunta Mostrar as pessoas que os amigos conhecem e ela não.

Exemplo:
            http://127.0.0.1:5000/naoamigos/Ana
            
            resposta será:
            ["Luiza"]
            
E por último uma maneira de cadastrar novas pessoas.

Isso foi feito criando manualmenteum dicionário com o seguinte conteúdo:
            dict_novos_amigos = {
            'Fernando': ['Maria','Vinicius','Carlos','Joao'],
            'Gustavo' :['Fernando'],}
            
 Inserindo /novo o programa irá incluir no dicionário original os novos amigos do exemplo acima.
 
             http://127.0.0.1:5000/novo
            
            resposta será:
            {"Ana":["Maria","Vinicius","Carlos","Joao"],"Carlos":["Ana"],"Fernando":["Maria","Vinicius","Carlos","Joao"],"Gustavo":["Fernando"],"Joao":["Ana","Luiza"],"Luiza":["Joao"],"Maria":["Ana","Vinicius"],"Vinicius":["Ana","Maria"]}

