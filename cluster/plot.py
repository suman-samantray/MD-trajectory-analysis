 
from matplotlib import pyplot
from pylab import genfromtxt  
 	


data = genfromtxt("cluster_traj.txt")

pyplot.plot(data[:,0], data[:,1])
pyplot.title('ClusterTrajectory')
pyplot.xlabel('Timestep')
pyplot.ylabel('Cluster')
pyplot.show()