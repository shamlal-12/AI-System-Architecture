"""Event persistence and alert dispatch interface."""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

@dataclass
class EventRecord:
    camera_id: str
    timestamp: datetime
    detections: list
    status: str = "created"

class AlertLogger:
    def __init__(self, destination: str) -> None:
        self.destination = destination

    def log_event(self, event: EventRecord) -> bool:
        """Persist event metadata; return success status."""
        raise NotImplementedError

    def send_alert(self, event: EventRecord) -> Dict[str, Any]:
        """Dispatch an alert and return delivery status details."""
        raise NotImplementedError
