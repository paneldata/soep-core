import os
import pandas as pd

def lower_all_names(x):
    def lower_x(x):
        try:
            return x.lower()
        except:
            return x
    names = [key for key in x.keys() if "_name" in key]
    x.ix[ : , names] = x.ix[ : , names].applymap(lower_x)

def datasets():
    x = pd.read_csv("metadata/logical_datasets.csv")
    x.rename(columns={
        "study":"study_name",
        "dataset":"dataset_name",
        "period":"period_name",
        "analysis_unit":"analysis_unit_name",
        "conceptual_dataset":"conceptual_dataset_name",
    }, inplace=True)
    lower_all_names(x)
    x.to_csv("ddionrails/datasets.csv", index=False)

def variables():
    x = pd.read_csv("metadata/logical_variables.csv")
    x.rename(columns={
        "study":"study_name",
        "dataset":"dataset_name",
        "variable":"variable_name",
        "concept":"concept_name",
    }, inplace=True)
    valid = x.ix[ : , ("study_name", "dataset_name", "variable_name")].duplicated() == False
    x = x.ix[valid]
    lower_all_names(x)
    x.to_csv("ddionrails/variables.csv", index=False)

def bibtex():
    os.system("cp metadata/bibtex.bib ddionrails")

def study():
    os.system("cp metadata/study.md ddionrails")

def r2ddi():
    os.system("""
        rm -r ddionrails/r2ddi
        mkdir -p ddionrails/r2ddi/v31
        cp -r r2ddi/v31/en ddionrails/r2ddi/v31
    """)

def main():
    study()
    datasets()
    variables()
    r2ddi()
    bibtex()

if __name__ == "__main__":
    main()
