import csv

def parse_csv(csv_file):
    intervals = []     #This will hold all the intervals with start and end times
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = []
        i = 0
        for row in csv_reader:
            i += 1
            if any(cell.strip() for cell in row):  # If a row is empty, silently skip
                if row[0].strip().startswith('#'): # If a row is a comment row, silently skip
                    continue
                if len(row) < 2 or len(row) > 3: # If a row isn't in 2 or 3 columns, warn and skip
                    print(f"Warning: Row {i} has {len(row)} columns (expected 2 or 3). Skipping this row.")
                    continue
                rows.append(row)

        if not rows: # Raise an error if the csv file does not have interval data
            raise ValueError('CSV File is empty')

        # A set will contain the unique values. We can use this to ensure we have only 2 values or 3 values in each row
        column_count = set(len(row) for row in rows)
        if len(column_count) != 1:
            raise ValueError("Inconsistency Detected: All rows must be either 2 (unweighted) or 3 (weighted).")

        # If each row has 2 columns, it's just start and end time
        if column_count == {2}:
            intervals = [(int(row[0]), int(row[1])) for row in rows] # Add in each interval with start and end time to 'intervals'
            is_weighted = False
        else:
            intervals = [(int(row[0]), int(row[1]), int(row[2])) for row in rows] # Add in each interval with start, end time, and weight to 'intervals'
            is_weighted = True

    return intervals, is_weighted