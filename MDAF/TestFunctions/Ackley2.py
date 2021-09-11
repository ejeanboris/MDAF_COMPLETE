import math as m

def main(args):

    '''
    #_# dimmensions: 2
	#_# upper: 32
	#_# lower: -32
	#_# minimum: [0, 0]

    >>> main([0, 0])
    -200.0

    
	#_# cm_angle: array([[5.65927783e+00],       [7.35496768e-01],       [5.78026016e+00],       [7.89658853e-01],       [1.64629829e+02],       [1.21305405e+01],       [2.36845276e-01],       [4.62474283e-02],       [0.00000000e+00],       [4.30000000e-02]])
	#_# cm_conv: array([[0.23076923],       [0.01923077],       [0.76923077],       [0.23076923],       [0.        ],       [0.013     ]])
	#_# cm_grad: array([[0.67776659],       [0.08057764],       [0.        ],       [0.027     ]])
	#_# ela_conv: array([[ 8.99000000e-01],       [ 0.00000000e+00],       [-1.28437313e+01],       [ 1.30097926e+01],       [ 1.00000000e+03],       [ 8.50000000e-02]])
	#_# ela_curv: array([[1.67138684e+00],       [2.11477874e+00],       [2.47871167e+00],       [2.35585418e+00],       [2.81304349e+00],       [3.84712253e+00],       [4.91521801e-01],       [0.00000000e+00],       [1.00947417e+00],       [1.27750804e+00],       [1.07231230e+01],       [1.84915518e+00],       [3.91414501e+00],       [1.12977041e+03],       [8.10226920e+01],       [0.00000000e+00],       [1.14593818e+00],       [1.56903313e+00],       [2.91410632e+00],       [1.88909835e+00],       [2.84062445e+00],       [2.56326184e+01],       [3.39935335e+00],       [0.00000000e+00],       [8.40000000e+03],       [7.48000000e-01]])
	#_# ela_distr: array([[-0.67013865],       [-0.09235035],       [ 1.        ],       [ 0.        ],       [ 0.024     ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [1.00000000e+00],       [1.75106294e-02],       [9.00000000e-02],       [1.02247191e-02],       [1.00000000e-02],       [8.50000000e+01],       [1.10000000e+02],       [1.26500000e+02],       [1.25000000e+02],       [1.35000000e+02],       [1.75000000e+02],       [1.94170081e+01],       [1.27400000e+04],       [7.85000000e-01]])
	#_# ela_meta: array([[-6.08058266e-03],       [-1.24578212e+02],       [ 1.63005925e-03],       [ 2.18786048e-03],       [ 1.34219690e+00],       [-7.02427127e-03],       [ 8.91942646e-01],       [ 1.00359484e+00],       [ 9.42910444e-01],       [ 0.00000000e+00],       [ 7.00000000e-03]])
	#_# basic: array([[   2.        ],       [ 500.        ],       [ -32.        ],       [ -32.        ],       [  32.        ],       [  32.        ],       [-196.11101183],       [ -82.53967011],       [   6.        ],       [   6.        ],       [  36.        ],       [  36.        ],       [   1.        ],       [   0.        ],       [   0.        ]])
	#_# disp: array([[ 1.43172836e-01],       [ 2.29370520e-01],       [ 3.22785149e-01],       [ 4.98604939e-01],       [ 1.45153158e-01],       [ 2.29371341e-01],       [ 3.18457221e-01],       [ 5.00075741e-01],       [-2.86475351e+01],       [-2.57655639e+01],       [-2.26422983e+01],       [-1.67638623e+01],       [-2.80625149e+01],       [-2.52978395e+01],       [-2.23733696e+01],       [-1.64112812e+01],       [ 0.00000000e+00],       [ 8.00000000e-03]])
	#_# limo: array([[ 1.91414000e-02],       [ 7.04396915e-03],       [ 2.47223669e+00],       [ 4.22072748e-01],       [-9.63566714e-03],       [-1.92775958e-03],       [ 2.50758701e+00],       [ 1.55577807e+00],       [ 1.01938498e+00],       [ 1.01237543e+00],       [ 1.79774226e+00],       [ 7.17105814e-01],       [ 0.00000000e+00],       [ 3.30000000e-02]])
	#_# nbc: array([[ 1.01253954],       [ 0.93528579],       [ 0.70792465],       [ 0.10676121],       [-0.23871564],       [ 0.        ],       [ 0.023     ]])
	#_# pca: array([[1.        ],       [1.        ],       [1.        ],       [1.        ],       [0.51329024],       [0.51329019],       [0.44184058],       [0.34219476],       [0.        ],       [0.002     ]])
	#_# gcm: array([[1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.021     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.02      ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.024     ]])
	#_# ic: array([[0.76113587],       [0.50550551],       [1.01159111],       [0.16516517],       [0.35140562],       [0.        ],       [0.153     ]])

	#_# Represented: 1

	'''
    return -200 * m.e**(-0.02 * m.sqrt(args[0]**2 + args[1]**2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
