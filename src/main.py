import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from core.network import Network

def main():
    app = QApplication(sys.argv)
    network = Network()
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()