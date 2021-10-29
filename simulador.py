while True: 
    print("-------------------------")
    print("   Seja bem- vindo(a)    ")
    print("  ao Tesouro Prefixado   ")
    print("-------------------------")

    print("Títulos que estão disponíveis para simulação:")
    print("1; Tesouro Prefixado 2024")
    print("2; Tesouro Prefixado 2026")

    escolha = input("Selecione a simulação que gostaria de fazer: 1/2; ")

    if escolha == '1':
        v_inicial = int(input("Qual valor gostaria de investir agora?: "))
        v_mensal = int(input("Qual valor você poderá investir mensalmente?: "))

        valor = (v_mensal*32) + v_inicial
        ir = (valor*0.20)/100
        v_ir = valor - ir
        b3 = (valor*0.25)/100
        lucro = valor*0.1081
        v_bruto = valor + lucro

        v_lqd = valor - (ir + b3)

        print("-------------------------")
        print(" RESULTADO DA SIMULAÇÃO  ")
        print("-------------------------")
        print("Valor inicial investido: R$ ", v_inicial)
        print("Aportes mensais: R$", v_mensal,"(32)")
        print("-------------------------")
        print("      Valor estimado     ")
        print("Valor bruto: R$", v_bruto)
        print("I.R: -R$", ir)
        print("Taxa da B3: -R$", b3)
        print("Valor líquido: R$", v_lqd)
        print("-------------------------")

        sn = int(input("Deseja simular com outro título? s/n: "))
    
    else:
        v_inicial = int(input("Qual valor você gostaria de investir agora?: "))
        v_mensal = int(input("Qual valor você poderá investir mensalmente?: "))

        valor = (v_mensal*50) + v_inicial
        ir = (valor*15)/100
        v_ir = valor - ir
        b3 = (valor*0.25)/100
        lucro = valor*0.1081
        v_bruto = valor + lucro

        v_lqd = valor - (ir + b3)

        print("-------------------------")
        print(" RESULTADO DA SIMULAÇÃO  ")
        print("-------------------------")
        print("Valor inicial investido: R$ ", v_inicial)
        print("Aportes mensais: R$", v_mensal,"(50)")
        print("-------------------------")
        print("      Valor estimado     ")
        print("Valor bruto: R$", v_bruto)
        print("I.R: -R$", ir)
        print("Taxa da B3: -R$", b3)
        print("Valor líquido: R$", v_lqd)
        print("-------------------------")
        sn = int(input("Deseja simular com outro título? s/n: "))

        if sn == 'n':
            break

print("Programa encerrado")