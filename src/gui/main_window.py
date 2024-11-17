from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QPushButton, QLabel, QToolBar, QStatusBar, QDockWidget)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from .map_view import mapView
from .control_panel import ControlPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Distribución de Agua")
        self.setMinimumSize(1200, 800)
        
        # Configurar la interfaz principal
        self._create_toolbar()
        self._create_status_bar()
        self._create_central_widget()
        self._create_dock_widgets()
        
        # Inicializar el estado
        self.statusBar().showMessage("Sistema listo")

    def _create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(32, 32))
        
        # Acciones del toolbar
        self.action_new = QAction("Nuevo", self)
        self.action_new.setStatusTip("Crear nueva red")
        toolbar.addAction(self.action_new)
        
        self.action_load = QAction("Cargar", self)
        self.action_load.setStatusTip("Cargar red existente")
        toolbar.addAction(self.action_load)
        
        self.action_save = QAction("Guardar", self)
        self.action_save.setStatusTip("Guardar red actual")
        toolbar.addAction(self.action_save)
        
        toolbar.addSeparator()
        
        self.action_simulation = QAction("Simulación", self)
        self.action_simulation.setStatusTip("Iniciar/Detener simulación")
        self.action_simulation.setCheckable(True)
        toolbar.addAction(self.action_simulation)
        
        self.addToolBar(toolbar)

    def _create_status_bar(self):
        status = QStatusBar()
        self.setStatusBar(status)

    def _create_central_widget(self):
        # Widget central que contendrá el mapa
        self.map_view = mapView()
        self.setCentralWidget(self.map_view)

    def _create_dock_widgets(self):
        # Panel de control (derecha)
        control_dock = QDockWidget("Panel de Control", self)
        control_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.control_panel = ControlPanel()
        control_dock.setWidget(self.control_panel)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, control_dock)
        
        # Historial (abajo)
        history_dock = QDockWidget("Historial", self)
        history_dock.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea)
        history_widget = QWidget()
        history_layout = QVBoxLayout(history_widget)
        history_layout.addWidget(QLabel("Historial de eventos"))
        history_dock.setWidget(history_widget)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, history_dock)