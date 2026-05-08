# Criar uma Def - função que encapsula todo o código do Fluxo de controle do Bonus
# ou seja tudo que estiver dentro do While


salario = False
bonus = False


def fluxo_de_bonus():

    while not nome:
        try:
            nome = input("Digite seu nome: ")
        except ValueError as e:
            print(f"Erro: {e}")
            nome = False
        if len(nome) == 0:
            raise ValueError("O nome não pode ser vazio.")
        elif any(char.isdigit() for char in nome):
            # verifica se o nome contém números e lança um erro caso seja verdade
            raise ValueError("O nome não pode conter números.")
        else:
            print(f"Olá, {nome}! Bem-vindo ao curso de Python para Dados!")
    except ValueError as e:
        print(f"Erro: {e}")
        nome = False  # Reinicia a variável para continuar o loop

    while not salario:
        try:
            salario = float(input("Digite seu salário: "))
            if salario < 0:
                raise ValueError("O salário não pode ser negativo.")
            except ValueError as e:
            print(f"Erro: {e}")
            salario = False
            salario = False  # Reinicia a variável para continuar o loop

    while not bonus:
        try:
        bonus = float(input("Digite a porcentagem do bônus: "))
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
            print("Erro: certifique-se de que o bônus é um número válido e não negativo.")
        except ValueError as e:
            print(f"Erro: {e}")
            bonus = False
            bonus = True
    except ValueError:
        print("Erro: certifique-se de que o bônus é um número válido e não negativo.")


valor_do_bonus: int = 1000 + salario * bonus
kpi: float = valor_do_bonus + salario / 1000

print(f"Olá {nome}, o seu salário é R${salario:.2f} e o seu bônus foi de {valor_do_bonus:.2f}")
print(f"Seu KPI é: {kpi:.2f}")
