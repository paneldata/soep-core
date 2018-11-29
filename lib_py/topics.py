import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos.topics import TopicParser
from ddi.onrails.repos import copy

def main():
    print("[INFO] Test topics converter.")
    copy.f("topics.csv")
    TopicParser(
        topics_input_csv="ddionrails/topics.csv",
        concepts_input_csv="ddionrails/concepts.csv",
    ).to_json()

if __name__ == "__main__":
    main()
