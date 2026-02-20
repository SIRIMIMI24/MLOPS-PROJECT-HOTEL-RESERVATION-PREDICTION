from src.data_ingestion import DataIngestion
from src.data_processing import DataProcessor
from src.model_training import ModelTraining
from utils.common_functions import read_yaml
from config.paths_config import *


if __name__=="__main__":
    ### 1. Data Ingestion

    data_ingestion = DataIngestion(
        dataset_name=DATASET_NAME,
        target_dir=TARGET_DIR,
        config=read_yaml(CONFIG_PATH)
    )
    data_ingestion.initiate_data_ingestion()
    data_ingestion.split_data()

    ### 2. Data Processing

    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()

    ### 3. Model Training

    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    trainer.run()