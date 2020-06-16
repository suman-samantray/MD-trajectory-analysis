#!/usr/bin/python

import numpy, matplotlib, matplotlib.colors, matplotlib.pyplot, gzip
import matplotlib.gridspec

import sys

from matplotlib import rc, rcParams
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
#rc('text', dvipnghack=True)
rcParams['text.latex.preamble'] = [r'\usepackage{siunitx}',r'\sisetup{detect-all}',r'\usepackage{helvet}',r'\usepackage{sansmath}',r'\sansmath']

def sscode_to_number(code):

    return {'C':0,'T':1,'E':2,'B':3,'H':4,'G':5,'I':6}[code]

eps=1.0e-4
#cmap=matplotlib.colors.ListedColormap(['#ffffff','#cc0000','#cc00cc','#ff66cc','#0000ff','#00ffff','#4888cc'])
#cmap=matplotlib.colors.ListedColormap(['#ffffff','#ffffff','#ffffff','#ffffff','#ffffff','#0000ff','#ffffff'])
cmap,norm=matplotlib.colors.from_levels_and_colors([-.1,0.9,1.9,2.9,3.9,4.9,5.9,6.9],
                                                   ['#ffffff','#ff0000','#cc00cc','#00ff00','#0000ff','#00ffff','#4888cc'])
matplotlib.colors.NoNorm()

cont=[i for i in range(8)]

if sys.argv[1][-3:]=='.gz':
    inf=gzip.open(sys.argv[1],'r')
else:
    inf=open(sys.argv[1],'r')

inf.readline()
inf.readline()
inf.readline()
inf.readline()
inf.readline()
nframe=int(inf.readline().split()[-1])
nres=int(inf.readline().split()[-1])
inf.readline()
inf.readline()

resid=numpy.zeros((nres))
ss_data=numpy.zeros((nres,nframe))

timestep=numpy.zeros((nframe))
for iframe in range(nframe):
    timestep[iframe]=10*iframe
    #print iframe
    for ires in range(nres):
        data=inf.readline().split()
        resid[ires]=int(data[0])
        ss_data[ires,iframe]=sscode_to_number(data[-1])+0.1
    print iframe

fig=matplotlib.pyplot.figure(figsize=(10,5.))
ax=fig.add_axes([0.15,0.20,0.80,0.70])
pl=matplotlib.pyplot.imshow(ss_data,interpolation='none',aspect='auto',cmap=cmap,norm=norm)

matplotlib.pyplot.xlim((0,0.05*nframe))
nxticks=4
#xticks=[500*i for i in range(nxticks+1)]
xticks=[0,200,400,600,800,1000]
xticklabels=["%4.f" % (t) for t in xticks]
#xticklabels=["%4.f" % (0.5*t) for t in xticks]
print xticklabels
matplotlib.pyplot.xlabel('$t$ / ns',name='helvetica-oblique',size=36)
matplotlib.pyplot.xticks(xticks,xticklabels,name='helvetica',size=24)
yticklabels=['K16','L17','V18','F19','F20','A21','E22']
yticks=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
#matplotlib.pyplot.ylabel('$Residue$',name='helvetica-oblique',size=36)
matplotlib.pyplot.ylim((0,nres))
#nyticks=nres/25
#yticks=[25*i for i in range(nyticks+1)]
#yticklabels=[i for i in yticks]

matplotlib.pyplot.yticks(yticks,yticklabels,name='helvetica',size=24)
#cb=matplotlib.pyplot.colorbar(boundaries=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0],
#                              values=['#ffffff','#ff0000','#cc00cc','#ff66cc','#0000ff','#00ffff','#4888cc'],
#                              ticks=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
#cb.ax.set_yticklabels(['C','T','E','B','H','G','I'])
#cb.ax.tick_params(labelsize=20)
cb=fig.colorbar(pl,ticks=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])#,tick_labels=['C','T','E','B','H','G','I'])
#cb=matplotlib.pyplot.colorbar(boundaries=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0],
#                              values=['#ffffff','#ff0000','#cc00cc','#ff66cc','#0000ff','#00ffff','#4888cc'],
#                              ticks=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5],cmap=cmap)
#cb.ax.set_yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
cb.ax.set_yticklabels(['C','T','E','B','H','G','I'])
cb.ax.tick_params(labelsize=20)

fig.savefig(sys.argv[2])
#matplotlib.pyplot.show()
