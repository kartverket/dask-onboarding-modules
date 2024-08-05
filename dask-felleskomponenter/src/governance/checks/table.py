from typing import List
from src.governance.main import TableMetadata
from .common import MetadataError, Errors

def check_beskrivelse(metadata: TableMetadata, context: List) -> List[MetadataError]:
    if metadata.beskrivelse is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_beskrivelse, 
                                     description="🔴 Feil: 'beskrivelse' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'beskrivelse' = '<<SETT_BESKRIVELSE_HER>>')")
        context.append(error_obj)
    
    return context

def check_tilgangsnivaa(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/sikkerhetsniva"
    
    if metadata.tilgangsnivaa is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_tilgangsnivaa, 
                                     description="🔴 Feil: 'tilgangsnivaa' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'tilgangsnivaa' = '<<SETT_TILGANGSNIVAA_HER>>')")
        context.append(error_obj)
    
    return context

def check_medaljongnivaa(metadata: TableMetadata, context: List) -> List[MetadataError]:
    valid_values = ["bronse", "sølv", "gull"]

    if metadata.medaljongnivaa is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_medaljongnivaa, 
                                     description="🔴 Feil: 'medaljongnivaa' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'medaljongnivaa' = '<<SETT_MEDALJONGNIVAA_HER>>')")
        context.append(error_obj)
    
    return context

def check_bruksvilkaar(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/formal"
    
    if metadata.privacy_considerations is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Feil: 'bruksvilkaar' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'privacy_considerations' = '<<SETT_PRIVACY_CONSIDERATIONS_HER>>')")
        context.append(error_obj)
    
    return context

def check_tema(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/inspiretema"
    if metadata.tema is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_tema, 
                                     description="🔴 Feil: 'tema' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'tema' = '<<SETT_TEMA_HER>>')")
        context.append(error_obj)
    
    return context

def check_emneord(metadata: TableMetadata, context: List) -> List[MetadataError]:
    if metadata.emneord is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_emneord, 
                                     description="🔴 Feil: 'emneord' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'emneord' = '<<SETT_emneord_HER>>')")
        
        context.append(error_obj)
    
    return context


# Spør thom om denne
def check_epsg_koder(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/epsg-koder"

    if metadata.epsg_koder is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_epsg_koder, 
                                     description="🔴 Feil: 'epsg_koder' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'epsg_koder' = '<<SETT_EPSG_KODER_HER>>')")
        context.append(error_obj)
    
    return context

def check_romlig_representasjonstype(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/api/register/romlig-representasjonstype "

    if metadata.romlig_representasjonstype is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.romlig_representasjonstype, 
                                     description="🔴 Feil: 'romlig_representasjonstype' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'romlig_representasjonstype' = '<<SETT_ROMLIG_REPRESENTASJONSTYPE_HER>>')")
        context.append(error_obj)
    
    return context

def check_bruksomraade(metadata: TableMetadata, context: List) -> List[MetadataError]:
    if metadata.bruksomraade is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.bruksomraade, 
                                     description="🔴 Feil: bruksomraade mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'bruksomraade' = '<<SETT_BRUKSOMRAADE_HER>>')")
        context.append(error_obj)
    
    return context

def check_begrep(metadata: TableMetadata, context: List) -> List[MetadataError]:
    if metadata.begrep is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_begrep, 
                                     description="🔴 Feil: 'begrep' mangler i table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'begrep' = '<<SETT_BEGREP_HER>>')")
        context.append(error_obj)
    
    return context
    
checks_for_valor = {
    "bronze": [check_beskrivelse, check_tilgangsnivaa],
    "silver": [check_beskrivelse, check_tema, check_emneord, check_tilgangsnivaa, check_epsg_koder, check_romlig_representasjonstype, check_bruksomraade],
    "gold":   [check_beskrivelse, check_tema, check_emneord, check_begrep, check_tilgangsnivaa, check_epsg_koder, check_romlig_representasjonstype, check_bruksomraade],
}


def validate_table(metadata: TableMetadata) -> List[MetadataError]:
    validation_context = check_medaljongnivaa(metadata, [])

    if len(validation_context) > 0:
        return validation_context
    
    for check in checks_for_valor[metadata.medaljongnivaa]:
        validation_context = check(metadata, validation_context)

    return validation_context
