import pandas as pd


def create_concepts_questions():

    x = pd.read_csv("metadata/questions.csv")
    x.rename(
        columns={
            "study": "study_name",
            "questionnaire": "instrument_name",
            "question": "question_name",
            "concept": "concept_name",
        },
        inplace=True,
    )
    x = x[["study_name", "instrument_name", "question_name", "concept_name"]]
    x.dropna(inplace=True)
    x.to_csv("ddionrails/concepts_questions.csv", index=False)


if __name__ == "__main__":
    create_concepts_questions()
