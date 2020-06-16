#!/opt/local/bin/python

import sys, numpy

RT=8.3143/4184.*298.

inf=open(sys.argv[1],'r')

for i in range(7):
    inf.readline()

data=inf.readline().split()
nstructures=int(data[1])

for i in range(4):
    inf.readline()

nst=[]
ist=0
while 1:
    data=inf.readline().split()
    if data[0]=='|':
        continue
    ist+=1
    n=int(data[2])

    nst.append(n)
    if ist==nstructures:
        break

print "## cluster number  FE  nstructures"
for i,n in enumerate(nst):

    fe=-RT*numpy.log(float(n)/float(nst[0]))
    print "%6d %12.6f %12d " % (i,fe,n)
