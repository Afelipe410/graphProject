from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCharts import QChart, QChartView, QScatterSeries, QLineSeries
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPainter, QPen, QColor

class MapView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        # Crear el gráfico
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        
        # Configurar la vista del gráfico
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Agregar la vista al layout
        self.layout.addWidget(self.chart_view)
        
        # Series para diferentes elementos
        self.tanks_series = QScatterSeries()
        self.tanks_series.setName("Tanques")
        self.tanks_series.setMarkerSize(15)
        
        self.districts_series = QScatterSeries()
        self.districts_series.setName("Barrios")
        self.districts_series.setMarkerSize(10)
        
        self.pipes_series = QLineSeries()
        self.pipes_series.setName("Tuberías")
        
        # Agregar series al gráfico
        self.chart.addSeries(self.tanks_series)
        self.chart.addSeries(self.districts_series)
        self.chart.addSeries(self.pipes_series)
        
        # Configurar ejes
        self.chart.createDefaultAxes()
        
        # Establecer el título
        self.chart.setTitle("Red de Distribución de Agua")

    def update_network(self, network):
        """
        Actualiza la visualización con los datos de la red
        """
        # Limpiar series existentes
        self.tanks_series.clear()
        self.districts_series.clear()
        self.pipes_series.clear()
        
        # Agregar tanques
        for tank in network.tanks.values():
            self.tanks_series.append(
                QPointF(tank.coordinates.lng, tank.coordinates.lat)
            )
        
        # Agregar barrios
        for district in network.districts.values():
            self.districts_series.append(
                QPointF(district.coordinates.lng, district.coordinates.lat)
            )
        
        # Agregar tuberías
        for pipe in network.pipes.values():
            # Obtener coordenadas de origen
            from_coord = self._get_component_coordinates(pipe.from_id, network)
            to_coord = self._get_component_coordinates(pipe.to_id, network)
            
            if from_coord and to_coord:
                self.pipes_series.append(
                    QPointF(from_coord[0], from_coord[1])
                )
                self.pipes_series.append(
                    QPointF(to_coord[0], to_coord[1])
                )
        
        # Actualizar ejes
        self.chart.createDefaultAxes()

    def _get_component_coordinates(self, component_id, network):
        """
        Obtiene las coordenadas de un componente (tanque o distrito)
        """
        if component_id in network.tanks:
            component = network.tanks[component_id]
            return (component.coordinates.lng, component.coordinates.lat)
        elif component_id in network.districts:
            component = network.districts[component_id]
            return (component.coordinates.lng, component.coordinates.lat)
        return None