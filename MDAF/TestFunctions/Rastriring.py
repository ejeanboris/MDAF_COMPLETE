import math

def main(args):
    '''
    >>> (main([0,0]) - 0)<0.001
    True

    
    #_# dimmensions: 2
	#_# upper: 5.12
	#_# lower: -5.12
	#_# minimum: [0,0]
    
	#_# cm_angle: array([[5.87139339e-01],       [2.50148614e-01],       [5.39132964e-01],       [2.87449942e-01],       [1.16642840e+02],       [4.26135413e+01],       [4.82701426e-01],       [6.47550685e-02],       [0.00000000e+00],       [3.73000000e-01]])
	#_# cm_conv: array([[0.26923077],       [0.19230769],       [0.44230769],       [0.55769231],       [0.        ],       [0.088     ]])
	#_# cm_grad: array([[0.32940512],       [0.14284079],       [0.        ],       [0.351     ]])
	#_# ela_conv: array([[ 6.52000000e-01],       [ 0.00000000e+00],       [-5.75302336e+00],       [ 1.19391378e+01],       [ 1.00000000e+03],       [ 9.72000000e-01]])
	#_# ela_curv: array([[3.14155067e+00],       [4.70454711e+01],       [5.91093992e+01],       [6.14106784e+01],       [7.35309119e+01],       [9.73695232e+01],       [1.95193801e+01],       [0.00000000e+00],       [1.00069440e+00],       [1.18483732e+00],       [4.10205349e+00],       [1.77600602e+00],       [2.93799708e+00],       [4.71444119e+01],       [7.49427603e+00],       [0.00000000e+00],       [1.00007229e+00],       [1.17324533e+00],       [3.52835610e+00],       [1.56143224e+00],       [2.79027274e+00],       [8.50533816e+01],       [7.05663035e+00],       [0.00000000e+00],       [8.40000000e+03],       [6.89500000e+00]])
	#_# ela_distr: array([[ 0.08411456],       [-0.42273661],       [ 1.        ],       [ 0.        ],       [ 0.14      ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [1.24736370e-15],       [3.14890101e-01],       [1.00000000e-02],       [1.11235955e-02],       [1.00000000e-02],       [4.00000000e+01],       [5.50000000e+01],       [6.71000000e+01],       [7.00000000e+01],       [7.50000000e+01],       [1.30000000e+02],       [1.63017629e+01],       [6.80000000e+03],       [6.69400000e+00]])
	#_# ela_meta: array([[-6.03378217e-03],       [ 3.70497354e+01],       [ 6.54354467e-03],       [ 3.36946885e-02],       [ 5.14930212e+00],       [-7.72510669e-03],       [ 4.81101589e-01],       [ 1.01316122e+00],       [ 4.75836669e-01],       [ 0.00000000e+00],       [ 4.40000000e-02]])
	#_# basic: array([[ 2.00000000e+00],       [ 5.00000000e+02],       [-5.12000000e+00],       [-5.12000000e+00],       [ 5.12000000e+00],       [ 5.12000000e+00],       [ 1.83249306e+00],       [ 7.66325249e+01],       [ 6.00000000e+00],       [ 6.00000000e+00],       [ 3.60000000e+01],       [ 3.60000000e+01],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 1.00000000e-03]])
	#_# disp: array([[ 0.41666182],       [ 0.54763843],       [ 0.57000276],       [ 0.66573524],       [ 0.4040245 ],       [ 0.55213845],       [ 0.56502387],       [ 0.65057055],       [-3.12243954],       [-2.42135986],       [-2.30165009],       [-1.789222  ],       [-3.13488171],       [-2.35578975],       [-2.28801132],       [-1.83802854],       [ 0.        ],       [ 0.106     ]])
	#_# limo: array([[ 6.30252412e-01],       [ 2.78501356e-02],       [ 7.89971253e+00],       [ 3.26190930e+00],       [-2.65522094e-02],       [ 5.21604974e-03],       [ 7.44675598e+00],       [ 2.13763366e+01],       [ 1.13338901e+00],       [ 1.07145472e+00],       [ 6.08810967e+00],       [ 7.16432880e-01],       [ 0.00000000e+00],       [ 2.54000000e-01]])
	#_# nbc: array([[ 0.23334974],       [ 0.73721487],       [ 0.21445289],       [ 0.27649545],       [-0.54463082],       [ 0.        ],       [ 0.337     ]])
	#_# pca: array([[1.        ],       [1.        ],       [0.33333333],       [1.        ],       [0.50305359],       [0.50305244],       [0.92033692],       [0.33667482],       [0.        ],       [0.015     ]])
	#_# gcm: array([[1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.202     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.166     ],       [3.        ],       [0.08333333],       [0.91666667],       [0.77777778],       [0.10005948],       [0.33333333],       [0.11068569],       [0.78925483],       [0.39487534],       [0.02777778],       [0.07407407],       [0.02777778],       [0.16666667],       [0.08018754],       [0.22222222],       [0.08333333],       [0.33333333],       [0.08333333],       [0.83333333],       [0.4330127 ],       [1.        ],       [0.78925483],       [0.02777778],       [0.        ],       [0.263     ]])
	#_# ic: array([[ 0.8782254 ],       [ 1.86686687],       [16.83550803],       [ 1.46646647],       [ 0.63654618],       [ 0.        ],       [ 2.818     ]])

	#_# Represented: 1

	'''
    vals = [(x**2 - 10*math.cos(2*math.pi*x)+10) for i,x in enumerate(args)]
    return sum(vals)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
