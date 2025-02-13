def main(args):
    '''
    >>> main([5,5])
    0

    
    #_# dimmensions: 2
	#_# upper: 500
	#_# lower: -500
	#_# minimum: [5, -5]
	#_# opti: 0
    
	#_# cm_angle: array([[8.42995060e+01],       [1.48465167e+01],       [8.85937471e+01],       [1.22477660e+01],       [1.56556548e+02],       [1.64601666e+01],       [2.62117969e-01],       [1.07318701e-01],       [0.00000000e+00],       [3.81000000e-01]])
	#_# cm_conv: array([[0.23076923],       [0.01923077],       [0.90384615],       [0.09615385],       [0.        ],       [0.077     ]])
	#_# cm_grad: array([[0.66304389],       [0.11459043],       [0.        ],       [0.176     ]])
	#_# ela_conv: array([[ 1.0000000e+00],       [ 0.0000000e+00],       [-5.4165993e+04],       [ 5.4165993e+04],       [ 1.0000000e+03],       [ 1.0510000e+00]])
	#_# ela_curv: array([[1.11653166e+02],       [5.87342803e+02],       [7.76324203e+02],       [8.09746028e+02],       [9.75220399e+02],       [1.27658179e+03],       [2.68311668e+02],       [0.00000000e+00],       [1.00877643e+00],       [1.39213209e+00],       [4.66136091e+00],       [1.90521110e+00],       [3.34958045e+00],       [1.10941818e+02],       [1.15327155e+01],       [0.00000000e+00],       [1.00000002e+00],       [1.00000129e+00],       [1.00065585e+00],       [1.00000229e+00],       [1.00000435e+00],       [1.10032917e+00],       [7.36581030e-03],       [0.00000000e+00],       [8.40000000e+03],       [5.63500000e+00]])
	#_# ela_distr: array([[ 0.45479172],       [-0.44239297],       [ 2.        ],       [ 0.        ],       [ 0.078     ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [2.36306319e-10],       [3.39801109e-02],       [3.00000000e-02],       [1.08988764e-02],       [1.00000000e-02],       [2.50000000e+01],       [3.00000000e+01],       [3.32000000e+01],       [3.50000000e+01],       [3.50000000e+01],       [4.00000000e+01],       [3.13983851e+00],       [3.41000000e+03],       [2.00400000e+00]])
	#_# ela_meta: array([[-6.08141078e-03],       [ 1.61741156e+05],       [ 4.69187877e-01],       [ 4.87943868e-01],       [ 1.03997544e+00],       [-4.82793266e-03],       [ 9.99975314e-01],       [ 1.00020587e+00],       [ 9.99975022e-01],       [ 0.00000000e+00],       [ 5.90000000e-02]])
	#_# basic: array([[ 2.00000000e+00],       [ 5.00000000e+02],       [-5.00000000e+02],       [-5.00000000e+02],       [ 5.00000000e+02],       [ 5.00000000e+02],       [ 1.42515936e+02],       [ 4.55661620e+05],       [ 6.00000000e+00],       [ 6.00000000e+00],       [ 3.60000000e+01],       [ 3.60000000e+01],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 0.00000000e+00]])
	#_# disp: array([[ 1.54548192e-01],       [ 2.36533792e-01],       [ 3.20672384e-01],       [ 5.01832640e-01],       [ 1.61683546e-01],       [ 2.35092782e-01],       [ 3.19484619e-01],       [ 5.02431697e-01],       [-4.41822856e+02],       [-3.98978176e+02],       [-3.55008369e+02],       [-2.60336217e+02],       [-4.30399953e+02],       [-3.92710925e+02],       [-3.49383323e+02],       [-2.55456484e+02],       [ 0.00000000e+00],       [ 7.00000000e-02]])
	#_# limo: array([[ 2.30080234e+00],       [ 2.94677297e-03],       [ 7.45052475e+02],       [ 2.78527250e+02],       [-6.90102908e-03],       [ 2.84166012e-03],       [ 2.56700894e+00],       [ 1.63021264e+00],       [ 1.00639041e+00],       [ 1.00376955e+00],       [ 5.69442133e+02],       [ 7.17132783e-01],       [ 0.00000000e+00],       [ 2.48000000e-01]])
	#_# nbc: array([[ 0.97863618],       [ 0.92457637],       [ 0.69441449],       [ 0.12402379],       [-0.24483581],       [ 0.        ],       [ 0.222     ]])
	#_# pca: array([[1.        ],       [1.        ],       [0.33333333],       [1.        ],       [0.51467844],       [0.51467818],       [0.99998406],       [0.34316251],       [0.        ],       [0.071     ]])
	#_# gcm: array([[1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.269     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.258     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.303     ]])
	#_# ic: array([[  0.7410432 ],       [  3.04804805],       [233.00614107],       [  2.56756757],       [  0.40160643],       [  0.        ],       [  5.173     ]])

	#_# Represented: 1

	'''
    return (abs(args[0])-5)**2 + (abs(args[1])-5)**2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
