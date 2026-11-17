"""
    INTEGRANTES

    - Temitope Kuku da Silva Ogunbanjo (RM: 573772 )
    - Gustavo de Souza Abreu (RM : 574080)
    - Gabriel Oliveira Gusmãos Florencio dos Santos (RM: 573747)
"""

from menu import Menu
from helpers import JumpLine
from helpers import Lock
from helpers import Text
from helpers import Digit
from helpers import ReadSetings


Flag = True

App = Menu()
App.LoadJson()

def Header():
    JumpLine(1)
    print(f"=" * 25 + "Bem Vindo ao Citizen Assist AI" + "=" * 25)
    print("> Dica: Você pode adicionar registros a base diretamente no appsettings.json!")
    JumpLine(1)

def Functions():
    JumpLine(1)
    print("-" * 25 + "Escolha a Sua próxima Função" + "-" * 25)
    JumpLine(1)
    print("> 1 - Listar Registros")
    print("> 2 - Criar Registro")
    print("> 3 - Deletar Registro (Id)")
    print("> 4 - Atualizar Registro (Id)")
    print("> 5 - Exibir Registro (Informações)")
    print("> 6 - Buscar/Pesquisar Registro (Id, Nome, Categoria, etc..")
    print("> 7 - Ordenar Lista (Categoria, Id)")
    print("> 8 - Atualizar JSON's de Visualização")
    print("> 9 - Encerrar Programa")
    JumpLine(1)

Header()

while Flag:
    Functions()

    Action = Lock("Digite a ação desejada: ", [1, 8])

    match Action:
        case 1:
            print("\n")
            App.Listar()
        case 2:
            print("\n")
            print("-" * 25 + "Digite os Valores do Registro" + "-" * 25)
            Categorias = ReadSetings()["Categorias"]
            Data = {}
            LocalFlag = True
            for I in Categorias:
                Value = Text(f"> Digite o/a {I} do Registro: ", 2)
                Data[I] = Value
            App.Cadastrar(Data)
        case 3:
            print("\n")
            Id = Digit("> Digite o Id do Registro a ser deletado: ")
            App.Excluir(Id)
        case 4:
            print('\n')
            Categorias = ReadSetings()["Categorias"]
            Id = Digit("> Digite o ID do Registro a ser atualizado: ")

            print("-" * 25 + "Qual dado você deseja mudar?" + "-" * 25)
            print("\n")

            for I,V in enumerate(Categorias):
                print(f"> {I + 1}: {V}")

            print('\n')

            Categoria  = Lock("Digite a categoria a ser alterada: ", [1, len(Categorias) + 1])
            print("\n")
            Categoria = Categorias[Categoria - 1]
            Valor = Text("Digite o novo valor (atualizado): ", 2)
            App.Atualizar(Id, Categoria, Valor)

        case 5:
            print("\n")
            Id = Digit("> Digite o ID do Registro a ser exibido: ")
            Registro = App.Pesquisar("Id", Id)
            if Registro:
                App.Exibir(Registro[0])
        case 6:
            print("\n")
            Categorias = ReadSetings()["Categorias"]
            print("-" * 25 + "Por qual dado você deseja pesquisar?" + "-" * 25)
            print("\n")

            for I,V in enumerate(Categorias):
                print(f"> {I + 1}: {V}")

            print('\n')
            
            Categoria  = Lock("Digite a categoria a ser buscada: ", [1, len(Categorias) + 1])

            Categoria = Categorias[Categoria - 1]
            
            print("\n")

            Valor = Text(f"Digite o valor a ser buscada nos/nas {Categoria}: ", 2)

            Registro = App.Pesquisar(Categoria, Valor)

        case 7: 
            print("\n")
            Categorias = ReadSetings()["CategoriasOrdenaveis"]
            print("-" * 25 + "Por qual dado você deseja ordenar os registros?" + "-" * 25)
            print("\n")

            for I,V in enumerate(Categorias):
                print(f"> {I + 1}: {V}")

            print('\n')
            
            Categoria  = Lock("Digite a categoria a ser ordenada: ", [1, len(Categorias) + 1])
            Categoria = Categorias[Categoria - 1]

            App.Ordenar(Categoria)

            App.Listar(Categoria)

        case 8:
            App.AtualizarJsons()
        case 9:
            Flag = False
            break
            