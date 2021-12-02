import pandas as pd
import numpy as np
import pytest


# Можно указывать много фикстур
# @pytest.fixture()
# def load_df():
#     return pd.DataFrame(
#         [["a", "b"], ["c", "d"], ["e", "s"]],
#         columns=["col 1", "col 2"],
#     )


@pytest.mark.main
def test_quantity_rows(load_df):
    assert load_df.shape[0] != 0


@pytest.mark.main
@pytest.mark.show
def test_quantity_columns(load_df):m
    assert load_df.shape[1] == 2


@pytest.mark.second
@pytest.mark.show
def test_find_duplicates(load_df):
    assert load_df.drop_duplicates().shape == load_df.shape


@pytest.mark.second
def test_find_missing_values_in_col1(load_df):
    assert load_df['col 1'].isna().sum() == 0


if __name__ == '__main__':
    print('Start Test')
