import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos import merge_instruments, dor1, copy

def datasets():
    x = pd.read_csv("metadata/datasets.csv")
    x.rename(columns={
        "study":"study_name",
        "dataset":"dataset_name",
        "period":"period_name",
        "analysis_unit":"analysis_unit_name",
        "conceptual_dataset":"conceptual_dataset_name",
    }, inplace=True)
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/datasets.csv", index=False)

def variables():
    x = pd.read_csv("metadata/variables.csv")
    x.rename(columns={
        "study":"study_name",
        "dataset":"dataset_name",
        "varname":"variable_name",
        "concept":"concept_name",
    }, inplace=True)
    valid = x.ix[ : , ("study_name", "dataset_name", "variable_name")].duplicated() == False
    x = x.ix[valid]
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/variables.csv", index=False)

def concepts():
    x = pd.read_csv("metadata/concepts.csv")
    x.rename(columns={
        "concept":"concept_name",
    }, inplace=True)
    valid = x.ix[ : , "concept_name"].duplicated() == False
    x = x.ix[valid]
    dor1.lower_all_names(x)
    x.to_csv("ddionrails/concepts.csv", index=False)

def main():
    copy.study()
    concepts()
    datasets()
    variables()
    copy.r2ddi("r2ddi/v31/en", "ddionrails/r2ddi/v31")
    copy.bibtex()

if __name__ == "__main__":
    main()
