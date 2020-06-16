#!/usr/bin/python

from matplotlib import rc, rcParams
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
#rc('text', dvipnghack=True)
rcParams['text.latex.preamble'] = [r'\usepackage{siunitx}',r'\sisetup{detect-all}',r'\usepackage{helvet}',r'\usepackage{sansmath}',r'\sansmath']

import numpy, scipy
import matplotlib, matplotlib.pyplot
import sys

nocolorbar=True
norm=matplotlib.colors.Normalize(vmin=-5,vmax=30)

inf=open(sys.argv[1],'r')
nx=int(sys.argv[3])
#print len(sys.argv[1])
ny=int(sys.argv[4])
dx=float(sys.argv[5])
dy=float(sys.argv[6])
try:
    nxticks=int(sys.argv[7])
except:
    nxticks=4
try:
    nyticks=int(sys.argv[8])
except:
    nyticks=4

fes=numpy.zeros([nx,ny])

lines=[]
for line in inf.readlines():
    line.strip()
    if line[0]=='#':
        continue
    if line=='\n':
        continue
    lines.append(line)

ii=0
min_e=1.e10
max_e=-1.e10

xmax=-1.0e10
xmin=1.0e10
ymax=-1.0e10
ymin=1.0e10

for iy in range(ny):
    for ix in range(nx):
        data=lines[ii].split()
        xx=float(data[0])
        yy=float(data[1])

        xmin=min(xx,xmin)
        xmax=max(xx,xmax)
        ymin=min(yy,ymin)
        ymax=max(yy,ymax)

        fes[ix,iy]=float(data[2])/4.184

        ii+=1

fes=numpy.transpose(fes)

print xmin,ymin
print xmax,ymax

dxtick=(xmax-xmin)/(nxticks-1.0)
dytick=(ymax-ymin)/(nyticks-1.0)

print dxtick,dytick

dnxtick=nx/(nxticks-1)
dnytick=ny/(nyticks-1)

print dnxtick,dnytick

xticks=[i*dnxtick for i in range(nxticks)]
xticklabels=["%4.2f" % (xmin+i*dxtick) for i in range(nxticks)]
yticks=[i*dnytick for i in range(nyticks)]
yticklabels=["%4.2f" % (ymin+i*dytick) for i in range(nyticks)]

fig=matplotlib.pyplot.figure(figsize=(8,6.))
#matplotlib.pyplot.suptitle('Amyloid Beta16-22 at BW(charmm36m)', fontsize=30)
#ax=fig.add_axes([0.15,0.90,0.6,0.05])
#ax=fig.add_axes([0.15,0.16,0.60,0.60])
c=matplotlib.pyplot.pcolormesh(fes,cmap='gist_stern')
matplotlib.pyplot.xticks(xticks,xticklabels,size=14)
matplotlib.pyplot.xlim((0,nx))
matplotlib.pyplot.yticks(yticks,yticklabels,size=14)
matplotlib.pyplot.ylim((0,ny))
cb=matplotlib.pyplot.colorbar()
cb.set_label(label='$Free\ Energy\ (Kcal/mol)$',size=20)
cb.ax.tick_params(labelsize=14)
matplotlib.pyplot.xlabel('$Dihedral\ Offset$',size=20)
matplotlib.pyplot.xlim((0,10))
matplotlib.pyplot.xticks(xticks,xticklabels,size=14)
matplotlib.pyplot.ylabel('$C-gamma\ Contacts$',size=20)
matplotlib.pyplot.ylim((0,15))
matplotlib.pyplot.yticks(yticks,yticklabels,size=14)
#bx=fig.add_axes([0.75,0.16,0.20,0.60])
#matplotlib.pyplot.ylim((0,nres))
#xxticks=[0,10,20]
#xxticklabels=["0",'10','20']
#matplotlib.pyplot.xticks(xxticks,xxticklabels,size=24)
#matplotlib.pyplot.xlabel('$\overline{z}_{res}$ / \AA',size=36)
#bx.set_yticklabels([])
#bx.plot(res_ave,res[:,-1],linewidth=2,color='#000000')

#matplotlib.pyplot.colorbar().set_label(label='$z_{res}$ / \AA',size=24)
#matplotlib.pyplot.show()
matplotlib.pyplot.savefig(sys.argv[2])
