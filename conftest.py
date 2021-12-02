import pandas as pd
import numpy as np
import pytest


@pytest.fixture(scope='session')
def load_df():
    """load sourse df"""
    return pd.DataFrame(
        # [["a", "b"], ["c", "d"], ["e", "s"], ["e", "s"], [np.nan, 1]],
        [["a", "b"], ["c", "d"], ["e", "s"]],
        columns=["col 1", "col 2"],
    )
