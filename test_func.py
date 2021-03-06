import pandas as pd
import numpy as np
import pytest


def load_df():
    return pd.DataFrame(
        [["a", "b"], ["c", "d"], ["e", "s"]],
        columns=["col 1", "col 2"], 
    )


def test_quantity_rows():
    df = load_df()
    assert df.shape[0] != 0


def test_quantity_columns():
    df = load_df()
    assert df.shape[1] == 2


def test_find_duplicates():
    df = load_df()
    assert df.drop_duplicates().shape == df.shape


def test_find_missing_values_in_col1():
    df = load_df()
    assert df['col 1'].isna().sum() == 0


if __name__ == '__main__':
    print('Start Test')
