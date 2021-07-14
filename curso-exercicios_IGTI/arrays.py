import numpy as np

x=np.ones((2, 2))
y=np.eye(2)
print('x:\n', x)
print('x:\n', y)
print('soma de 2 arrays:\n', x + y)
print('soma com float/int:', x + 2)
print('subtraçao de 2 arrays:\n', x - y)
print('subtraçao com float/int:', x - 2)
print('divisao com float/int:', x / 2)
print('mutiplicaçao de 2 arrays:\n', x * y)
print('mutiplicaçao com float/int:', x * 2)