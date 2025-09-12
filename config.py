from pathlib import Path

# Define project root
PROJECT_ROOT = Path(__file__).resolve().parent

# Data paths
RAW_DATA = PROJECT_ROOT / "data" / "dog_harness_data.csv"
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Model paths
MODELS_DIR = PROJECT_ROOT / "models"

# Notebook path (optional, just for reference)
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
