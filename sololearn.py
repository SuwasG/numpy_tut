
from numpy import numpy_financial as nfp
predict=nfp.fv(rate=0.1,pv=-1000,nper=2,pmt=0)
print(predict)