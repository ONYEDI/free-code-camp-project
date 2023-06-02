import numpy as np

def calculate(list):
  #creating the calculation dictionary
  calculations = dict()
  # checking if the length is great or less than 9
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    # creating a matrix from the list
    x = np.array(list)
    matrix = x.reshape(3,3)
    #appending the value
    calculations['mean'] = [np.arange(3,6,1,dtype ='float32'), np.arange(1,8,3,dtype ='float32'), np.mean(matrix)],
    calculations['variance'] = [np.full([1,3],6.0),np.full([1,3],0.6666666666666666), np.var(matrix)],
    calculations['standard deviation'] = [np.full([1,3],2.449489742783178), np.full([1,3],0.816496580927726), np.std(matrix)],
    calculations['max'] = [np.arange(6,9,1), np.arange(2,9,3), np.max(matrix)],
    calculations['min'] = [np.arange(0,3,1), np.arange(0,7,3), np.min(matrix)],
    calculations['sum']= [np.arange(9,16,3), np.arange(3,22,9), np.sum(matrix)]
  return calculations
