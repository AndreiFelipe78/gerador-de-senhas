import random

def create_password():
    print('Bem vindx ao seu gerador de senhas')
    while True:
        try:
            tamanho = int(input('\ndigite a quantidade de caracteres que a senha deve ter: '))
        except ValueError:
            print('Opção inválida! Escolha o tamanho da sua senha digitando o numero de caracteres desejado.')
        else:
            passwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K',    'L','M','N','O',    'P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','#','$','%','&','(',')','*','+','-','/','<','=','>','?','@',     '_', '{', '}', '|', '~', '[', ']    ', '"']
            random.shuffle(passwd)
            passwd = random.sample(passwd, tamanho)
            new_passwd = "".join(passwd)
            print('Sua nova senha é: {}'.format(new_passwd))
            break

create_password()
    