from PySide6.QtWidgets import QApplication

from Screen.cadastro import Cadastro

import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    tela = Cadastro(app)
    tela.janela.show()

    sys.exit(tela.app.exec())