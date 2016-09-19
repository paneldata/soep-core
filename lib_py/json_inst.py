import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos import merge_instruments

def main():
    merge_instruments.main(
        #export_json=False,
        #export_yaml=True,
    )

if __name__ == "__main__":
    main()
