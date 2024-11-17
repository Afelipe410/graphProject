from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, QPushButton, 
                           QLabel, QComboBox, QSpinBox, QFormLayout)

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        
        # Crear secciones del panel
        self._create_network_controls()
        self._create_simulation_controls()
        self._create_analysis_controls()
        
        # Agregar espacio expandible al final
        self.layout.addStretch()

    def _create_network_controls(self):
        group = QGroupBox("Control de Red")
        layout = QVBoxLayout()
        
        # Botones para gestión de componentes
        btn_add_tank = QPushButton("Agregar Tanque")
        btn_add_district = QPushButton("Agregar Barrio")
        btn_add_pipe = QPushButton("Agregar Tubería")
        
        layout.addWidget(btn_add_tank)
        layout.addWidget(btn_add_district)
        layout.addWidget(btn_add_pipe)
        
        group.setLayout(layout)
        self.layout.addWidget(group)

    def _create_simulation_controls(self):
        group = QGroupBox("Control de Simulación")
        layout = QFormLayout()
        
        # Controles de simulación
        self.sim_speed = QSpinBox()
        self.sim_speed.setRange(1, 10)
        self.sim_speed.setValue(1)
        
        self.obstruction_level = QSpinBox()
        self.obstruction_level.setRange(0, 100)
        self.obstruction_level.setSuffix("%")
        
        self.selected_pipe = QComboBox()
        self.selected_pipe.addItem("Seleccionar tubería...")
        
        # Agregar controles al layout
        layout.addRow("Velocidad:", self.sim_speed)
        layout.addRow("Obstrucción:", self.obstruction_level)
        layout.addRow("Tubería:", self.selected_pipe)
        
        # Botones de control
        btn_apply = QPushButton("Aplicar Cambios")
        layout.addRow(btn_apply)
        
        group.setLayout(layout)
        self.layout.addWidget(group)

    def _create_analysis_controls(self):
        group = QGroupBox("Análisis")
        layout = QVBoxLayout()
        
        # Botones para análisis
        btn_optimize = QPushButton("Optimizar Red")
        btn_find_critical = QPushButton("Puntos Críticos")
        btn_suggest_tanks = QPushButton("Sugerir Nuevos Tanques")
        
        layout.addWidget(btn_optimize)
        layout.addWidget(btn_find_critical)
        layout.addWidget(btn_suggest_tanks)
        
        group.setLayout(layout)
        self.layout.addWidget(group)