import numpy as np

def calculate(list):
    if(len(list) !=9):
      raise ValueError("List must contain nine numbers.")

    ls = np.array(list)
    print(ls)

    mean_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    mean_columns = ([ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()])

    var_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    var_columns = ([ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()])

    std_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    std_columns = ([ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()])

    max_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    max_columns = ([ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()])

    min_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    min_columns = ([ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()])

    sum_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    sum_columns = ([ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()])

    return {
        'mean': [mean_columns, mean_rows, ls.mean()],
        'variance': [var_columns, var_rows, ls.var()],
        'standard deviation': [std_columns, std_rows, ls.std()],
        'max': [max_columns, max_rows, ls.max()],
        'min': [min_columns, min_rows, ls.min()],
        'sum': [sum_columns, sum_rows, ls.sum()]
    }
