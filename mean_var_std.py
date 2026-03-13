import numpy as np




def calculate(numbers):
  if len(numbers) != 9:
    raise ValueError("List must contain nine numbers.")



  matrix = np.array(numbers).reshape(3,3)

  mean_col = np.mean(matrix, axis=0).tolist()
  mean_row = np.mean(matrix, axis=1).tolist()
  mean_all = np.mean(matrix).tolist()
  var_col = np.var(matrix, axis=0).tolist()
  var_row = np.var(matrix, axis=1).tolist()
  var_all = np.var(matrix).tolist()
  std_col = np.std(matrix, axis=0).tolist()
  std_row = np.std(matrix, axis=1).tolist()
  std_all = np.std(matrix).tolist()
  max_col = np.max(matrix, axis=0).tolist()
  max_row = np.max(matrix, axis=1).tolist()
  max_all = np.max(matrix).tolist()
  min_col = np.min(matrix, axis=0).tolist()
  min_row = np.min(matrix, axis=1).tolist()
  min_all = np.min(matrix).tolist()
  sum_col = np.sum(matrix, axis=0).tolist()
  sum_row = np.sum(matrix, axis=1).tolist()
  sum_all = np.sum(matrix).tolist()
  calculations = {
        'mean': [mean_col, mean_row, mean_all],
        'variance': [var_col, var_row, var_all],
        'standard deviation': [std_col, std_row, std_all],
        'max': [max_col, max_row, max_all],
        'min': [min_col, min_row, min_all],
        'sum': [sum_col, sum_row, sum_all]
    }

  return calculations
