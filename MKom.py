#import package
import numpy as np
from math import exp,sin,cos,tan
#test function or default function
def funct(x):
	y=exp(x)-4*x**2
	return y
#xa=bottom limit, xb=upper limit, funct=define function, lmx=list x value, lfmx=list function value
def Bisection(funct,xa,xb,n):
	lfmx=np.zeros(n)
	lmx=np.zeros(n)
	for i in range(n):
		fa=funct(xa)
		#fb=funct(xb)
		mx=(xa+xb)/2
		fmx=funct(mx)
		if (fmx*fa)<=0:
			xb=mx
		else:
			xa=mx
		lmx[i]=mx
		lfmx[i]=fmx
	return lmx,lfmx

#xa=bottom limit, xb=upper limit, funct=define function, lmx=list x value, lfmx=list function value
def RegulaFalsi(funct,xa,xb,n):
	lfmx=np.zeros(n)
	lmx=np.zeros(n)
	for i in range(n):
		fa=funct(xa)
		fb=funct(xb)
		mx=((fb*xa)-(fa*xb))/(fb-fa)
		fmx=funct(mx)
		if (fmx*fa)<=0:
			xb=mx
		else:
			xa=mx
		lmx[i]=mx
		lfmx[i]=fmx
	return lmx,lfmx

#funct=define function, lxi=list of x, lfxi=list of f(xi)
def Secant(funct,x0,x1,n):
	lfxi=np.zeros(n)
	lxi=np.zeros(n)
	lxi[0:2]=x0,x1
	lfxi[0:2]=funct(x0),funct(x1)
	for i in range(n-2):#start with x2
		xi=(lfxi[i+1]*lxi[i]-lfxi[i]*lxi[i+1])/(lfxi[i+1]-lfxi[i])
		fxi=funct(xi)
		lxi[i+2]=xi
		lfxi[i+2]=fxi
	return lxi,lfxi
