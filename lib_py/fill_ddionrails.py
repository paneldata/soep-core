import pathlib
import shutil
from collections import OrderedDict

import pandas
from ddi.onrails.repos import merge_instruments
from ddi.onrails.repos.topics import TopicParser

from concepts_questions import create_concepts_questions
from questions_variables import questions_from_generations
from transformations import preprocess_transformations

STUDY = "soep-core"
VERSION = "v35"

INPUT_DIRECTORY = pathlib.Path("metadata")
OUTPUT_DIRECTORY = pathlib.Path("ddionrails")


def datasets():
    _datasets = pandas.read_csv("metadata/datasets.csv")
    columns = OrderedDict(
        [
            ("study", "study_name"),
            ("dataset", "dataset_name"),
            ("period", "period_name"),
            ("analysis_unit", "analysis_unit_name"),
            ("conceptual_dataset", "conceptual_dataset_name"),
        ]
    )
    _datasets.rename(
        columns=columns, inplace=True,
    )
    _datasets.rename(columns={"name": "dataset_name"}, inplace=True)
    _datasets.to_csv("ddionrails/datasets.csv", index=False)


def read_variables():
    _variables = pandas.read_csv("metadata/variables.csv")
    columns = OrderedDict(
        [
            ("study", "study_name"),
            ("dataset", "dataset_name"),
            ("variable", "variable_name"),
            ("concept", "concept_name"),
            ("description", "description"),
        ]
    )
    _variables.rename(
        columns=columns, inplace=True,
    )
    _variables.rename(columns={"name": "variable_name"}, inplace=True)
    _variables = _variables.loc[:, list(columns.values())]
    return _variables.drop_duplicates()


def variables():
    variables = read_variables()
    variables.to_csv("ddionrails/variables.csv", index=False)


def concepts():
    _concepts = pandas.read_csv("metadata/concepts.csv")
    _concepts.rename(
        columns={"concept": "name", "topic_prefix": "topic_name"}, inplace=True
    )
    _concepts.drop_duplicates("name")
    _concepts.to_csv("ddionrails/concepts.csv", index=False)


def main():
    concepts()
    datasets()
    variables()
    questions_from_generations(VERSION)
    merge_instruments.main()
    TopicParser(
        topics_input_csv="ddionrails/topics.csv",
        concepts_input_csv="ddionrails/concepts.csv",
    ).to_json()
    create_concepts_questions()
    shutil.copy("metadata/analysis_units.csv", "ddionrails/analysis_units.csv")
    shutil.copy("metadata/conceptual_datasets.csv", "ddionrails/conceptual_datasets.csv")
    shutil.copy("metadata/periods.csv", "ddionrails/periods.csv")
    transformations = preprocess_transformations(
        INPUT_DIRECTORY.joinpath("generations.csv"), STUDY, VERSION
    )
    transformations.to_csv(OUTPUT_DIRECTORY.joinpath("transformations.csv"), index=False)


if __name__ == "__main__":
    main()
