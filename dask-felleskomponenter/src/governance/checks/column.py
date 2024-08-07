from typing import List
from .common import MetadataError
from src.governance.main import TableMetadata

def check_romlig_representasjonstype(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/romlig-representasjonstype "

    if metadata.romlig_representasjonstype is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     description="🔴 Feil: 'romlig_representasjonstype' mangler i column properties. Type: <romlig_representasjonstype> - gyldige verdier finner du her: " + kodeliste_url, 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'romlig_representasjonstype' = '<<SETT_ROMLIG_REPRESENTASJONSTYPE_HER>>')")
        context.append(error_obj)
    
    return context