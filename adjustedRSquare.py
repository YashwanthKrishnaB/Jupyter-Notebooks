def adjusted_rSquare(r,x):
    n=x.shape[0]
    p=x.shape[1]
    return 1-(1-r)*(n-1)/(n-p-1)
