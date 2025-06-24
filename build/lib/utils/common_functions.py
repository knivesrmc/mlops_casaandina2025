import os
import pandas
from src.logger import get_logger
from src.custom_exception  import CustomException
import yaml
import pandas as pd

logger= get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Archivo no se encuentra en la ruta")
        with open(file_path,"r") as yaml_file:
            config= yaml.safe_load(yaml_file)
            logger.info("Lectura correcta del archivo YAML")
            return config
    except Exception as e:
        logger.error("Error Mientras se lee el archivo YAML")
        raise CustomException("Error en lectura del archivo YAML", e)
def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)