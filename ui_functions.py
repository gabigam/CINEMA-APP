from operator import index
from pydoc import cli
from docs import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
from filmes import *
import functools
from salas import *
from cliente import *

class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        #BOTÕES FIXOS
        self.pushButton_6.hide() #Esconde botão de CONTINUAR na pagina de escolha de lugares
        self.hideButton = False
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        #LISTAS ADM
        self.cliente = []
        #DEFININDO VARIÁVEIS IMPORTANTES
        self.dateSelect = 0 # 0 = Data 01 | 1 = Data 02 | 2 = Data 03 ....
        self.selectFilm = None
        self.position = None
        #Componentes dos horários
        self.saveSala_01 = []
        #LISTA DOS HORÁRIOS + DATAS
        self.dataButtons = [
                    self.pushButton,self.pushButton_2,self.pushButton_3,self.pushButton_4,self.pushButton_5
                ]
        self.hourPage = [
                    self.page_horario_1,self.page_horario_2,self.page_horario_3,self.page_horario_4,self.page_horario_5
                ]
        ####################################################
        self.labels = [
            self.filme_1, self.filme_2,self.filme_3,self.filme_4,self.filme_5,self.filme_6
        ]
        self.btnBack.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))

        for i in range(len(self.labels)): #Pegando labels dos filmes em cartaz
            self.labels[i].mousePressEvent = functools.partial(self.getFilme, film_id=i) #Pegando qual filme foi clicado e salvando ID
        
    def getFilme(self, event, film_id=None):
        for i in filme.getId():
            if i == film_id:
                #CARREGANDO PROPRIEDADES DA PÁGINA:
                #Adicionando horários
                self.addButtonHorario(i)       
                #Editando informações
                self.selectFilm = film_id
                self.filme_img.setPixmap(QtGui.QPixmap(filme.getPath(i))) #Pegando Path da imagem
                self.filme_name.setText(filme.getNome(i)) #Exibindo nome
                self.filme_descri.setHtml(filme.getDescricao(i)) #Exibindo descrição'''
                #Mudando de página
                self.stackedWidget.setCurrentWidget(self.page_2)
                #Mudando Data
                for count in range(len(self.dataButtons)):
                    self.dataButtons[count].mousePressEvent = functools.partial(self.changeButtonColor, button_id = self.dataButtons[count], count_id = count)

    def addButtonHorario(self,id):
        self.hourSelect = [] #Variável que serve para salvar o horário que foi selecionado
        #USAR AS VÁRIÁVEIS SALVDAS LÁ NO INCIO COM MÉTODO DE SETAR ELAS

        framesList = [
            self.frame_horario_1, 
            self.frame_horario_2,
            self.frame_horario_3,
            self.frame_horario_4,
            self.frame_horario_5
        ]  
        self.btn = [] #Onde será armazenado os botões - uma lista de Objetos
        btn_obj = 0
        #CREATE BUTTON
        for frameL in range(len(framesList)):
            horarioList = [ #Onde está sendo armazenado a lista de horários
                salas.getSala1()[id].split('==')[frameL].split('//'),
                salas.getSala2()[id].split('==')[frameL].split('//'),
                salas.getSala3()[id].split('==')[frameL].split('//'),
                salas.getSala4()[id].split('==')[frameL].split('//'),
                salas.getSala5()[id].split('==')[frameL].split('//')
            ]
            y_position = 15
            for h in range(5):
                x_position = 100 #Reseta a posição inicial dos horários

                for x in horarioList[h]:
                    if x != "''":
                        self.btn.append(None)
                        self.btn[btn_obj] = QPushButton(framesList[frameL])
                        self.btn[btn_obj].setGeometry(QtCore.QRect(x_position, y_position, 71, 31))
                        self.btn[btn_obj].setStyleSheet("QPushButton{\n"
                        "background-color: black;\n"
                        "color: white;\n"
                        "border-radius: 10px;\n"
                        "border: 2px solid black;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                        "background-color: black;\n"
                        "color: white;\n"
                        "border-radius: 10px;\n"
                        "border: 2px solid white;\n"
                        "}")
                        self.btn[btn_obj].setObjectName(x)
                        self.btn[btn_obj].setText(x)
                        self.hourSelect.append(x)
                        #Adicionando posição X para os próximos horários
                        x_position += 80
                        btn_obj += 1
                #Adicionando posição Y para os próximos horários
                y_position += 70
        self.selectHorario()
        self.btnBack.clicked.connect(lambda: self.delHorario()) #Verifica se botão de voltar foi clicado e limpa os Horários que foram adicionado

    def selectHorario(self):
        index_id = 0
        for k in self.dataButtons:
            k.mousePressEvent = functools.partial(self.setDate, index_page=k.objectName())
    
        for p in self.btn:
            p.mousePressEvent = functools.partial(self.setHorario, index=index_id, position = p.y())
            index_id += 1
        
    def setDate(self, event, index_page= None):
        self.dateSelect = 0
        for getButton in range(len(self.dataButtons)):
            if index_page == self.dataButtons[getButton].objectName():
                self.stackedWidget_2.setCurrentWidget(self.hourPage[getButton])
                self.dateSelect = getButton
    
    def setHorario(self, event, index=None, position=None):
        self.position = position
        dados = [filme.getNome(self.selectFilm), self.getSalaNumber(), self.hourSelect[index], self.dateSelect]
        #print(dados)
        cadeiras_compradas = salas.changeLugares(dados)
        #print(cadeiras_compradas)
        self.lugarComprar = []
        salaNumber = self.getSalaNumber() #Pegando número da Sala
        self.selectLugares = []
        self.buttLugares = [
            self.a1, self.a2, self.a3, self.a4,
            self.b1, self.b2, self.b3, self.b4,
            self.c1, self.c2, self.c3, self.c4
        ]
        for i in self.buttLugares: #Retornando todos os lugares para Disponíveis
            i.setText('')
            i.setChecked(False)

        if cadeiras_compradas != None: #Verificando os lugares que já foram comprado e mudando para INDISPONÍVEL
            for z in self.buttLugares:
                for x in cadeiras_compradas:
                    for nameObject in x:
                        if z.objectName() == nameObject:
                            z.setChecked(True)
                            z.setText('INDISPONÍVEL')
        self.stackedWidget.setCurrentWidget(self.page_3)
        for indexLugar in range(len(self.buttLugares)):
            self.buttLugares[indexLugar].mousePressEvent = functools.partial(self.setLugar, hourSelect=self.hourSelect[index], butt=self.buttLugares[indexLugar], hideButton = True)

    def setLugar(self, event, id_lugar=None, hourSelect = None,butt = None, hideButton = None):
        self.hideButton = hideButton
        if self.hideButton == True and butt.text() != 'INDISPONÍVEL':
            self.pushButton_6.show() #Mostrando botão de CONTINUAR
        stop_if = False
        if butt.isChecked() and butt.text() != 'INDISPONÍVEL':
            butt.setChecked(False)
            self.selectLugares.remove(butt.objectName())
            self.lugarComprar.remove(butt)
            stop_if = True
            if len(self.lugarComprar) == 0: #Verificando se nenhum lugar está selecionando e escondendo botão de continuar
                self.pushButton_6.hide()
                self.hideButton = False
        if butt.isChecked() == False and butt.text() != 'INDISPONÍVEL' and stop_if == False:
            butt.setChecked(True)
            self.selectLugares.append(butt.objectName())
            self.lugarComprar.append(butt)
        salaNumber = self.getSalaNumber() #Pegando número da Sala
        dados = [filme.getNome(self.selectFilm), salaNumber, hourSelect, self.dateSelect,self.selectLugares]
        self.pushButton_6.mousePressEvent = functools.partial(self.buy, dados_info = dados, lugares = self.lugarComprar)
        
    def buy(self, event, dados_info = None, lugares = None):       
        self.stackedWidget.setCurrentWidget(self.page_4)
        datas = ['31/05', '01/06', '02/06', '03/06', '04/06']
        qtd_lugares = len(dados_info[4])
        info_ingresso = f"INFORMAÇÕES DO INGRESSO\nQuantidade de lugares selecionados: {qtd_lugares}\nNúmero da Sala: 0{dados_info[1] + 1}\nData do filme: {datas[dados_info[3]]}\nHorário do filme: {dados_info[2]}\n"
        salas.lugares(dados_info)
        #print(salas.getLugaresComprados())
        #for i in lugares:
            #i.setChecked(False)
        self.label_14.setText(info_ingresso)
        self.filme_img_2.setPixmap(QtGui.QPixmap(filme.getPath(self.selectFilm))) #Pegando Path da imagem
        self.filme_name_2.setText(filme.getNome(self.selectFilm)) #Exibindo nome

        self.pushButton_8.mousePressEvent = functools.partial(self.finishBuy, dados = dados_info)
        self.pushButton_9.mousePressEvent = functools.partial(self.cancelarCompra, compra = dados_info)

    def finishBuy(self, event, dados = None):
        try:
            number = int(self.lineEdit_2.text())
            if len(self.lineEdit.text()) > 0 and len(self.lineEdit_2.text()) >= 9 and len(self.lineEdit_2.text()) <= 11:
                cliente = f'{self.lineEdit.text()} | {number} | {dados}'
                cliente_geral.adicionarCliente(cliente)
                msg = QMessageBox()
                msg.setWindowTitle("Ingresso Comprado Com Sucesso")
                msg.setText("Compra feita com sucesso")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                x = msg.exec_()
                self.pushButton_6.hide()
                self.stackedWidget.setCurrentWidget(self.page)
            else:
                self.errorPopUp("Verifique se os dados inseridos estão corretos")
        except:
            self.errorPopUp("Verifique se os dados inseridos estão corretos")

    def errorPopUp(self, msg_insert):
        msg = QMessageBox()
        msg.setWindowTitle("Erro ao comprar Ingresso")
        msg.setText(msg_insert)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def getSalaNumber(self):
        inicial_position = 15
        inicial_sala = 0
        for x in range(5):
            if self.position == inicial_position:
                return inicial_sala
            else:
                inicial_position += 70
                inicial_sala += 1

    def changeButtonColor(self, event, button_id = None, count_id = None):
        self.stackedWidget_2.setCurrentWidget(self.hourPage[count_id])
        for x in self.dataButtons:
            if x.isChecked():
                x.setChecked(False)
        button_id.setChecked(True)

    def cancelarCompra(self, event, compra = None):
        salas.removeLugar(compra)
        self.stackedWidget.setCurrentWidget(self.page)
        
    def delHorario(self):
        for x in range(len(self.btn)):
            self.btn[x].deleteLater()

    

        
            
        
        

