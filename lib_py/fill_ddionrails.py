import os, sys, re
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

Q_IN_V_RE = re.compile(r'^[a-z]*([0-9]{2})')
I_IN_V_RE = re.compile(r'^([a-z]{1,2})([hp])')

from ddi.onrails.repos import merge_instruments, dor1, copy, convert_r2ddi, topics

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

def read_variables():
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
    return x

def variables():
    x = read_variables()
    x.to_csv("ddionrails/variables.csv", index=False)

def questions_variables():
    x = read_variables()
    x = x[["study_name", "dataset_name", "variable_name"]]
    def determin_question(x):
        try:
            i = Q_IN_V_RE.match(x).group(1)
            if i[0] == "0":
                return i[1]
            else:
                return i
        except:
            return None
    x["question_name"] = x["variable_name"].apply(determin_question)
    def determin_instrument(x):
        year_letters = list("abcdefghijklmnopqrstuvwxyz")
        year_letters += [ "b%s" % x for x in list("abcdefghijklm") ]
        try:
            year_letter = I_IN_V_RE.match(x).group(1)
            p_or_h = I_IN_V_RE.match(x).group(2)
            if p_or_h == "p":
                instrument_type = "pe"
            else:
                instrument_type = "hh"
            year = year_letters.index(year_letter) + 1984
            return "soep-core-%s-%s" % (year, instrument_type)
        except:
            return None
    x["instrument_name"] = x["variable_name"].apply(determin_instrument)
    x.dropna(inplace=True)
    x.to_csv("ddionrails/questions_variables.csv", index=False)

def concepts():
    x = pd.read_csv("metadata/concepts.csv")
    x.rename(columns={
        "concept":"concept_name",
        "topic_prefix":"topic_name",
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
    questions_variables()
    convert_r2ddi.Parser("soep-core", version="v33").write_json()
    merge_instruments.main()
    copy.bibtex(input_format="latin1")
    topics.Topic.import_all()

if __name__ == "__main__":
    main()

