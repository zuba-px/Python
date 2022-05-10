names = ['kaique','brenda', 'luan','vinicius','sammy','jane','weller','zapata','edgar','dean',]
rgm = ['985','475', '412', '521', '635', '748', '987', '032']
print('****************** NÃO USAR ESPAÇO NO NOME E NEM NO RGM ******************')
name = input('Type your name:')
password = input('Type your rgm:')

if name in names and password in rgm:
    print('You pass in the test')
elif name == "" or password == "":
    print('You Fail, try again')
    while name or password == "":
        print('Name or rgm are wrong, try again')
        name = input('Type your name:')
        password = input('Type your rgm:')


else:
    print('Você falhou no teste')

