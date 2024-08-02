from dataclasses import dataclass
from typing import Optional


class Errors:
    missing_owner = "missing-owner"
    missing_origin = "missing-origin"
    missing_description = "missing-description"

@dataclass
class MetadataError:
    catalog: str
    schema: str
    table: str
    column: Optional[str]
    error_id: str
    description: str
    solution: Optional[str]
