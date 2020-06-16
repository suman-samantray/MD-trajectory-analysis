#!/opt/local/bin/python

## get_ree_hist
##
##

import numpy, sys

def anint(x):

    x1=numpy.floor(x)
    x2=x1+1.0

    if (x2-x)<(x-x1):
        return x2
    else:
        return x1

inf=open(sys.argv[1],'r')
rlo=float(sys.argv[3])
rhi=float(sys.argv[4])
dr=float(sys.argv[5])
t0=float(sys.argv[6])

nBin=int((rhi-rlo)/dr)
print nBin

rg_hist=numpy.zeros(nBin)

norm=0.0

for line in inf.readlines():
    data=line.split()
    if line[0] in ["#","@"]:
        continue
    if line[0]=='&':
        break
    if float(data[0])<t0:
        continue

    rg=10.0*float(data[1])

    ibin=anint((rg-rlo)/dr)
    if ibin>len(rg_hist)-1:
        continue

    rg_hist[int(ibin)]+=1.0
    norm+=1.0

rg_hist/=norm
ouf=open(sys.argv[2],'w')
for i in range(len(rg_hist)):
    rr=rlo+(i+0.5)*dr
    print >> ouf, rr,rg_hist[i]
