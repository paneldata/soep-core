import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos import topics

def main():
    print("[INFO] Test topics converter.")
    topics.Topic.import_all()

if __name__ == "__main__":
    main()
