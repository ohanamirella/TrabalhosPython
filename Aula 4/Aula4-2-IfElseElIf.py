# Aula 4 11-11-2019
# Estrutura de decisão 2


idade = 17.5
#--- If simples, validação de apenas uma condição
if idade ==18:
    print('Maior')
#--- If com else, 
#--- Caso a condição validada pelo If não seja verdadeira, 
#--- O Else é executado

if idade < 18:
    print('Menor')
else:
    print('Maior')

#--- If com Elif e else
#--- Caso a condição validada no if seja falsa
#--- É validado a condição do ElIf
#--- Caso a condição do ElIf seja falsa
#--- Else é executado
if idade < 18:
    print('Dimenor')
elif idade == 18:
    print('Silasco')
else:
    print('SilascoMaisAinda')

#--- If com variável booleana
#--- Em caso de variável booleana, não é necessário a validacao(==True)
#--- Pois o If ja valida o se o conteúdo da variável é True, senão vai para o Else
ativo = True
if ativo:
    print('Logar')
else:
    print('Não pode')