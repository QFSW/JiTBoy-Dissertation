import csv
import sys

path = sys.argv[1]

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            for i, cell in enumerate(row):
                if i > 0:
                    print(' & ', end='')

                row = cell.replace('_', '\_') \
                          .replace('$', '\$')

                print(row, end='')
            print(' \\\\')
