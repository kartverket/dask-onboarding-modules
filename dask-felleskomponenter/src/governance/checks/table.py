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
                                     description="🔴 Feil: 'beskrivelse' mangler i table properties. Type: <string>", 
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
                                     description="🔴 Feil: 'tilgangsnivaa' mangler i table properties. Type: <sikkerhetsnivaa> - gyldige verdier finner du her: " + kodeliste_url, 
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
                                     description="🔴 Feil: 'medaljongnivaa' mangler i table properties. Type: <valør> - Gyldige verdier: ['bronse', 'sølv', 'gull']", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'medaljongnivaa' = '<<SETT_MEDALJONGNIVAA_HER>>')")
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
                                     description="🔴 Feil: 'tema' mangler i table properties. Type: <inspiretema> - gyldige verdier finner du her: " + kodeliste_url, 
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
                                     description="🔴 Feil: 'emneord' mangler i table properties. Type: <string>", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'emneord' = '<<SETT_EMNEORD_HER>>')")
        
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
                                     description="🔴 Feil: 'epsg_koder' mangler i table properties. Type: <epsg_koder> - gyldige verdier finner du her: " + kodeliste_url, 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'epsg_koder' = '<<SETT_EPSG_KODER_HER>>')")
        context.append(error_obj)
    
    return context

def check_bruksomraade(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/metadata-kodelister/formal"

    if metadata.bruksomraade is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_bruksomraade, 
                                     description="🔴 Feil: bruksomraade mangler i table properties. Type: <formal> - gyldige verdier finner du her: " + kodeliste_url, 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'bruksomraade' = '<<SETT_BRUKSOMRAADE_HER>>')")
        context.append(error_obj)
    
    return context

def check_begrep(metadata: TableMetadata, context: List) -> List[MetadataError]:
    kodeliste_url = "https://register.geonorge.no/metadata-kodelister/nasjonal-temainndeling"

    if metadata.begrep is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_begrep, 
                                     description="🔴 Feil: 'begrep' mangler i table properties. Type: <nasjonal-temainndeling> - gyldige verdier finner du her: " + kodeliste_url, 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'begrep' = '<<SETT_BEGREP_HER>>')")
        context.append(error_obj)
    
    return context
    
checks_for_valor = {
    "bronse": [check_beskrivelse, check_tilgangsnivaa],
    "sølv": [check_beskrivelse, check_tema, check_emneord, check_tilgangsnivaa, check_epsg_koder, check_bruksomraade],
    "gull":   [check_beskrivelse, check_tema, check_emneord, check_begrep, check_tilgangsnivaa, check_epsg_koder, check_bruksomraade],
}


def validate_table(metadata: TableMetadata) -> List[MetadataError]:
    validation_context = check_medaljongnivaa(metadata, [])

    if len(validation_context) > 0:
        return validation_context
    
    for check in checks_for_valor[metadata.medaljongnivaa]:
        validation_context = check(metadata, validation_context)

    return validation_context
