import argparse
import csv
from collections import defaultdict


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

    args = parser.parse_args()

    rows: list

    with open(args.PATH_TO_CSV_FILE, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = [row for row in csv_reader]

    if args.header:
        header = rows[0]
        rows = rows[1:]
    else:
        header = None

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


if __name__ == "__main__":
    main()
