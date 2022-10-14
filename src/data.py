from typing import Any, Dict
import pandas as pd
from openbb_terminal.api import openbb

from src.base import pred_type, probabalistic, get_items


def load_data(ticker: str) -> pd.DataFrame:
    df = openbb.stocks.load("AAPL")
    df.columns = [x.lower() for x in df.columns]
    df = df.reset_index()
    return df


def run_prediction(df: pd.DataFrame, num_days: int, info: Dict[str, Any]) -> pred_type:
    the_model, _, temp_dict = get_items(info)
    (ticker_series, historical_fcast, predicted_values, precision, _model,) = getattr(
        openbb.forecast, the_model
    )(df, **temp_dict)
    if the_model in probabalistic:
        preds_df = predicted_values.quantile_df().head(num_days)
    else:
        preds_df = predicted_values.head(num_days)
    vals = [x[0] for x in preds_df.values]
    return vals, precision
