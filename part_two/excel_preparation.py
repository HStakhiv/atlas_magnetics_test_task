import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell, xl_range

from data_calculating import DATA


def create_excel():
    data_len = len(DATA)

    need_to_find = ["Mean", "Median", "Mode", "Standard Deviation"]
    keywords = [
        "AVERAGE",
        "MEDIAN",
        "MODE",
        "STDEVA",
    ]

    with xlsxwriter.Workbook("calculating.xlsx") as workbook:
        worksheet = workbook.add_worksheet("data")

        worksheet.write_row(0, 0, ["№", "Data"])
        worksheet.write_column(data_len + 1, 0, need_to_find)

        worksheet.write_column(1, 0, range(1, data_len + 1))
        worksheet.write_column(1, 1, DATA)

        for i, keyword in enumerate(keywords):
            worksheet.write_formula(
                xl_rowcol_to_cell(data_len + 1 + i, 1),
                f"={keyword}({xl_range(1, 1, data_len, 1)}",
            )


if __name__ == "__main__":
    create_excel()
