import sys
from pathlib import Path

class AutoImporter:
    def __init__(self, base_dir=None):
        """
        Constructor de la clase AutoImporter.
        Agrega todos los subdirectorios del directorio base a sys.path.
        
        Args:
            base_dir (str): Ruta al directorio base. Si no se proporciona, se utiliza el directorio actual.
        """
        if base_dir is None:
            base_dir = Path.cwd()
        else:
            base_dir = Path(base_dir).resolve()
        
        self.add_to_sys_path(base_dir)
    
    def add_to_sys_path(self, base_dir):
        """
        Recorre recursivamente todos los subdirectorios del directorio base y los añade a sys.path.
        
        Args:
            base_dir (Path): Directorio base desde el cual se añaden los subdirectorios.
        """
        for subdir in base_dir.rglob("*"):
            if subdir.is_dir() and str(subdir) not in sys.path:
                sys.path.append(str(subdir))
