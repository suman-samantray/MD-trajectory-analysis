#!/usr/bin/python

import numpy, matplotlib, matplotlib.colors, matplotlib.pyplot, gzip
import matplotlib.gridspec
import matplotlib.patches as patches

import sys

def anint(x):
    x1=numpy.floor(x)
    x2=x1+1.0
    if (x2-x)<(x-x1):
        return int(x2)
    else:
        return int(x1)

## regions for SS types
phi_alpha_1=-122
phi_alpha_2=-52
psi_alpha_1=-84
psi_alpha_2=-14

rama=numpy.zeros((360,360))

inf=open(sys.argv[1],'r')
nRes=int(sys.argv[3])
nPB=nRes-1

while 1:
    line=inf.readline()
    if line[0]=='@':
        continue
    if line[0]=='#':
        continue
    break

norm=0
while 1:
    line=inf.readline()[:-1]
    if line=='':
        break
    if len(line)==0:
        break
    norm+=1
    data=line.split()
    if len(data)<2:
        break
    (phi,psi)=(float(data[0]),float(data[1]))
    iPhi=anint(phi)+180
    if iPhi==360:
        iPhi=0
    iPsi=anint(psi)+180
    if iPsi==360:
        iPsi=0
    rama[iPsi,iPhi]+=1.0

    for i in range(nPB-1):
        line=inf.readline()
        data=line.split()
        if len(data)<2:
            break
        (phi,psi)=(float(data[0]),float(data[1]))
        iPhi=anint(phi)+180
        if iPhi==360:
            iPhi=0
        iPsi=anint(psi)+180
        if iPsi==360:
            iPsi=0
        rama[iPsi,iPhi]+=1.0


## normalise
fig=matplotlib.pyplot.figure(figsize=(10,8))
cs=matplotlib.pyplot.contourf([float(iPsi) for iPsi in range(-180,180)],[float(iPhi) for iPhi in range(-180,180)],rama,[0,10,20,30,40,50,60],extend='both')
ca=matplotlib.pyplot.gca()
ca.add_patch(patches.Rectangle((-122,-84),70,70,fill=False))
ca.add_patch(patches.Rectangle((-150,95),80,80,fill=False))
ca.add_patch(patches.Rectangle((14,52),70,70,fill=False))
ca.add_patch(patches.Rectangle((-180,50),130,130,fill=False))
ca.add_patch(patches.Rectangle((150,50),30,130,fill=False))
ca.add_patch(patches.Rectangle((-180,-180),130,30,fill=False))
cb=matplotlib.pyplot.colorbar()

font = {'family': 'serif',
        'color':  'darkred',
        'size': 24,
        }

matplotlib.pyplot.title('Ramanchandran_Plot', fontdict=font)
matplotlib.pyplot.xlabel('Phi',fontdict=font)
matplotlib.pyplot.xticks([-180,-90,0,90,180],['-180','-90','0','90','180'],size=16)
matplotlib.pyplot.ylabel('Psi',fontdict=font)
matplotlib.pyplot.yticks([-180,-90,0,90,180],['-180','-90','0','90','180'],size=16)

#cb=matplotlib.pyplot.colorbar()
fig.savefig(sys.argv[2])
