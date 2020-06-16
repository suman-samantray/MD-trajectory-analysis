#!/opt/local/bin/python

from matplotlib import rc, rcParams
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Plsztino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Plsztino']})
rc('text', usetex=True)
#rc('text', dvipnghack=True)
rcParams['text.latex.preamble'] = [r'\usepackage{siunitx}',r'\sisetup{detect-all}',r'\usepackage{helvet}',r'\usepackage{sansmath}',r'\sansmath']

import numpy, matplotlib, matplotlib.pyplot,sys


def read_data(inf):

    r=[]
    f=[]
    for line in inf.readlines():
        if line[0] in ['#','@']:
            continue
        data=line.split()
        r.append(float(data[0]))
        f.append(float(data[1]))
    r=numpy.array(r)
    f=numpy.array(f)
    return r,f

presentation=True
paper=False
if presentation:
    ticksize=20
    labelsize=36
    linethickness=2
    xmin=0.2
    ymin=0.23
    dx=0.6
    dy=0.67
if paper:
    ticksize=24
    labelsize=24
    linethickness=2
    xmin=0.20
    ymin=0.15
    dx=0.75
    dy=0.75



yticks=[0.0,0.0025,0.005,0.0075]
yticklabels=['0','2.5','5','7.5']
x1=0.0
x2=80.0
xticks=[0,20,40,60,80]
xticklabels=['0','20','40','60','80']

inf1=open(sys.argv[1],'r')
#change 
#inf2=open(sys.argv[2],'r')

r_1,hist_1=read_data(inf1)
#change
#r_2,hist_2=read_data(inf2)


fig=matplotlib.pyplot.figure(figsize=(20,16.0))

ax=fig.add_axes([xmin,ymin,dx,dy])
matplotlib.pyplot.xlim((2.5,10.0))
matplotlib.pyplot.xticks([0.0,2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0],['0.0','2.0','4.0','6.0','8.0','10.0','12.0','14.0','16.0','18.0'],size=ticksize)
matplotlib.pyplot.xlabel('$r_{G}$ / \AA',size=labelsize)

matplotlib.pyplot.ylim((0,0.08))
#matplotlib.pyplot.yticks([0,0.05,0.10,0.15,0.20],['0','0.05','0.10','0.15'],size=ticksize)\
matplotlib.pyplot.yticks([0,0.025,0.05,0.075,0.10],['0','0.025','0.05','0.075','0.10'],size=ticksize)
matplotlib.pyplot.ylabel('$P(r_{G})$',size=labelsize)
matplotlib.pyplot.plot(r_1,hist_1,color="#000000",linewidth=linethickness,label='Nchain6')
#change
#matplotlib.pyplot.plot(r_2,hist_2,color="#aa0000",linewidth=linethickness,label='Nchain20')
#change
fig.savefig(sys.argv[2])
