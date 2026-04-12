# Inicialização dos contadores
excelente = 0
ruim = 0

# Loop para 50 entrevistados
for i in range(50):
    print(f"\nEntrevistado {i+1}")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite a opção (1/2/3): "))
    
    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

# Resultado final
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")