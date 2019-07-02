# -*- coding: utf-8 -*-

""" Preprocessing pipeline for soep-core """

import pathlib

from ddi.onrails.repos import dor1, merge_instruments
from ddi.onrails.repos.topics import TopicParser

from convert_r2ddi import Parser as XmlParser
from helpers import add_columns, extract_unique_values, link_to, preprocess
from steps.questions_variables import questions_from_generations
from steps.transformations import preprocess_transformations

STUDY = "soep-core"
VERSION = "v34"

INPUT_DIRECTORY = pathlib.Path("metadata")
LINK_TO_INPUT_DIRECTORY = pathlib.Path("..").joinpath(INPUT_DIRECTORY)
OUTPUT_DIRECTORY = pathlib.Path("ddionrails")


def preprocess_datasets() -> None:
    """ Preprocess datasets
        -------------------

        read from: metadata/datasets.csv

        rename columns:
            - dataset -> name

        lowercase elements in columns:
            - study
            - name
            - analysis_unit
            - conceptual_dataset
            - period

        select subset of columns in specific order:
            - study
            - name
            - label
            - description
            - analysis_unit
            - conceptual_dataset
            - period

        write to: ddionrails/datasets.csv
    """
    DATATYPE_MAPPING = {"period": str}
    RENAME_COLUMNS = {"dataset": "name"}
    UNIQUE_COLUMNS = ["study", "name"]
    LOWERCASE_COLUMNS = [
        "study",
        "name",
        "analysis_unit",
        "conceptual_dataset",
        "period",
    ]
    WANTED_COLUMNS = [
        "study",
        "name",
        "label",
        "description",
        "analysis_unit",
        "conceptual_dataset",
        "period",
    ]
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("datasets.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("datasets.csv"),
        datatype_mapping=DATATYPE_MAPPING,
        rename_columns=RENAME_COLUMNS,
        unique_columns=UNIQUE_COLUMNS,
        lowercase_columns=LOWERCASE_COLUMNS,
        wanted_columns=WANTED_COLUMNS,
    )


def preprocess_variables() -> None:
    """ Preprocess variables
        --------------------

        read from: metadata/variables.csv

        rename columns:
            - study_name -> study
            - dataset_name -> dataset
            - variable_name -> name
            - concept_name -> concept

        drop duplicates rows based on columns:
            - study
            - dataset
            - name

        lowercase elements in columns:
            - name
            - topic

        select subset of columns in specific order:
            - study
            - dataset
            - name
            - concept

        write to: ddionrails/variables.csv
    """
    RENAME_COLUMNS = {
        "study_name": "study",
        "dataset_name": "dataset",
        "variable_name": "name",
        "concept_name": "concept",
    }
    UNIQUE_COLUMNS = ["study", "dataset", "name"]
    LOWERCASE_COLUMNS = ["study", "dataset", "name", "concept"]
    WANTED_COLUMNS = LOWERCASE_COLUMNS
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("variables.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("variables.csv"),
        rename_columns=RENAME_COLUMNS,
        unique_columns=UNIQUE_COLUMNS,
        lowercase_columns=LOWERCASE_COLUMNS,
        wanted_columns=WANTED_COLUMNS,
    )


def preprocess_concepts() -> None:
    """ Preprocess concepts
        -------------------

        read from: metadata/concepts.csv

        drop columns:
            - topic

        rename columns:
            - concept -> name
            - topic_prefix -> topic

        drop duplicates rows based on columns:
            - name

        lowercase elements in columns:
            - name
            - topic

        select subset of columns in specific order:
            - name
            - label
            - label_de
            - topic

        write to: ddionrails/concepts.csv
    """
    DROP_COLUMNS = ["topic"]
    RENAME_COLUMNS = {"concept": "name", "topic_prefix": "topic"}
    UNIQUE_COLUMNS = ["name"]
    LOWERCASE_COLUMNS = ["name", "topic"]
    WANTED_COLUMNS = ["name", "label", "label_de", "topic"]
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("concepts.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("concepts.csv"),
        drop_columns=DROP_COLUMNS,
        rename_columns=RENAME_COLUMNS,
        unique_columns=UNIQUE_COLUMNS,
        lowercase_columns=LOWERCASE_COLUMNS,
        wanted_columns=WANTED_COLUMNS,
    )


def preprocess_instruments() -> None:
    """ Preprocess instruments
        ----------------------

        read from: metadata/questionnaires.csv

        rename columns:
            - questionnaire -> name

        select subset of columns in specific order:
            - study
            - name
            - label
            - label_de
            - description
            - description_de
            - analysis_unit
            - period

        write to: ddionrails/instruments.csv
    """
    RENAME_COLUMNS = {"questionnaire": "name"}
    UNIQUE_COLUMNS = ["study", "name"]
    WANTED_COLUMNS = [
        "study",
        "name",
        "label",
        "label_de",
        "description",
        "description_de",
        "analysis_unit",
        "period",
    ]
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("questionnaires.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("instruments.csv"),
        rename_columns=RENAME_COLUMNS,
        unique_columns=UNIQUE_COLUMNS,
        wanted_columns=WANTED_COLUMNS,
    )


def preprocess_publications() -> None:
    """ Preprocess publications
        -----------------------

        read from: metadata/publications.csv

        rename columns:
            - questionnaire -> instrument

        add "study" column

        select subset of columns in specific order:
            - study
            - name
            - title
            - author
            - year
            - abstract
            - cite
            - sub_type
            - studies
            - url
            - doi

        drop rows with missing values in columns:
            - name

        write to: ddionrails/publications.csv
    """
    DATATYPE_MAPPING = {"name": str}
    UNIQUE_COLUMNS = ["study", "name"]
    WANTED_COLUMNS = [
        "study",
        "name",
        "title",
        "author",
        "year",
        "abstract",
        "cite",
        "sub_type",
        "studies",
        "url",
        "doi",
    ]
    DROP_MISSING_COLUMNS = ["name"]
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("publications.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("publications.csv"),
        datatype_mapping=DATATYPE_MAPPING,
        unique_columns=UNIQUE_COLUMNS,
        wanted_columns=WANTED_COLUMNS,
        drop_missing_columns=DROP_MISSING_COLUMNS,
        add_study_column=STUDY,
    )


def preprocess_concepts_questions() -> None:
    """ Preprocess concepts_questions
        -----------------------------

        read from: metadata/questions.csv

        rename columns:
            - questionnaire -> instrument

        select subset of columns in specific order:
            - study
            - instrument
            - question
            - concept

        drop rows with missing values in columns:
            - concept

        write to: ddionrails/concepts_questions.csv
    """
    RENAME_COLUMNS = {"questionnaire": "instrument"}
    WANTED_COLUMNS = ["study", "instrument", "question", "concept"]
    DROP_MISSING_COLUMNS = ["concept"]
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("questions.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("concepts_questions.csv"),
        rename_columns=RENAME_COLUMNS,
        wanted_columns=WANTED_COLUMNS,
        drop_missing_columns=DROP_MISSING_COLUMNS,
    )


def preprocess_periods() -> None:
    """ Preprocess periods
        ------------------

        read from: metadata/periods.csv

        add "study" column

        select subset of columns in specific order:
            - study
            - name
            - label
            - description
            - definition

        write to: ddionrails/periods.csv
    """
    WANTED_COLUMNS = ["study", "name", "label", "description", "definition"]
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("periods.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("periods.csv"),
        wanted_columns=WANTED_COLUMNS,
        add_study_column=STUDY,
    )


def preprocess_topics() -> None:
    """ Preprocess topics
        -----------------

        read from: metadata/topics.csv

        rename columns:
            - parent_name -> parent

        select subset of columns in specific order:
            - name
            - label
            - label_de
            - parent

        write to: ddionrails/topics.csv
    """
    RENAME_COLUMNS = {"parent_name": "parent"}
    WANTED_COLUMNS = ["name", "label", "label_de", "parent"]
    preprocess(
        in_filename=INPUT_DIRECTORY.joinpath("topics.csv"),
        out_filename=OUTPUT_DIRECTORY.joinpath("topics.csv"),
        rename_columns=RENAME_COLUMNS,
        wanted_columns=WANTED_COLUMNS,
    )


def run():
    # create symlinks
    link_to(
        LINK_TO_INPUT_DIRECTORY.joinpath("study.md"),
        OUTPUT_DIRECTORY.joinpath("study.md"),
    )
    link_to(
        LINK_TO_INPUT_DIRECTORY.joinpath("analysis_units.csv"),
        OUTPUT_DIRECTORY.joinpath("analysis_units.csv"),
    )
    link_to(
        LINK_TO_INPUT_DIRECTORY.joinpath("attachments.csv"),
        OUTPUT_DIRECTORY.joinpath("attachments.csv"),
    )
    link_to(
        LINK_TO_INPUT_DIRECTORY.joinpath("conceptual_datasets.csv"),
        OUTPUT_DIRECTORY.joinpath("conceptual_datasets.csv"),
    )

    # preprocessing
    questions_from_generations(VERSION)
    XmlParser(STUDY, version=VERSION).write_json()
    merge_instruments.main()
    TopicParser(
        topics_input_csv="ddionrails/topics.csv",
        concepts_input_csv="ddionrails/concepts.csv",
    ).to_json()
    preprocess_concepts()
    preprocess_concepts_questions()
    preprocess_datasets()
    preprocess_instruments()
    preprocess_periods()
    preprocess_publications()
    preprocess_variables()
    preprocess_topics()

    transformations = preprocess_transformations(
        INPUT_DIRECTORY.joinpath("generations.csv"), STUDY, VERSION
    )
    transformations.to_csv(
        OUTPUT_DIRECTORY.joinpath("transformations.csv"), index=False
    )


if __name__ == "__main__":
    run()
