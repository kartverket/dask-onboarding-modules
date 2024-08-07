from typing import Any, List
from pyspark import SparkContext

from .checks.table import validate_table
from .checks.common import MetadataError, TableMetadata

class Metadata:
    def __init__(self, catalog: str, schema: str, table: str, spark: SparkContext) -> None:
        self.catalog = catalog
        self.schema = schema
        self.table = table
        self.spark = spark
    
    def get_table_metadata(self) -> TableMetadata:
        df_tbltags = self.spark.sql(f"SELECT catalog_name, schema_name, table_name, tag_name, tag_value FROM information_schema.table_tags WHERE catalog_name = '{self.catalog}' AND schema_name = '{self.schema}' AND table_name = '{self.table}';")
        
        keys = { }

        for r in df_tbltags.collect():
            if "delta." in r["key"]: # Ignorer delta spesifikke properties
                continue
            keys[r["tag_name"]] = r["tag_value"]
        
        return TableMetadata(
            catalog=self.catalog, schema=self.schema, table=self.table, 
            beskrivelse=keys["beskrivelse"], tilgangsnivaa=keys["tilgangsnivaa"], 
            medaljongnivaa=keys["medaljongnivaa"], tema=keys["tema"], 
            emneord=keys["emneord"], epsg_koder=keys["epsg_koder"], 
            bruksomraade=keys["bruksomraade"], begrep=keys["begrep"]
        )
    
    def get_table_column_metadata(self) -> Any: # Lage denne typen i annen oppgave
        df = self.spark.sql(f"""
                    SELECT C.*, CT.*
                    FROM system.information_schema.columns AS C 
                    LEFT JOIN system.information_schema.column_tags AS CT
                    ON C.table_catalog = CT.catalog_name 
                        AND C.table_schema = CT.schema_name 
                        AND C.table_name = CT.table_name 
                        AND C.column_name = CT.column_name
                    WHERE C.table_catalog = '{self.catalog}' 
                        AND C.table_schema = '{self.schema}' 
                        AND C.table_name = '{self.table}'
                   """)
        return df

    def validate(self) -> List[MetadataError]:
        table_metadata: TableMetadata = self.get_table_metadata()
        
        return validate_table(table_metadata)