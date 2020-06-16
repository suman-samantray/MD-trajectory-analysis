#!/opt/local/bin/python

# make_cluster_traj
# python script to read in cluster log file and
# determine number of clusters against time
# for LSZ/ala this won't strictly work but can use this for testing purposes

import sys

cluster_dict={}

inf=open(sys.argv[1],'r')

lines=inf.readlines()

istart=lines.index('cl. | #st  rmsd | middle rmsd | cluster members\n')

icluster=-1
for line in lines[istart+1:]:
    # find separators
    sep1=line.index('|')
    sep2=sep1+line[sep1+2:].index('|')+2
    sep3=sep2+line[sep2+2:].index('|')+2

    try:
        icluster=int(line[:sep1-1])
    except:
        pass


    data=line[sep3+1:].split()
    for d in data:
        timestep=int(d)
        cluster_dict[timestep]=icluster


f = file("cluster_traj", "w")
k=cluster_dict.keys()
k.sort()
clusters_found=[]
nclusters=0
for timestep in k:
    icluster=cluster_dict[timestep]
    if not(icluster in clusters_found):
        clusters_found.append(icluster)
        nclusters+=1
    f.write( '%s%s%s\n' % (timestep, '  ', str(nclusters)))

f.close()
