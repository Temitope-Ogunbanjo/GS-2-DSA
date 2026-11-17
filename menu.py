import json
from typing import TypedDict, Required, NotRequired

'''
    Classe - Registro (Node)
'''
class Node(TypedDict):
    Id : str
    Titulo : str
    Categoria : str
    Descricao : str
    PublicoAlvo : str
    Canal : NotRequired[str]
    LocalAtendimento : NotRequired[str]

class Node:
    def __init__(self, Data : Node):
        self.Id = Data["Id"]
        self.Proximo = None
        self.Items = {}
        self.Items["Titulo"] = Data["Titulo"]
        self.Items["Categoria"] = Data["Categoria"]
        self.Items["Descricao"] = Data["Descricao"]
        self.Items["PublicoAlvo"] = Data["PublicoAlvo"]
        if Data["Canal"]:
            self.Items["Canal"] = Data["Canal"]

        if Data["LocalAtendimento"]:
            self.Items["LocalAtendimento"] = Data["LocalAtendimento"]


class Menu:
    def __init__(self):
        self.Main = None
        self.CurrentId = 0
        
    def AtualizarJsons(self):

        def SerializarTree(Registro):
            if Registro is None:
                return None

            Estrutura = {"Id": Registro.Id}
            
            for I, V in Registro.Items.items():
                Estrutura[I] = V

            Estrutura["Proximo"] = SerializarTree(Registro.Proximo)
            
            return Estrutura

        def SerializarId(Registro):
            if Registro is None:
                return None

            proximo_id = Registro.Proximo.Id if Registro.Proximo is not None else None

            Estrutura = {
                "ProximoId": proximo_id,
                "Proximo": SerializarId(Registro.Proximo)
            }
            
            return Estrutura
        
        TreeData = SerializarTree(self.Main)
        
        IdData = {}
        if self.Main is not None:
            IdData[str(self.Main.Id)] = SerializarId(self.Main)

        with open("Id.json", "w", encoding="utf-8") as Arquivo:
            json.dump(IdData, Arquivo, indent=4, ensure_ascii=False)

        with open("Tree.json", "w", encoding="utf-8") as Arquivo:
            json.dump(TreeData, Arquivo, indent=4, ensure_ascii=False)
    

    def LoadJson(self):
        try:
            with open("appsettings.json", "r", encoding="utf-8") as file:
                Data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            Data = [] 
            
        for Item in Data["Data"]:
            self.Cadastrar(Item, True)

        self.Ordenar("id")

    def Cadastrar(self, Data : Node, Message=False):
        Data["Id"] = self.CurrentId
        self.CurrentId += 1
        Registro = Node(Data)
        Registro.Proximo = self.Main
        self.Main = Registro
        if not Message:
            print("\n")
            print("=" * 25 + f"Registro: {Registro.Items["Titulo"]} Inserido com Sucesso | Id : {Registro.Id}" + "=" * 25)

    def Listar(self, Categoria=False):

        if not self.Main:
            print("A Lista está vazia")
            return

        Current = self.Main

        print("=" * 25 + "Lista de registros ativos" + "=" * 25)

        while Current is not None:
            if Categoria and Categoria.lower() != "id":
                print(f"Titulo: {Current.Items["Titulo"]} | ID: {Current.Id} | {Categoria}: {Current.Items[Categoria]}")
            else:
                print(f"Titulo: {Current.Items["Titulo"]} | ID: {Current.Id}")
            Current = Current.Proximo

    def Atualizar(self, Id, Categoria, Valor):
        Current = self.Main

        while Current is not None:
            if Current.Id == Id:
                Current.Items[Categoria] = Valor
                print("\n")
                print("-" * 25 + f" Registro com ID {Id} teve seu/sua {Categoria} Atualizado para '{Valor}'" + "-" * 25)
                return True
            Current = Current.Proximo
            
        print(f"> ID: {Id} não encontrado na base")
        return False

    def Excluir(self, Id):
        Current = self.Main
        Anterior = None

        while Current is not None and Current.Id != Id:
            Anterior = Current
            Current = Current.Proximo

        if Current is None:
            print(f"> ID: {Id} não encontrado (sem necessidades de exclusão)")
            return False

        if Anterior is None:
            self.Main = Current.Proximo
        else:
            Anterior.Proximo = Current.Proximo

        print(f"> Registro com ID: {Id} ({Current.Items["Titulo"]}) excluído.")

    def Exibir(self, Registro):
        if not Registro:
            print("\n")
            print("Registro não encontrado na Base")
            print("\n")

        print("\n")
        print("=" * 25 + f"Registro: {Registro.Items["Titulo"]}" + "=" * 25)

        print("\n")
        print(f"> Id: {Registro.Id} ")
        
        for I,V in Registro.Items.items():
            print(f"> {I}: {V}")

        print("\n")

    def Pesquisar(self, Atributo, Valor):
        Current = self.Main
        Resultado = []

        print("\n")
        while Current is not None:
            if Atributo.lower() == "id":
                if Current.Id == Valor:
                    print(f"> Registro ({Current.Items["Titulo"]}) com Id : {Valor} foi encontrado")
                    Resultado.append(Current)
                Current = Current.Proximo
            else:
                if Current.Items[Atributo] == Valor:
                    print(f"> Registro com {Atributo}: {Valor} foi encontrado | Id: {Current.Id}, Titulo : {Current.Items["Titulo"]}")
                    Resultado.append(Current)
                Current = Current.Proximo

        if len(Resultado) == 0:
            print(f"> Não forão encontrados registros com {Atributo} de valor {Valor}!")

        return Resultado
    
    def Ordenar(self, Categoria):
        if self.Main is None or self.Main.Proximo is None:
            return
        
        Ordenada = None
        Current = self.Main

        if Categoria.lower() == "id":
            while Current is not None: 
                Proximo = Current.Proximo

                if Ordenada is None or Current.Id < Ordenada.Id:
                    Current.Proximo = Ordenada
                    Ordenada = Current
                else:
                    Temp = Ordenada
                    while (Temp.Proximo is not None and Temp.Proximo.Id < Current.Id):
                        Temp = Temp.Proximo
                    Current.Proximo = Temp.Proximo
                    Temp.Proximo = Current

                Current = Proximo
        else:
            while Current is not None: 
                Proximo = Current.Proximo

                if Ordenada is None or Current.Items[Categoria].lower() < Ordenada.Items[Categoria].lower():
                    Current.Proximo = Ordenada
                    Ordenada = Current
                else:
                    Temp = Ordenada
                    while (Temp.Proximo is not None and Temp.Proximo.Items[Categoria].lower() < Current.Items[Categoria].lower()):
                        Temp = Temp.Proximo
                    Current.Proximo = Temp.Proximo
                    Temp.Proximo = Current

                Current = Proximo

        self.Main = Ordenada
        self.AtualizarJsons()