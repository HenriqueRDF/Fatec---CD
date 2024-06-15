import time

min = 1
print("Jogo do Adivinha")
nmax = int(input("Digite o valor Max: "))
print("PC: Pense em um número entre 1 e", nmax)
print("PC: Eu vou adivinhar...")
time.sleep(2)

while True:
    calc = (min + nmax)//2  # // para evitar divisão de ponto flutuante
    print("PC: Meu palpite é:", calc)
    resp = input("PC: É maior, menor ou igual ao número que você pensou? (>, <, =) ")

    if resp == "=":
        print("PC: Acertei! o((>ω< ))o")
        break
    elif resp == ">":
        print("O número é maior que", calc)
        min = calc + 1
        print("Eu: Tente de novo...")
        time.sleep(2)
    elif resp == "<":
        print("O número é menor que", calc)
        nmax = calc - 1
        print("Eu: Tente de novo...")
        time.sleep(2)