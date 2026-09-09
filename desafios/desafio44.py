preco = float(input('Qual o valor do prosuto? '))

print('Qual será a forma de pagamento?')
print('1 - À vista - Dinheiro ou cheque')
print('2 - No cartão')

opcao = int(input('Como deseja fazer? '))

if opcao == 1:
    print(f'Para pagamento à vista, o total fica R${float(preco-(preco/100*10))}, por que teve R${float(preco/100*10)} de desconto!')
elif opcao == 2:
    parcelas = int(input('Em quantas vezes deseja fazer? '))
    elif parcelas == 1:
    print(f'Para gamento à vista no cartão, o total fica R${float(preco-(preco/100*5))}, por que teve R${float(preco/100*5)} de desconto!')
    elif parcelas == 2:
        print(f'Para pagamento em até 2 vezes no cartão o total fica R${preco}!')
    elif parcelas >= 3:
        print(f'Para pagamento em 3x ou mais o valor total fica R${preco+(preco/100*20)} por que tem 20% de juros que totaliza R${preco/100*20}!')
    else:
        print(f'Quantidade de parcelas invalidas!')
else:
    print(f'Opção invalida! refaça todo novamente!')