import csv
import numpy as np
import pandas as pd
import logging as l

l.basicConfig(level=l.INFO)
l.info("START")

##
# Set file names
#
l.info("Set file names")

system_files = {
  "con_in":"input/concepts-v30.csv",
  "con_out":"output/soep-core/concepts.csv",
  "cdat_in":"input/conceptual_datasets-v30.csv",
  "cdat_out":"output/soep-core/conceptual_datasets.csv",
}

core_files = {
  "var_in":"input/soepcore/variables-v30.csv",
  "var_out":"output/soep-core/logical_variables.csv",
  "dat_in":"input/soepcore/datasets-v30.csv",
  "dat_out":"output/soep-core/logical_datasets.csv",
}

long_files = {
  "var_in":"input/soeplong/variables-v30.csv",
  "var_out":"output/soep-long/logical_variables.csv",
  "dat_in":"input/soeplong/datasets-v30.csv",
  "dat_out":"output/soep-long/logical_datasets.csv",
  "gen_in":"input/soeplong/generations-v30.csv",
  "gen_out":"output/soep-long/generations.csv",
  "gen_old":"input/soep-long-old/generations.csv",
}

##
# Processing concepts
#
l.info("Procssing concepts")

concepts = pd.read_csv(system_files["con_in"])
concepts = concepts.drop(["topic", "label_old", "label_de_old"], 1)
concepts.rename(columns={"topic_prefix":"topic"}, inplace=True)
concepts.to_csv(system_files["con_out"], index=False)

##
# Processing conceptual_datasets
#
l.warning("Conceptual datasets are missing")

conceptual_datasets = pd.read_csv(system_files["cdat_in"])
conceptual_datasets.to_csv(system_files["cdat_out"], index=False)

##
# Processing core variables
#
l.info("Processing core variables")

core_variables = pd.read_csv(core_files["var_in"])
core_variables.rename(columns={"varname":"variable"}, inplace=True)
column_list = ['study', 'dataset', 'variable', 'concept']
core_variables[column_list].to_csv(core_files["var_out"], index=False)

##
# Processing core datasets
#
l.info("Processing core datasets")

core_datasets = pd.read_csv(core_files["dat_in"])
core_datasets.to_csv(core_files["dat_out"], index=False)

##
# Processing long variables
#
l.info("Processing long variables")

long_variables = pd.read_csv(long_files["var_in"])
long_variables.rename(columns={"varname":"variable", "recname":"dataset"},
    inplace=True)
column_list = ['study', 'dataset', 'variable', 'concept', 'description',
    'description_long', 'boost']
long_variables[column_list].to_csv(long_files["var_out"], index=False)

##
# Processing long datasets
#
l.info("Processing long datasets")

long_datasets = pd.read_csv(long_files["dat_in"])
long_datasets.to_csv(long_files["dat_out"], index=False)

##
# Processing long generations
#
l.info("Processing long generations")

gen_new = pd.read_csv(long_files["gen_in"])
gen_new["input_version"] = "v30"
gen_new["output_version"] = "v30"

gen_old = pd.read_csv(long_files["gen_old"])

long_generations = gen_old.append(gen_new)
long_generations.to_csv(long_files["gen_out"], index=False)

l.warning("Distributions and datasets_distributions for **long** are missing.")
l.warning("Distributions and datasets_distributions for **core** are missing.")
l.warning("periods_variables.csv???")

l.info("END")
