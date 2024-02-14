class Filmes:

    def __init__(self):
        self.__filmes = ['Batman','Morbius','Sonic', 'Espiral', 'Lamb', 'Escolha ou morra']
        self.__descricao = [
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Após a morte de seus pais, o jovem bilionário Bruce Wayne (Robert Pattinson) age como vigilante noturno em Gotham City. No entanto, uma série de crimes desafiará as suas habilidades heróicas. Enquanto isso, o Charada (Paul Dano) decide fazer um jogo de gato e rato com Bruce e o comissário James Gordon (Jeffrey Wright).</span></p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">O bioquímico Michael Morbius tenta curar-se de uma doença rara no sangue mas, sem perceber, ele fica infectado com uma forma de vampirismo.</span></p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Sonic, o porco-espinho azul mais famoso do mundo, se junta com os seus amigos para derrotar o terrível Doutor Eggman, um cientista louco que planeja dominar o mundo, e o Doutor Robotnik, responsável por aprisionar animais inocentes em robôs.</p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">O detetive Zeke Banks investiga o caso de um assassino em série que está seguindo os passos de Jigsaw. Involuntariamente, ele se vê preso no centro do jogo mórbido do homicida.</p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">María e Ingvar, um casal sem filhos, descobrem um misterioso recém nascido na sua quinta na Islândia. A prespectiva inesperada de uma vida familiar tráz-lhes muita felicidade, antes de começar a destruí-los. “As imagens do prólogo estabelecem desde o início que esta será uma experiência cinematográfica cativante.</p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Dois amigos descobrem um estranho jogo retrô que oferece um grande prêmio em dinheiro. Porém, o desafio contém uma maldição sangrenta capaz de invadir a realidade e eles logo descobrem que não estão jogando por dinheiro, mas pelas suas vidas.</p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">DESCRIÇÃO</p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">DESCRIÇÃO</p>',
            '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">DESCRIÇÃO</p>',
            ]
        #self.__classificacao = [10,12,15]
        self.__id = [0,1,2,3,4,5]
        self.__pathIMG = [
            ":/filmesIMG/images.jpg",
            ":/filmesIMG/images_1.jpg",
            ":/filmesIMG/Sonic_the_Hedgehog_2019.jpg",
            ":/filmesIMG/3152202.jpg",
            ":/filmesIMG/4198735.jpg",
            ":/filmesIMG/escolha-ou-morra-poster.jpg",
        ]

    def getNome(self, id):
        return self.__filmes[id]

    def getDescricao(self, id):
        return self.__descricao[id]

    def getPath(self, id):
        return self.__pathIMG[id]

    def getId(self):
        return self.__id


filme = Filmes()
