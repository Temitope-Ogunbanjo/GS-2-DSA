import json

def JumpLine(Num):
    print("\n" * Num)  

def Lock(Texto, Range):
    while True:
        Resultado = input(Texto).strip()
        if Resultado.isdigit():
            Valor = int(Resultado)
            if Range[0] <= Valor <= Range[1]:
                return Valor
        print(f"[!] Opção inválida. Digite um número entre {Range[0]} e {Range[1]}.")

def Text(Texto, Length):
    while True:
        Resultado = input(Texto).strip()
        if len(Resultado) > Length:
            return Resultado
        print(f"[!] Opção Invalída. Digite uma string válida, não nula, com pelo menos {Length} caracteres!")

def Digit(Texto):
    while True: 
        Resultado = input(Texto).strip()
        if Resultado.isdigit():
            return int(Resultado)
        print(f"Digite um valor numérico válido (integer)")

def ReadSetings():
    try:
        with open("appsettings.json", "r", encoding="utf-8") as file:
            Data = json.load(file)
            return Data["Settings"]
    except (FileNotFoundError, json.JSONDecodeError):
            return []


