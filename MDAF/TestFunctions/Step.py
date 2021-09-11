import math

def main(args):
    '''
    >>> main([0,0])
    0

    
    #_# dimmensions: 2
	#_# upper: 100
	#_# lower: -100
	#_# minimum: [0,0]
	#_# opti: 0
    
	#_# cm_angle: array([[1.76951433e+01],       [2.53449463e+00],       [1.73770488e+01],       [2.51496578e+00],       [1.61069593e+02],       [1.41112959e+01],       [2.50578704e-01],       [3.08199018e-02],       [0.00000000e+00],       [3.11000000e-01]])
	#_# cm_conv: array([[0.23076923],       [0.03846154],       [0.67307692],       [0.30769231],       [0.        ],       [0.057     ]])
	#_# cm_grad: array([[0.6861495 ],       [0.08471491],       [0.        ],       [0.215     ]])
	#_# ela_conv: array([[ 8.71000000e-01],       [ 1.00000000e-03],       [-2.02239361e+01],       [ 2.03378736e+01],       [ 1.00000000e+03],       [ 5.49000000e-01]])
	#_# ela_curv: array([[0.00000000e+00],       [0.00000000e+00],       [2.30592511e-04],       [0.00000000e+00],       [0.00000000e+00],       [2.75548505e-02],       [2.34386226e-03],       [0.00000000e+00],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [1.00000000e+00],       [7.50344071e+31],       [7.50344071e+31],       [8.30484005e+31],       [8.30484005e+31],       [9.10623938e+31],       [9.10623938e+31],       [1.13334981e+31],       [9.90000000e-01],       [6.00400000e+03],       [2.86500000e+00]])
	#_# ela_distr: array([[ 0.02006772],       [-0.62140715],       [ 1.        ],       [ 0.        ],       [ 0.111     ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [1.39349701e-01],       [4.88512241e-01],       [1.00000000e-02],       [1.11235955e-02],       [1.00000000e-02],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [0.00000000e+00],       [5.90000000e+02],       [3.94000000e-01]])
	#_# ela_meta: array([[-6.06539506e-03],       [ 9.90020277e+01],       [ 8.01352476e-04],       [ 3.01415715e-03],       [ 3.76133754e+00],       [-7.26293464e-03],       [ 9.36883288e-01],       [ 1.01130593e+00],       [ 9.36200242e-01],       [ 0.00000000e+00],       [ 4.50000000e-02]])
	#_# basic: array([[ 2.00e+00],       [ 5.00e+02],       [-1.00e+02],       [-1.00e+02],       [ 1.00e+02],       [ 1.00e+02],       [ 3.00e+00],       [ 1.95e+02],       [ 6.00e+00],       [ 6.00e+00],       [ 3.60e+01],       [ 3.60e+01],       [ 1.00e+00],       [ 0.00e+00],       [ 3.00e-03]])
	#_# disp: array([[ 1.62767939e-01],       [ 2.35149318e-01],       [ 3.47340681e-01],       [ 5.12177764e-01],       [ 1.64507464e-01],       [ 2.34816459e-01],       [ 3.49915299e-01],       [ 5.12127048e-01],       [-8.74945746e+01],       [-7.99303899e+01],       [-6.82058800e+01],       [-5.09796519e+01],       [-8.57515939e+01],       [-7.85353614e+01],       [-6.67220794e+01],       [-5.00733178e+01],       [ 0.00000000e+00],       [ 5.60000000e-02]])
	#_# limo: array([[ 2.12855984e-03],       [ 5.41850462e-04],       [ 1.41285806e+00],       [ 1.19321767e-02],       [-4.64254718e-03],       [ 5.34346782e-05],       [ 1.01304331e+00],       [ 1.20693637e-02],       [ 1.00329972e+00],       [ 1.00334870e+00],       [ 1.01324563e+00],       [ 7.17136058e-01],       [ 0.00000000e+00],       [ 3.00000000e-01]])
	#_# nbc: array([[ 0.96803593],       [ 0.92588983],       [ 0.67665516],       [ 0.11764107],       [-0.24469197],       [ 0.        ],       [ 0.347     ]])
	#_# pca: array([[1.        ],       [1.        ],       [1.        ],       [1.        ],       [0.50586371],       [0.50586326],       [0.40607191],       [0.3373892 ],       [0.        ],       [0.022     ]])
	#_# gcm: array([[1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.293     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.261     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.239     ]])
	#_# ic: array([[0.76154199],       [0.18518519],       [0.73259654],       [0.00500501],       [0.35140562],       [0.        ],       [1.652     ]])

	#_# Represented: 1

	'''
    floors = [math.floor(abs(a)) for a in args]
    return sum(floors)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
