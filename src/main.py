import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import mainWindow
from core.network import network

def main():
    app = QApplication(sys.argv)
    network = network()
    
    window = mainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()