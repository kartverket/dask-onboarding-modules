from dataclasses import dataclass
from typing import Any, List, Optional

import requests


@dataclass
class MetadataError:
    catalog: str
    schema: str
    table: str
    column: Optional[str]
    description: str
    solution: Optional[str]

def check_codelist_value(kodeliste_url: Optional[str], value: Any, allowed_values: Optional[List[Any]] = None, override_kodeliste_keyword: Optional[str] = None) -> bool:
    if value == None:
        return False

    if allowed_values != None:
        return value in allowed_values
    
    if kodeliste_url == None:
        return value != None

    kodeliste_entry = "codevalue" if override_kodeliste_keyword == None else override_kodeliste_keyword
    values_res = requests.get(kodeliste_url, headers={ "Accept": "application/json" }).json()
    valid_values = list(filter(lambda x: x != None, [x.get(kodeliste_entry, None) for x in values_res["containeditems"]]))

    return value in valid_values
