import matplotlib.pyplot as plt
import numpy as np
import allantools as allan

def example1():
	"""
	Compute the GRADEV of a white phase noise. Compares two different 
	scenarios. 1) The original data and 2) ADEV estimate with gap robust ADEV.
	"""
	N = 1000
	f = 1
	y = np.random.randn(1,N)[0,:]
	x = np.linspace(1,len(y),len(y))
	x_ax, y_ax, err_l,err_h, ns = allan.gradev(y,f,x)
	plt.errorbar(x_ax, y_ax,yerr=[err_l,err_h],label='GRADEV, no gaps')
	
	
	y[np.floor(0.4*N):np.floor(0.6*N)] = np.NaN # Simulate missing data
	x_ax, y_ax, err_l,err_h, ns = allan.gradev(y,f,x)
	plt.errorbar(x_ax, y_ax,yerr=[err_l,err_h], label='GRADEV, with gaps')
	plt.xscale('log')
	plt.yscale('log')
	plt.grid()
	plt.legend()
	plt.xlabel('Tau / s')
	plt.ylabel('Overlapping Allan deviation')
	plt.show()

def example2():
	"""
	Compute the GRADEV of a nonstationary white phase noise.
	"""
	N=1000 # number of samples
	f = 1 # data samples per second
	s=1+5/N*np.arange(0,N)
	y=s*np.random.randn(1,N)[0,:]
	x = np.linspace(1,len(y),len(y))
	x_ax, y_ax, err_l, err_h, ns = allan.gradev(y,f,x)
	plt.loglog(x_ax, y_ax,'b.',label="No gaps")
	y[int(0.4*N):int(0.6*N,)] = np.NaN  # Simulate missing data
	x_ax, y_ax, err_l, err, ns = allan.gradev(y,f,x)
	plt.loglog(x_ax, y_ax,'g.',label="With gaps")
	plt.grid()
	plt.legend()
	plt.xlabel('Tau / s')
	plt.ylabel('Overlapping Allan deviation')
	plt.show()
	

if __name__ == "__main__":
	#example1()
	example2()