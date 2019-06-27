# -*- coding: utf-8 -*-

""" Helper functions for preprocessing pipeline """

import pathlib
from typing import Dict, List

import pandas as pd


def link_to(origin: str, target: str) -> None:
    """ Creates a symlink from origin to target """
    try:
        pathlib.Path(target).symlink_to(pathlib.Path(origin))
    except FileExistsError:
        pass


def add_columns(df: pd.DataFrame, columns: List[str]) -> None:
    """ Add columns to a DataFrame from a list of column names """
    for column in columns:
        df[column] = None


def extract_unique_values(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """ Extract the unique values of a given column name in a DataFrame """
    unique_values = df[column_name].dropna().unique()
    unique_values = pd.DataFrame(unique_values, columns=["name"])
    add_columns(unique_values, ["label", "label_de", "description"])
    unique_values.sort_values(by="name", inplace=True)
    return unique_values


def preprocess(
    in_filename: str,
    out_filename: str,
    datatype_mapping: Dict = None,
    drop_columns: List = None,
    rename_columns: Dict = None,
    unique_columns: List = None,
    lowercase_columns: List = None,
    wanted_columns: List = None,
    drop_missing_columns: List = None,
    add_study_column: str = None,
    new_columns: List = None,
) -> None:

    # Read from disk
    df = pd.read_csv(in_filename, dtype=datatype_mapping)

    # Drop columns
    if drop_columns:
        df.drop(drop_columns, axis=1, inplace=True)

    # rename columns
    if rename_columns:
        df.rename(columns=rename_columns, inplace=True)

    # add a study column
    if add_study_column:
        df["study"] = add_study_column

    # add columns
    if new_columns:
        add_columns(df, new_columns)

    # drop duplicated rows
    df.drop_duplicates(subset=unique_columns, inplace=True)

    # lowercase columns
    if lowercase_columns:
        for column in lowercase_columns:
            df[column] = df[column].str.lower()

    # select subset of dataframe
    if wanted_columns:
        df = df[wanted_columns]

    # drop rows containing missing values
    if drop_missing_columns:
        df.dropna(subset=drop_missing_columns, inplace=True)

    # write to disk
    df.to_csv(out_filename, index=False)
