from dataclasses import dataclass, field
from typing import Optional

@dataclass
class TableMetadata:
    catalog: Optional[str] = field(default=None)
    schema: Optional[str] = field(default=None)
    table: Optional[str] = field(default=None)
    beskrivelse: Optional[str] = field(default=None)
    tilgangsnivaa: Optional[str] = field(default=None)
    medaljongnivaa: Optional[str] = field(default=None)
    tema: Optional[str] = field(default=None)
    emneord: Optional[str] = field(default=None)    
    epsg_koder: Optional[str] = field(default=None)    
    romlig_representasjonstype: Optional[str] = field(default=None)
    bruksomraade: Optional[str] = field(default=None)
    begrep: Optional[str] = field(default=None)


class Metadata:
    def __init__(self, catalog: str, schema: str, table: str) -> None:
        self.catalog = catalog
        self.schema = schema
        self.table = table
    
    def get_table_metadata(self) -> TableMetadata:
        pass