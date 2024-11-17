from typing import Dict, List, Optional
from .tank import Tank
from .pipe import Pipe
from .district import District
import json

class Network:
    def __init__(self):
        self.districts: Dict[str, District] = {}
        self.tanks: Dict[str, Tank] = {}
        self.pipes: Dict[str, Pipe] = {}
        self.version: str = "1.0"
        self.last_updated: str = ""

    def load_from_json(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
            network_data = data.get('network', {})
            
            self.version = network_data.get('version', '1.0')
            self.last_updated = network_data.get('last_updated', '')
            
            for district_data in network_data.get('districts', []):
                district = District.from_dict(district_data)
                self.districts[district.id] = district
                
            for tank_data in network_data.get('tanks', []):
                tank = Tank.from_dict(tank_data)
                self.tanks[tank.id] = tank
                
            for pipe_data in network_data.get('pipes', []):
                pipe = Pipe.from_dict(pipe_data)
                self.pipes[pipe.id] = pipe
                
            return True
            
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {str(e)}")
            return False

    def save_to_json(self, file_path: str) -> bool:
     
        try:
            network_data = {
                'network': {
                    'version': self.version,
                    'last_updated': self.last_updated,
                    'districts': [district.to_dict() for district in self.districts.values()],
                    'tanks': [tank.to_dict() for tank in self.tanks.values()],
                    'pipes': [pipe.to_dict() for pipe in self.pipes.values()]
                }
            }
            
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(network_data, file, indent=2)
                
            return True
            
        except Exception as e:
            print(f"Error al guardar el archivo JSON: {str(e)}")
            return False

    def validate_network(self) -> List[str]:
        
        errors = []
        
        for pipe_id, pipe in self.pipes.items():
            if pipe.from_id not in self.tanks and pipe.from_id not in self.districts:
                errors.append(f"Tubería {pipe_id}: Origen {pipe.from_id} no existe")
            
            if pipe.to_id not in self.tanks and pipe.to_id not in self.districts:
                errors.append(f"Tubería {pipe_id}: Destino {pipe.to_id} no existe")
        
        for district_id, district in self.districts.items():
            has_connection = any(
                pipe.to_id == district_id or pipe.from_id == district_id
                for pipe in self.pipes.values()
            )
            if not has_connection:
                errors.append(f"Distrito {district_id} no tiene conexiones")
        
        return errors

    def find_path(self, from_id: str, to_id: str) -> Optional[List[str]]:
        visited = set()
        path = []
        
        def dfs(current_id: str) -> bool:
            if current_id == to_id:
                return True
                
            visited.add(current_id)
            
            for pipe_id, pipe in self.pipes.items():
                next_id = None
                if pipe.from_id == current_id and pipe.to_id not in visited:
                    next_id = pipe.to_id
                elif pipe.to_id == current_id and pipe.from_id not in visited:
                    next_id = pipe.from_id
                    
                if next_id and next_id not in visited:
                    path.append(pipe_id)
                    if dfs(next_id):
                        return True
                    path.pop()
                    
            return False
        
        if dfs(from_id):
            return path
        return None