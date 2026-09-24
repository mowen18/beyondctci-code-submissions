# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Spreadsheet:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mat = [[0] * cols for _ in range(rows)]
    def new(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mat = [[0] * cols for _ in range(rows)]

    def set(self, row, col, value):
        self.mat[row][col] = value

    def get(self, row, col):
        return self.mat[row][col]

    def sort_rows_by_column(self, col):
        self.mat.sort(key = lambda row: row[col])

    def sort_columns_by_row(self, row):
        cols_vals = []
        new_sheet = []
        for i in range(self.cols):
            cols_vals.append((i, self.get(row,i)))
        cols_vals.sort(key=lambda x: x[1])
        for r in range(self.rows):
            new_row = []
            for col, _ in cols_vals:
                new_row.append(self.mat[r][col])
            new_sheet.append(new_row)
        self.mat = new_sheet
            
        
