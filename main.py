def code():
  x = int(input("Digite um número: "))
  z = int (input("Digite outro número: "))
  
  method = int(input("Escolha o método desejado: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 Divisão: "))
  
  if method == 1:
    print(x+z)
  elif method == 2:
    print(x-z)
  elif method == 3:
    print(x*z)
  elif method == 4:
    print(x/z)
  
  restart = int(input("Deseja reiniciar? 1 - Sim, 2 - Não: "))
  
  if restart == 1:
    code()
  else:
    print("Obrigado por usar nosso programa!")
code()