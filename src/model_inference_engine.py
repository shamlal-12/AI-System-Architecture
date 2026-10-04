"""Object detection inference interface."""
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np

@dataclass
class Detection:
    class_name: str
    confidence: float
    box: Tuple[float, float, float, float]

class ModelInferenceEngine:
    def __init__(self, model_path: str, confidence_threshold: float = 0.5) -> None:
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold

    def load_model(self) -> None:
        """Load model weights and initialize inference runtime."""
        raise NotImplementedError

    def predict(self, image: np.ndarray) -> List[Detection]:
        """Run inference and return filtered detections."""
        raise NotImplementedError
