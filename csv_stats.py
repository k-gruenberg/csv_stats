import argparse
import csv
from collections import defaultdict


def fix_width(s: str, width: int) -> str:
    if len(s) >= width:
        return s
    else:
        return s + (" " * (width - len(s)))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="A Python script printing various statistics about a given CSV file. "
                    "Useful as a starting point for data analysis tasks."
    )

    parser.add_argument(  # (positional argument)
        'PATH_TO_CSV_FILE',
        help="The path to the CSV file to analyze."
    )

    parser.add_argument(
        "--header",
        dest='header',
        action='store_true',
        help="Use this flag when the given CSV file contains a header row at the top."
    )

    parser.add_argument(
        "--delimiter",
        dest='delimiter',
        metavar="CSV_DELIMITER",
        type=str,
        default=",",
        help="Optional: specify a custom CSV delimiter. Default: ',' (comma)."
    )

    parser.add_argument(
        "--quotechar",
        dest='quotechar',
        metavar="CSV_QUOTE_CHAR",
        type=str,
        default='\"',
        help="Optional: specify a custom CSV quote character. Default: '\"' (double quote char)."
    )

    args = parser.parse_args()

    rows: list

    with open(args.PATH_TO_CSV_FILE, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=args.delimiter, quotechar=args.quotechar)
        rows = [row for row in csv_reader]

    if args.header:
        header = rows[0]
        max_header_str_len: int = max(len(h) for h in header)
        header_fixed_width = [fix_width(h, max_header_str_len) for h in header]
        rows = rows[1:]
    else:
        header = None
        header_fixed_width = None

    print("")
    print(f"No. of rows: {len(rows)}")
    print(f"No. of columns: {len(rows[0])}")
    print("")
    print("Duplicate rows:")
    rows_by_count: dict = defaultdict(int)
    for row in rows:
        rows_by_count[tuple(row)] += 1
    idx: int = 0
    for row, count in sorted(rows_by_count.items(), key=lambda itm: itm[1], reverse=True):
        if count > 1:
            idx += 1
            print(f"\t({idx}) {count}x {row}")
    print("")
    print("Rows with missing values:")
    rows_by_missing_value_count: dict = dict()
    for row in rows:
        missing_value_count: int = len([cell for cell in row if cell in ["", "NA", "N/A", "na", "n/a"]])
        rows_by_missing_value_count[tuple(row)] = missing_value_count
    idx = 0
    for row, missing_value_count in sorted(rows_by_missing_value_count.items(), key=lambda itm: itm[1], reverse=True):
        if missing_value_count > 0:
            idx += 1
            if idx > 5:
                print("\t...")
                break
            else:
                print(f"\t({idx}) {missing_value_count} missing: {row}")
    print("")
    print("Columns:")
    for col_idx in range(len(rows[0])):
        column: list = [row[col_idx] for row in rows]
        distinct_values: list = sorted(set(val for val in column))
        col_type: str
        try:
            int_values = [int(val) for val in column]
            float_values = int_values
            col_type = "INT  "
        except ValueError:
            try:
                int_values = None
                float_values = [float(val) for val in column]
                col_type = "FLOAT"
            except ValueError:
                int_values = None
                float_values = None
                col_type = "STR  "
        print(
            f"\t({col_idx + 1:03}) {col_type} " +
            (f"{header_fixed_width[col_idx]} " if header is not None else "") +
            f"{len(distinct_values):7_} distinct values" +  # 7 = for values up to "999_999"
            (f": {', '.join(f'{len([v for v in column if v == val])}x {repr(val)}' for val in distinct_values)}" if len(distinct_values) <= 5 else "") +
            (f": min. {min(float_values):_.2f}, max. {max(float_values):_.2f}, "
             f"{len([f for f in float_values if f < 0]):_} neg. values, "
             f"{len([f for f in float_values if f == 0]):_} zero values, "
             f"{len([f for f in float_values if f > 0]):_} pos. values"
             if col_type in ["FLOAT", "INT  "] and len(distinct_values) > 5 else "")
        )
    print("")


if __name__ == "__main__":
    main()
