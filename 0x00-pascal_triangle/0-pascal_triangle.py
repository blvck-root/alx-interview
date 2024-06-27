#!/usr/bin/python3
"""
Implement Pascal's Triangle
"""

def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to a given number of rows (n).
  It is based on the Binomial Coefficient

  Args:
      n: The number of rows in the Pascal's triangle.

  Returns:
      A list of lists representing the Pascal's triangle. If n <= 0, returns an empty list.
  """
  try:
    triangle = []
    if n <= 0:
      return triangle

    for i in range(1, n + 1):
      C = 1  # C(i, j)
      row = []
      for j in range(1, i + 1):
        row.append(C)
        C = int(C * (i - j) / j)
      triangle.append(row)
    return triangle
  except TypeError:
    print("Input must be an integer")