import math

def soma(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a: float, b: float) -> float:
    """Retorna a subtração de dois números (a - b)."""
    return a - b

def multiplicacao(a: float, b: float) -> float:
    """Retorna a multiplicação de dois números."""
    return a * b

def divisao(a: float, b: float) -> float:
    """Retorna a divisão de dois números, tratando divisão por zero."""
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a / b

def exponenciacao(a: float, b: float) -> float:
    """Retorna a exponenciação a ** b."""
    return a ** b

def raiz(a: float, n: float = 2) -> float:
    """Retorna a raiz n-ésima de um número.
    Por padrão, calcula a raiz quadrada (n=2).
    """
    if n == 0:
        raise ValueError("Erro: não existe raiz de ordem 0.")
    if a < 0 and n % 2 == 0:
        raise ValueError("Erro: não é possível calcular raiz par de número negativo.")
    return a ** (1/n)

def ler_numero(mensagem: str) -> float:
    """Lê um número de ponto flutuante da entrada do usuário com validação."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def menu() -> None:
    """Exibe o menu interativo da calculadora científica."""
    while True:
        print("\n===== Calculadora Científica =====")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Exponenciação (a ** b)")
        print("6. Raiz n-ésima")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                a = ler_numero("Digite o primeiro número: ")
                b = ler_numero("Digite o segundo número: ")
                print(f"Resultado: {soma(a, b)}")

            elif opcao == "2":
                a = ler_numero("Digite o primeiro número: ")
                b = ler_numero("Digite o segundo número: ")
                print(f"Resultado: {subtracao(a, b)}")

            elif opcao == "3":
                a = ler_numero("Digite o primeiro número: ")
                b = ler_numero("Digite o segundo número: ")
                print(f"Resultado: {multiplicacao(a, b)}")

            elif opcao == "4":
                a = ler_numero("Digite o numerador: ")
                b = ler_numero("Digite o denominador: ")
                print(f"Resultado: {divisao(a, b)}")

            elif opcao == "5":
                a = ler_numero("Digite a base: ")
                b = ler_numero("Digite o expoente: ")
                print(f"Resultado: {exponenciacao(a, b)}")

            elif opcao == "6":
                a = ler_numero("Digite o número: ")
                n = ler_numero("Digite o índice da raiz (padrão=2): ")
                print(f"Resultado: {raiz(a, n)}")

            elif opcao == "0":
                print("Saindo... Até mais!")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    menu()
