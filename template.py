import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define project name
project_name = "mlops"

# Define the list of files
list_of_files = [
    # GitHub workflows
    ".github/workflows/.gitkeep",

    # Data files
    "data/olist_customers_dataset.csv",

    # Materializer files
    f"src/{project_name}/materializer/custom_materializer.py",

    # Model files
    f"src/{project_name}/model/__init__.py",
    f"src/{project_name}/model/data_cleaning.py",
    f"src/{project_name}/model/evaluation.py",
    f"src/{project_name}/model/model_dev.py",

    # Pipelines
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/deployment_pipeline.py",
    f"src/{project_name}/pipelines/training_pipeline.py",

    # Utilities
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    # Steps
    f"src/{project_name}/steps/__init__.py",
    f"src/{project_name}/steps/config.py",
    f"src/{project_name}/steps/01_ingest_data.py",
    f"src/{project_name}/steps/02_clean_data.py",
    f"src/{project_name}/steps/03_evaluate_model.py",
    f"src/{project_name}/steps/04_train_model.py",

    # Tests
    f"src/{project_name}/tests/__init__.py",
    f"src/{project_name}/tests/test_data.py",

    # Main scripts
    "run_deployment.py",
    "run_pipeline.py",

    # Configuration and requirements
    "config.yaml",
    "requirements.txt",

    # Streamlit app
    "streamlit_app.py",
]


# Logic to create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # Create empty file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            # Optionally, write placeholder text for specific files
            if filename == "config.yaml":
                f.write("# Configuration file\n")
            elif filename == "requirements.txt":
                f.write("# Add your dependencies here\n")
            # Log the file creation
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")

logging.info("Project structure setup complete.")
