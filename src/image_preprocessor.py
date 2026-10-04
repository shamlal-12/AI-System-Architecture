"""Frame preprocessing interface."""
import numpy as np

class ImagePreprocessor:
    def __init__(self, target_width: int, target_height: int) -> None:
        self.target_width = target_width
        self.target_height = target_height

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """Return a model-ready image array."""
        raise NotImplementedError
