import numpy as np

def calculate(list):
  #convert the list into a 3x3 matrix
  array = np.reshape(list, (3,3))

  #return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
  mean_1 = np.mean(array, axis=0)
  mean_2 = np.mean(array, axis=1)
  mean_f = np.mean(array.flatten())

  variance_1 = np.var(array,axis = 0)
  variance_2 = np.var(array,axis = 1)
  variance_f = np.var(array.flatten())

  std_1 = np.std(array,axis = 0)
  std_2 = np.std(array,axis = 1)
  std_f = np.std(array.flatten())

  max_1 = np.max(array,axis = 0)
  max_2 = np.max(array,axis = 1)
  max_f = np.max(array.flatten())

  min_1 = np.min(array,axis = 0)
  min_2 = np.min(array,axis = 1)
  min_f = np.min(array.flatten())

  sum_1 = np.sum(array,axis = 0)
  sum_2 = np.sum(array,axis = 1)
  sum_f = np.sum(array.flatten())

  calculations = {
  'mean': [mean_1, mean_2, mean_f],
  'variance': [variance_1, variance_2, variance_f],
  'standard deviation': [std_1, std_2, std_f],
  'max': [max_1, max_2, max_f],
  'min': [min_1, min_2, min_f],
  'sum': [sum_1, sum_2, sum_f]
}


  return calculations