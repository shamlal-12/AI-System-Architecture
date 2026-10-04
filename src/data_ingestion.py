"""Video source ingestion interface."""
from dataclasses import dataclass
from datetime import datetime
from typing import Iterator, Optional
import numpy as np

@dataclass
class FrameRecord:
    camera_id: str
    timestamp: datetime
    image: np.ndarray

class DataIngestion:
    def __init__(self, source_uri: str, camera_id: str) -> None:
        self.source_uri = source_uri
        self.camera_id = camera_id

    def open(self) -> bool:
        """Open the configured video source."""
        raise NotImplementedError

    def read_frames(self) -> Iterator[FrameRecord]:
        """Yield timestamped frames until the source ends."""
        raise NotImplementedError

    def close(self) -> None:
        """Release stream and associated resources."""
        raise NotImplementedError
