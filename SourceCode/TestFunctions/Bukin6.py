from math import sqrt, fabs


def main(args):
    return 100*sqrt(fabs(args[1]-0.01*args[0]**2))+0.01*fabs(args[0]+10)