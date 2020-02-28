"""Everything to clean up files in datapackage.json before validation"""
import json
import os
import unittest
from pathlib import Path
from typing import Any, Dict, List, Union
from unittest.mock import mock_open, patch

import pandas


def clean_resources():
    datapackage_path = Path("../metadata")
    resources = get_datapackage_structure()
    for resource in resources:
        resource_dataframe = None
        with open(datapackage_path.joinpath(resource["path"]), "r") as in_file:
            resource_dataframe = pandas.read_csv(in_file)
            resource_dataframe = clean_columns(resource_dataframe, resource["columns"])
        with open(datapackage_path.joinpath(resource["path"]), "w") as out_file:
            out_file.seek(0)
            resource_dataframe.to_csv(out_file, index=False)


def clean_columns(dataframe: pandas.DataFrame, columns: List[str]) -> pandas.DataFrame:
    header: List[str] = list(dataframe.columns)
    filtered_header: List[str] = list()
    for column in columns:
        if column in header:
            filtered_header.append(column)
    return dataframe.loc[:, filtered_header]


def get_datapackage_structure(
    path: Path = Path(__file__)
    .absolute()
    .parent.joinpath("../metadata/datapackage.json"),
) -> List[Dict[str, Union[str, List[str]]]]:
    datapackage: Dict[str, Any]
    with open(path, "r") as file:
        datapackage = json.load(file)

    file_columns = list()
    for resource in datapackage["resources"]:
        processed_resource = dict()
        processed_resource["path"] = path.parent.joinpath(resource["path"])
        processed_resource["columns"] = [
            field["name"] for field in resource["schema"]["fields"]
        ]
        file_columns.append(processed_resource)
    return file_columns


###### Tests #######


class TestColumnFilter(unittest.TestCase):
    def test_column_filter(self):
        expected_columns = ["name", "study", "dataset"]
        extra_columns = ["something", "something_else"]
        dataframe = pandas.DataFrame(columns=extra_columns + expected_columns)
        result = clean_columns(dataframe, expected_columns)
        self.assertEqual(expected_columns, list(result.columns))
        dataframe = pandas.DataFrame(columns=extra_columns + expected_columns[1:])
        result = clean_columns(dataframe, expected_columns)
        self.assertEqual(expected_columns[1:], list(result.columns))


class TestGetDatapackageStructure(unittest.TestCase):
    DATAPACKAGE = {
        "name": "some-study",
        "schema": "tabular-data-package",
        "profile": "tabular-data-package",
        "resources": [
            {
                "path": "analysis_units.csv",
                "profile": "tabular-data-resource",
                "name": "analysis_units",
                "title": "Analysis units",
                "format": "csv",
                "mediatype": "text/csv",
                "encoding": "utf-8",
                "schema": {
                    "fields": [
                        {
                            "name": "name",
                            "title": "Name of the analysis unit",
                            "type": "string",
                            "format": "default",
                            "constraints": {"required": True, "maxLength": 255},
                        },
                        {
                            "name": "label",
                            "title": "Label (English) of the analysis unit",
                            "type": "string",
                            "format": "default",
                            "constraints": {"maxLength": 255},
                        },
                        {
                            "name": "label_de",
                            "title": "Label (German) of the analysis unit",
                            "type": "string",
                            "format": "default",
                            "constraints": {"maxLength": 255},
                        },
                        {
                            "name": "description",
                            "title": "Description of the analysis unit using Markdown",
                            "type": "string",
                            "format": "default",
                        },
                    ],
                    "primaryKey": ["name"],
                },
            },
            {
                "path": "conceptual_datasets.csv",
                "profile": "tabular-data-resource",
                "name": "conceptual_datasets",
                "title": "Conceptual datasets",
                "format": "csv",
                "mediatype": "text/csv",
                "encoding": "utf-8",
                "schema": {
                    "fields": [
                        {
                            "name": "name",
                            "title": "Name of the conceptual dataset",
                            "type": "string",
                            "format": "default",
                            "constraints": {"required": True, "maxLength": 255},
                        },
                        {
                            "name": "label",
                            "title": "Label (English) of the conceptual_dataset",
                            "type": "string",
                            "format": "default",
                            "constraints": {"maxLength": 255},
                        },
                        {
                            "name": "label_de",
                            "title": "Label (German) of the conceptual_dataset",
                            "type": "string",
                            "format": "default",
                            "constraints": {"maxLength": 255},
                        },
                        {
                            "name": "description",
                            "title": "Description of the conceptual_dataset using Markdown",
                            "type": "string",
                            "format": "default",
                        },
                    ],
                    "primaryKey": ["name"],
                },
            },
        ],
    }

    def test_get_datapackage_structure(self):
        expected = [
            {
                "path": "analysis_units.csv",
                "columns": ["name", "label", "label_de", "description"],
            },
            {
                "path": "conceptual_datasets.csv",
                "columns": ["name", "label", "label_de", "description"],
            },
        ]
        with patch(
            "builtins.open", mock_open(read_data=json.dumps(self.DATAPACKAGE))
        ) as patched_input:
            result = get_datapackage_structure(path=Path("/test/file.json"))
            self.assertEqual(expected, result)


if __name__ == "__main__":
    clean_resources()
