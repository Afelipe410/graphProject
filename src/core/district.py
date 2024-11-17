from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Coordinates:
    lat: float
    lng: float

    def to_dict(self) -> Dict[str, float]:
        return {
            'lat': self.lat,
            'lng': self.lng
        }

    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> 'Coordinates':
        return cls(
            lat=data.get('lat', 0.0),
            lng=data.get('lng', 0.0)
        )

@dataclass
class Demand:
    daily_average: float
    peak_hour: float   

    def to_dict(self) -> Dict[str, float]:
        return {
            'daily_average': self.daily_average,
            'peak_hour': self.peak_hour
        }

    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> 'Demand':
        return cls(
            daily_average=data.get('daily_average', 0.0),
            peak_hour=data.get('peak_hour', 0.0)
        )

class District:
    def __init__(self, id: str, name: str, coordinates: Coordinates, 
                 demand: Demand, population: int):
        self.id = id
        self.name = name
        self.coordinates = coordinates
        self.demand = demand
        self.population = population

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'District':
        return cls(
            id=data['id'],
            name=data['name'],
            coordinates=Coordinates.from_dict(data['coordinates']),
            demand=Demand.from_dict(data['demand']),
            population=data['population']
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'coordinates': self.coordinates.to_dict(),
            'demand': self.demand.to_dict(),
            'population': self.population
        }

    def calculate_current_demand(self, hour: int) -> float:

        peak_hours = {6, 7, 8, 9, 18, 19, 20, 21}
        if hour in peak_hours:
            return self.demand.peak_hour
        return self.demand.daily_average / 24