from datetime import date, timedelta
from argparse import ArgumentParser
from csv import DictReader
from apportion import apportion

# Get year.
parser = ArgumentParser()
parser.add_argument('year', type=int)
parser.add_argument('--days', required=False, type=int)
args = parser.parse_args()

# Compute dates and timespan.
begin = date(args.year, 1, 1)
end = date(args.year + 1, 1, 1)
days = args.days or (end - begin).days

# Read in books.
with open('esv_books.csv', newline='') as csvfile:
    rows = [row for row in DictReader(csvfile)]
    titles = [row['book'] for row in rows]
    chapters = [int(row['num_chapters']) for row in rows]
books = len(titles)

# Apportionment.
apportionment = apportion(days, chapters)

# Produce calendar.
current = begin
for i in range(books):
    for j in range(apportionment[i]):
        goal = (j + 1) * chapters[i] // apportionment[i]
        print(current, titles[i], goal)
        current += timedelta(days=1)
