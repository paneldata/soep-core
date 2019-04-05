import pandas as pd
from ddi.onrails.repos import convert_r2ddi, copy, dor1, merge_instruments
from ddi.onrails.repos.topics import TopicParser

from concepts_questions import create_concepts_questions
from questions_variables import questions_from_generations

STUDY = "soep-core"
VERSION = "v34"


def datasets():
    x = pd.read_csv("metadata/datasets.csv")
    x.rename(
        columns={
            "study": "study_name",
            "dataset": "dataset_name",
            "period": "period_name",
            "analysis_unit": "analysis_unit_name",
            "conceptual_dataset": "conceptual_dataset_name",
        },
        inplace=True,
    )
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/datasets.csv", index=False)


def read_variables():
    x = pd.read_csv("metadata/variables.csv")
    x.rename(
        columns={
            "study": "study_name",
            "dataset": "dataset_name",
            "varname": "variable_name",
            "concept": "concept_name",
        },
        inplace=True,
    )
    valid = (
        x.ix[:, ("study_name", "dataset_name", "variable_name")].duplicated() == False
    )
    x = x.ix[valid]
    dor1.lower_all_names(x)
    return x


def variables():
    x = read_variables()
    x.to_csv("ddionrails/variables.csv", index=False)


def concepts():
    x = pd.read_csv("metadata/concepts.csv")
    x.rename(
        columns={"concept": "concept_name", "topic_prefix": "topic_name"}, inplace=True
    )
    valid = x.ix[:, "concept_name"].duplicated() == False
    x = x.ix[valid]
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/concepts.csv", index=False)


def main():
    copy.study()
    concepts()
    datasets()
    variables()
    questions_from_generations(VERSION)
    convert_r2ddi.Parser(STUDY, version=VERSION).write_json()
    merge_instruments.main()
    copy.f("publications.csv")
    copy.f("topics.csv")
    TopicParser(
        topics_input_csv="ddionrails/topics.csv",
        concepts_input_csv="ddionrails/concepts.csv",
    ).to_json()
    create_concepts_questions()


if __name__ == "__main__":
    main()
