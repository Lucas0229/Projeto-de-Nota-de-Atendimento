from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init()

# LISTA com os níveis do reservatório
niveis_reservatorio = [10, 25, 50, 75, 95]

def definir_cor(nivel):
    """
    FUNÇÃO que define a cor conforme o nível informado
    """
    if nivel == 1:
        return Fore.RED + Style.BRIGHT
    elif nivel == 2:
        return Fore.YELLOW + Style.BRIGHT
    elif nivel == 3:
        return Fore.GREEN + Style.BRIGHT
    elif nivel == 4:
        return Fore.CYAN + Style.BRIGHT
    elif nivel == 5:
        return Fore.BLUE + Style.BRIGHT
    else:
        return Fore.WHITE

# SIMULAÇÃO - Nível atual do reservatório (você pode alterar este valor)
nivel_atual = 2  # MUDE para 1, 2, 3, 4 ou 5 para testar

# Pega o nível da lista
porcentagem = niveis_reservatorio[nivel_atual - 1]

print("=== SISTEMA DE MONITORAMENTO ===")
print()

# APLICA A COR usando a função
cor = definir_cor(nivel_atual)

# EXIBE A SITUAÇÃO ATUAL com cor
print(cor + f"NÍVEL {nivel_atual}: {porcentagem}%", end=" | ")
Style.RESET_ALL

if nivel_atual == 1:
    print(cor + "MUITO BAIXO (CRÍTICO)" + Style.RESET_ALL)
elif nivel_atual == 2:
    print(cor + "BAIXO" + Style.RESET_ALL)
elif nivel_atual == 3:
    print(cor + "MÉDIO" + Style.RESET_ALL)
elif nivel_atual == 4:
    print(cor + "ALTO" + Style.RESET_ALL)
elif nivel_atual == 5:
    print(cor + "MUITO ALTO (ALERTA)" + Style.RESET_ALL)

print()
print("Restauração do estilo padrão do terminal:", Style.RESET_ALL)
print("=== FIM DO MONITORAMENTO ===\n")