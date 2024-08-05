from dataclasses import dataclass
from typing import Optional


class Errors:
    missing_beskrivelse = "missing-beskrivelse"
    missing_tema = "missing-tema"
    missing_emneord = "missing-emneord"
    missing_begrep = "missing-begrep"
    missing_tilgangsnivaa = "missing-tilgangsnivaa"
    missing_medaljongnivaa = "missing-medaljongnivaa"
    missing_epsg_koder = "missing-epsg_koder"
    missing_romlig_representasjonstype = "missing-romlig_representasjonstype"
    missing_bruksomraade = "missing-bruksomraade"

@dataclass
class MetadataError:
    catalog: str
    schema: str
    table: str
    column: Optional[str]
    error_id: str
    description: str
    solution: Optional[str]
