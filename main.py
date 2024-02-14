from ui_functions import *


if __name__ == "__main__":
    try:
        qt = QApplication(sys.argv)
        app_open = App()
        app_open.show()
        qt.exec_()
    except:
        print('Erro ao abrir aplicativo, verifique a integridade dos arquivos')