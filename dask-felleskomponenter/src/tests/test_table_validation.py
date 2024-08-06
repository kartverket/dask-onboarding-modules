from typing import Any
import unittest
from unittest.mock import MagicMock

from src.governance.main import Metadata, TableMetadata

import json

def read_file(filepath: str):
    with open(filepath, 'r') as file:
        gold_mock_json_data = json.load(file)

        return gold_mock_json_data


class TestValidateTable(unittest.TestCase):
    
    def test_validate_calls_get_metadata_with_correct_arguments(self):
        # Arrange
        gold_mock_json_data = read_file("example_table_metadata_gold.json")
        Metadata.get_table_metadata = MagicMock(return_value=TableMetadata(**gold_mock_json_data))
        metadata = Metadata("catalog", "schema", "table", None)

        # Act
        metadata.validate()

        # Assert
        Metadata.get_table_metadata.assert_any_call()

    def test_validate_succeeds_with_correct_set_of_gold_metadata(self):
        # Arrange
        gold_mock_json_data = read_file("example_table_metadata_gold.json")
        Metadata.get_table_metadata = MagicMock(return_value=TableMetadata(**gold_mock_json_data))
        metadata = Metadata("catalog", "schema", "table", None)

        # Act
        result = metadata.validate()

        # Assert
        self.assertListEqual(result, [])

