# Aula 28 - 17-12-2019
# Revisão de listas dicionário e arquivos

# Faça uma função que receba o texto como parametro e retorne uma lista com
#  dicionários.



def salvar_pessoa(pessoa_dicionario):
    texto = open ('aula28.txt','a')
    texto.write(f"{pessoa_dicionario['numero']};{pessoa_dicionario['nome']};{pessoa_dicionario['idade']}{pessoa_dicionario['email']};{pessoa_dicionario['numero']};{pessoa_dicionario['cpf']}\n")
    texto.close()
   
    texto = '''1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117
    2;Haroldo;44;f;baratarebelde@gmail.com;050923172729
    3;Pilar;50;m;wanderson10sp@gmail.com;018937341049
    4;Suzete Salvador;45;f;eladiomp2@yahoo.com.br;056928409823
    5;Riane;37;f;orkutzimpower@terra.com.br;018916004377
    6;Waldir;34;f;nandah.s2@bol.com.br;058903756441
    7;Lilian;22;f;arydoido@gmail.com;031958621596
    8;Matilde;20;m;eu_kaka_@hotmail.com;012941959390
    9;Samanta;19;m;carro.tuning@yahoo.com.br;028964480437
    10;Margarida;30;m;paraaconta.08@hotmail.com;047903547580
    11;Evelyn;31;m;joaosilvaticudo@gmail.com;053958638386
    12;Alessio;29;m;w.nill02@gmail.com;033961294774
    13;Yolanda;25;m;patty_karen2005@hotmail.com;027903312626
    14;Germana;33;f;jarlinhatopdelinhagv@hotmail.com;053964603415
    15;Helio;33;f;juh.slim@gmail.com;046997316461
    16;Liége;21;f;gledsonlds@hotmail.com;056992948431
    17;Yan;42;m;lucapratto@yahoo.com.br;016963562866
    18;Silvain;50;f;hie.s2@hotmail.com;021963399433
    19;Brian;33;f;juliagabrielle06@hotmail.com;027962676732
    20;Deoclides;40;f;patriciamascena@gmail.com;012961047979
    21;Jaqueline;32;m;aninha183@hotmail.com;014958997782
    22;Rosamaria;45;f;j_leosao@hotmail.com;026944672627
    23;Carla;42;m;jhasdfjo@hotmail.com;046976625208
    24;Aida Santos;30;f;nayara.cristinap@hotmail.com;034920819199
    25;Thomas;19;m;jfdslinda@bol.com.br;030974027667
    26;Naiara;23;m;darknees_666@ig.com.br;018976696717
    27;Karyne;17;m;garotosonhador_1@hotmail.com;054984689319
    28;Alenis Dias;43;f;vi_vi_cristinaf@hotmail.com;034980886309
    29;Grace;38;m;amandakell@uol.com.br;041932906720
    30;Zacarias;31;m;loca.som@hotmail.com;041926007066
    31;Marco;29;f;tashaqn@hotmail.com;050919604868
    32;Angélica;43;f;andrea_fatima2005@hotmail.com;031984219049
    33;Dionisio;38;f;tico_axe@yahoo.com.br;029971421524
    34;Cassio;23;m;blu.william@gmail.com;052974708463
    35;Selma;17;f;reinaldobeltrao@bol.com.br;051974848498
    36;Flávia;21;m;let_araujo23@yahoo.com.br;033918718514
    37;Osni;34;m;ash_highschool@hotmail.com;046975591151
    38;Timoteo;30;f;marcellaparaty@hotmail.com;040927395638
    39;Cristiane;38;m;lilimil125@yahoo.com.br;054918308625
    40;Else;45;m;laurinho_simoes@hotmail.com;042908347369
    41;Cecília;46;m;dani_sk8_95@hotmail.com;025963481920
    42;Giulliane;25;m;skarletlinda@hotmail.com;027905662731
    43;Feliciano;44;m;karinafloroliveira@hotmail.com;055985937562
    44;Cassiane;41;m;tauanerbd@gmail.com;025998359783
    45;Aléssia;21;f;thayna_bitencourt@yahoo.com.br;033950734254
    46;Josie;32;m;marclei@pop.com.br;033972950508
    47;Thayná;42;m;caio167@hotmail.com;028984798536
    48;Paola;50;m;chel_bdl@hotmail.com;024966119466
    49;Silvio;45;m;laurim_crazyboy@hotmail.com;033986392040
    50;Vanusa;23;m;aline_gatinha_13@yahoo.com.br;015938655596'''