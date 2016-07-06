import os
import re
import pandas as pd

studies = {study : {} for study in os.listdir("import/") }

dataset_re = re.compile(r"^(.*)\.xml$")

for study in studies:
    study_path = "import/" + study + "/r2ddi/"
    versions = os.listdir(study_path)
    for version in versions:
        version_path = study_path + version
        datasets = os.listdir(version_path)
        studies[study][version] = [ dataset_re.sub(r"\1", d) for d in datasets ]

studies

distributions = pd.DataFrame()
datasets_distributions = pd.DataFrame()

for study, versions in studies.items():
    active_version = sorted(versions.keys())[-1]
    for version, datasets in versions.items():
        active = ( version == active_version )
        distributions = distributions.append(pd.DataFrame({
            "study" : study,
            "distribution" : version,
            "active" : active,
        }, index=[version]))
        for dataset in datasets:
            datasets_distributions = datasets_distributions.append(pd.DataFrame({
                "study" : study,
                "distribution" : version,
                "dataset" : dataset,
                "version" : version,
            }, index = [dataset]))
        
distributions.to_csv("output/distributions.csv", index=False)
datasets_distributions.to_csv("output/datasets_distributions.csv", index=False)
