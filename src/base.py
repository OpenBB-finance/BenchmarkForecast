from typing import Tuple, List, Dict, Any
import copy

pred_type = Tuple[List[float], float]

probabalistic = ["expo"]

# Please do NOT change these after first model run, feel free to add as many as you like
# Please use ALL possible arguments to the model so that the excel sheet had all information
expo1 = {
    "model": "expo",
    "name": "expo1",
    "ticker": "AAPL",
    "trend": "A",
    "seasonal": "A",
    "seasonal_periods": 7,
    "dampen": "F",
    "start_window": 0.85,
    "forecast_horizon": 5,
}

models = [expo1]


def get_items(model_dict: Dict[str, Any]) -> Tuple[str, str, Dict[str, Any]]:
    temp_dict = copy.deepcopy(model_dict)
    model = temp_dict.pop("model")
    name = temp_dict.pop("name")
    ticker = temp_dict.pop("ticker")
    return model, f"{name}-{ticker}", temp_dict
