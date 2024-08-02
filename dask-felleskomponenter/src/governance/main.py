from dataclasses import dataclass, field
from typing import Optional

@dataclass
class TableMetadata:
    catalog: Optional[str] = field(default=None)
    schema: Optional[str] = field(default=None)
    table: Optional[str] = field(default=None)
    owner: Optional[str] = field(default=None)
    origin: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    access_class: Optional[str] = field(default=None)
    valor: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    privacy_considerations: Optional[str] = field(default=None)
    theme: Optional[str] = field(default=None)
    keyword: Optional[str] = field(default=None)    
    epsg_codes: Optional[str] = field(default=None)    
    spatial_representation: Optional[str] = field(default=None)
    usage: Optional[str] = field(default=None)
    concept: Optional[str] = field(default=None)

class Metadata:
    def __init__(self, catalog: str, schema: str, table: str) -> None:
        self.catalog = catalog
        self.schema = schema
        self.table = table
    
    def get_table_metadata(self) -> TableMetadata:
        pass