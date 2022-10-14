from src.excel import (
    get_empty,
    load_or_create_wb,
    enter_row,
    existing_dates,
    get_or_create_sheet,
)
from src.data import load_data, run_prediction
from src.base import models


def main(filename: str = "records.xlsx", num_ints_predict: int = 5) -> None:
    workbook = load_or_create_wb(filename)

    for model in models:
        df = load_data(model["ticker"])
        last_date = df.date.iloc[-1]
        worksheet = get_or_create_sheet(workbook, model)
        dates = existing_dates(worksheet)
        if last_date in dates:
            continue
        pred_info = run_prediction(df, num_ints_predict, model)

        to_enter = get_empty(worksheet)
        enter_row(worksheet, to_enter, last_date, pred_info, model)

    workbook.save(filename=filename)


if __name__ == "__main__":
    main()
