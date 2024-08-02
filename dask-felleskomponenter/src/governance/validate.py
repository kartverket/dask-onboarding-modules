from .main import Metadata, TableMetadata
from .checks.table import validate_table

def validate(catalog: str, schema: str, table: str) -> str:
    metadata = Metadata(catalog=catalog, schema=schema, table=table)
    
    table_metadata: TableMetadata = metadata.get_table_metadata()

    return validate_table(table_metadata)