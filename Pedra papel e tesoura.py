print("❀"*15)
print("Pedra - Papel - Tesoura")
print("❀"*15)
print()
print("━"*20)
print("|  Opção 1 - Pedra  |\n|  Opção 2 - Papel  |\n| Opção 3 - Tesoura |")
print("━"*20)

#Definindo as variáveis
import random
computer_choice=(random.randint(1,3))
user_choice=int(input("Digite um número para começar: "))

#while para escolhas invalidas
while user_choice>3 or user_choice<1:
    print("Assim não vale!!! \nTem que ser um número entre 1 e 3 >:( \nTente de novo! \n")
    user_choice=int(input("Digite um número para começar: "))

#comparando escolhas do usuário e computador - 1
if user_choice==1 and computer_choice==1:
    print ("Empate!")
elif user_choice==1 and computer_choice==2:
    print("Você perdeu! :(")
elif user_choice==1 and computer_choice==3:
    print("Você venceu! :)")

#comparando escolhas do usuário e computador - 2
elif user_choice==2 and computer_choice==1:
    print("Você venceu! :)")
elif user_choice==2 and computer_choice==2:
    print("Empate!")
elif user_choice==2 and computer_choice==3:
    print("Você perdeu! :(")

#comparando escolhas do usuário e computador - 3
elif user_choice==3 and computer_choice==1:
    print("Você perdeu! :(")
elif user_choice==3 and computer_choice==2:
    print("Você venceu! :)")
else:
    print("Empate!")

#Transformando as variáveis int em str
#Computador
if computer_choice==1:
    computer_choice="Pedra"
elif computer_choice==2:
    computer_choice="Papel"
else:
    computer_choice="Tesoura"
#Usuário
if user_choice==1:
    user_choice="Pedra"
elif user_choice==2:
    user_choice="Papel"
else:
    user_choice="Tesoura"
#Fim
print("Você escolheu",user_choice,"e o comutador escolheu",computer_choice,"!")