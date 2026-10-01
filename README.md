# Student Marks Analysis

A beginner-friendly Python project that analyzes student marks and calculates the **total, average, highest, and lowest** marks. It also identifies which student scored the highest and the lowest.

## Objective

Practice Python data processing and basic statistical calculations using lists and built-in functions.

## Tools Used

- Python 3
- Jupyter Notebook

## Dataset

A manually created dataset of 8 students stored in two Python lists:

| Student | Marks |
|---------|-------|
| Asha    | 78    |
| Ravi    | 85    |
| Meena   | 62    |
| Kiran   | 90    |
| Swetha  | 71    |
| Harsh   | 89    |
| Rupesh  | 70    |
| Akhil   | 65    |

## Approach

1. **Store the data** in two lists: `students` (names) and `marks` (scores).
2. **Total** is calculated using `sum(marks)`.
3. **Average** is calculated as total divided by the number of students: `total / len(marks)`.
4. **Highest and lowest** marks are found using `max(marks)` and `min(marks)`.
5. **Topper and lowest scorer** are found by getting the position of the mark with `marks.index()` and using that position to pick the name from `students`.
6. **Results** are displayed using `print()` and f-strings, with the average rounded to 2 decimal places.

## How to Run

1. Install Python and Jupyter Notebook:
   ```
   pip install notebook
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   jupyter notebook
   ```
4. Open `student_marks_analysis.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Sample Output

```
Total marks: 610
Average marks: 76.25
Highest marks: 90
Lowest marks: 62
Topper: Kiran (90)
Lowest: Meena (62)
```

## Limitations

- If two students tie for the highest or lowest mark, `.index()` returns only the first match.
- The program does not handle an empty list (dividing by zero would cause an error).

## Possible Improvements

- Handle ties and empty lists.
- Read marks from a CSV file instead of typing them manually.
- Use `pandas` and `matplotlib` to analyze larger datasets and plot charts.

## Author

SwethaPulusu

#Live Demo

https://studentmarksanalysis-y2rh5wvpjfptd2qcfxcc8l.streamlit.app/
