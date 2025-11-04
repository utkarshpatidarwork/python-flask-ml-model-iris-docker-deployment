import pickle
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "model" / "model.pkl"

def load_model(path: Path = MODEL_PATH):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model
