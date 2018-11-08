import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos.topics2 import TopicParser
from ddi.onrails.repos.copy import f

def copy_topics_csv():
    x = pd.read_csv("metadata/topics.csv")
    x.rename(columns=dict(
        topic="name",
        parent="parent_name"
    ), inplace=True)
    x.to_csv("ddionrails/topics.csv", index=False)

def main():
    print("[INFO] Test topics converter.")
    copy_topics_csv()
    TopicParser(
        topics_input_csv="ddionrails/topics.csv",
        concepts_input_csv="ddionrails/concepts.csv",
    ).to_json()

if __name__ == "__main__":
    main()
