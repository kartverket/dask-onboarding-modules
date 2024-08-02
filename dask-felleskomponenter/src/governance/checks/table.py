from typing import List
from src.governance.main import TableMetadata
from .common import MetadataError, Errors

def check_owner(metadata: TableMetadata, context: List) -> List:
    if metadata.owner is None:
        error_obj = MetadataError(catalog=metadata.catalog,
                                     schema=metadata.schema,
                                     table=metadata.table,
                                     column=None,
                                     error_id=Errors.missing_owner,
                                     description="🔴 Error: Owner is missing from table properties",
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'owner' = '<<SET_OWNER_HERE>>')")
        context.append(error_obj)

    return context

def check_origin(metadata: TableMetadata, context: List) -> List:
    if metadata.origin is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_description, 
                                     description="🔴 Error: Origin is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'origin' = '<<SET_ORIGIN_HERE>>')")
        context.append(error_obj)

    return context

def check_description(metadata: TableMetadata, context: List) -> List:
    if metadata.description is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Description is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'description' = '<<SET_DESCRIPTION_HERE>>')")
        context.append(error_obj)
    
    return context

def check_access_class(metadata: TableMetadata, context: List) -> List:
    if metadata.access_class is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Access class is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'access_class' = '<<SET_ACCESS_CLASS_HERE>>')")
        context.append(error_obj)
    
    return context

def check_valor(metadata: TableMetadata, context: List) -> List:
    if metadata.valor is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Valor is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'valor' = '<<SET_VALOR_HERE>>')")
        context.append(error_obj)
    
    return context

def check_title(metadata: TableMetadata, context: List) -> List:
    if metadata.title is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Title is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'title' = '<<SET_TITLE_HERE>>')")
        context.append(error_obj)
    
    return context

def check_privacy_considerations(metadata: TableMetadata, context: List) -> List:
    if metadata.privacy_considerations is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Privacy considerations is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'privacy_considerations' = '<<SET_PRIVACY_CONSIDERATIONS_HERE>>')")
        context.append(error_obj)
    
    return context

def check_theme(metadata: TableMetadata, context: List) -> List:
    if metadata.theme is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Theme is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'theme' = '<<SET_THEME_HERE>>')")
        context.append(error_obj)
    
    return context

def check_keyword(metadata: TableMetadata, context: List) -> List:
    if metadata.keyword is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Keyword is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'keyword' = '<<SET_KEYWORD_HERE>>')")
        context.append(error_obj)
    
    return context


# Spør thom om denne
def check_epsg_codes(metadata: TableMetadata, context: List) -> List:
    if metadata.epsg_codes is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Epsg codes is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'epsg_codes' = '<<SET_EPSG_CODES_HERE>>')")
        context.append(error_obj)
    
    return context

def check_spatial_representation(metadata: TableMetadata, context: List) -> List:
    if metadata.spatial_representation is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Spatial representation is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'spatial_representation' = '<<SET_SPATIAL_REPRESENTATION_HERE>>')")
        context.append(error_obj)
    
    return context

def check_usage(metadata: TableMetadata, context: List) -> List:
    if metadata.usage is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Usage is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'usage' = '<<SET_USAGE_HERE>>')")
        context.append(error_obj)
    
    return context

def check_concept(metadata: TableMetadata, context: List) -> List:
    if metadata.concept is None:
        error_obj = MetadataError(catalog=metadata.catalog, 
                                     schema=metadata.schema, 
                                     table=metadata.table, 
                                     column=None, 
                                     error_id=Errors.missing_origin, 
                                     description="🔴 Error: Concept is missing from table properties", 
                                     solution=f"ALTER TABLE {metadata.catalog}.{metadata.schema}.{metadata.table} SET TBLPROPERTIES ( 'concept' = '<<SET_CONCEPT_HERE>>')")
        context.append(error_obj)
    
    return context
    
checks_for_valor = {
    "bronze": [check_title, check_description, check_access_class, check_privacy_considerations],
    "silver": [check_title, check_description, check_theme, check_keyword, check_access_class, check_epsg_codes, check_spatial_representation, check_usage, check_privacy_considerations],
    "gold":   [check_title, check_description, check_theme, check_keyword, check_concept, check_access_class, check_epsg_codes, check_spatial_representation, check_usage, check_privacy_considerations],
}

def validate_table(metadata: TableMetadata) -> List[str]:
    validation_context = check_valor(metadata, [])

    if len(validation_context) > 0:
        return validation_context
    
    for check in checks_for_valor[metadata.valor]:
        validation_context = check(metadata, validation_context)

    return validation_context
