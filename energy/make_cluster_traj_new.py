#!/opt/local/bin/python

# make_cluster_traj
# python script to read in cluster log file and
# determine number of clusters against time
# for LSZ/ala this won't strictly work but can use this for testing purposes

import sys, numpy

cluster_dict={}


inf=open(sys.argv[1],'r')
df_imp=float(sys.argv[2])

lines=inf.readlines()

istart=lines.index('cl. | #st  rmsd | middle rmsd | cluster members\n')

icluster=-1
max_cluster=-1
for line in lines[istart+1:]:
    # find separators
    sep1=line.index('|')
    sep2=sep1+line[sep1+2:].index('|')+2
    sep3=sep2+line[sep2+2:].index('|')+2

    try:
        icluster=int(line[:sep1-1])
        if icluster>max_cluster:
            max_cluster=icluster
    except:
        pass


    data=line[sep3+1:].split()
    for d in data:
        timestep=float(d)
        cluster_dict[timestep]=icluster



k=cluster_dict.keys()
k.sort()
clusters_found=[]
nclusters=0
cluster_c=numpy.zeros((icluster))
for timestep in k:
    icluster=cluster_dict[timestep]
    if not(icluster in clusters_found):
        clusters_found.append(icluster)
        nclusters+=1

    cluster_c[icluster-1]+=1.0
    cmax=max(cluster_c)
    nclusters_imp=0.0
    for cc in cluster_c:
        if cc==0:
            continue
        df=-numpy.log(cc/cmax)
        if df<df_imp:
            nclusters_imp+=1.0


    print timestep,nclusters,nclusters_imp
