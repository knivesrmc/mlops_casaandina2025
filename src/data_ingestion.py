import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml


logger =get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config=config["data_ingestion"]
        self.bucket_name=self.config["bucket_name"]
        self.file_name= self.config["bucket_file_name"]
        self.train_test_ratio=self.config["train_ratio"]

        os.makedirs(RAW_DIR, exist_ok=True)
        logger.info(f"Ingestion de data iniciada con {self.bucket_name} y archivo es {self.file_name}")
    
    def descarga_csv_desde_gcp(self):
        try:
            
            client=storage.Client()
            bucket=client.bucket(self.bucket_name)

            blob=bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)

            logger.info(f"El archivo CSV ha sido descargado correctamente hacia {RAW_FILE_PATH}")
        except Exception as e:
            logger.error("Error mientras descargaba el archivo csv")
            raise CustomException("Error en descarga de Archivo CSV ", e)
    
    def split_data(self):
        try:
            logger.info("Iniciando proceso de division de data")
            data= pd.read_csv(RAW_FILE_PATH)

            train_data, test_data= train_test_split(data, test_size=1-self.train_test_ratio)

            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)

            logger.info(f"Data de entrenamiento guardada en {TRAIN_FILE_PATH}")
            logger.info(f"Data de Testeo guardada en {TEST_FILE_PATH}")
        except Exception as e:
            logger.error("Error mientras se realizaba la division de la data")
            raise CustomException("Error en la division de la data para testeo y entrenamiento", e)
    
    def run(self):
        #Funcion de ejecucion del run
        try:
            logger.info("Iniciando el proceso de ingesta de data")
            #Comentado--
            #self.descarga_csv_desde_gcp()
            self.split_data()
            logger.info("Finalizacion de ingesta de data")
        except CustomException as ce:
            logger.error(f"CustomException :{str(ce)}")
        finally:
            logger.info("Ingesta de la data Terminada")

if __name__=="__main__":
    data_ingestion=DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()


        






