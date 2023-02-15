# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:25:45 2023

@author: npl71
"""
#cython: boundscheck=False, wraparound=False, nonecheck=False
import numpy as np
from libc.math cimport abs 

cpdef int fastmlv(double[:,:]data,int x,int y):
    
    a = np.array(data[x+1,y],data[x-1,y],data[x,y+1],data[x,y-1],data[x+1,y+1], data[x-1,y-1],data[x+1,y-1],data[x-1,y+1])
    b = np.array(data[x,y],data[x,y],data[x,y],data[x,y],data[x,y],data[x,y],data[x,y],data[x,y])
    
    
    
    void subtract(int *x, int *y, int *result, int size)
    {    
    for (int q=0 ; q<size ; ++q)
        result[q] = y[q]-x[q];
    }
        
    d=subtract(b,a,result,8)
    e=abs(d)
    return e
    
cpdef double[:,:] fastmlv_image(double[:,:] imagedata):
    cdef int length = imagedata.shape[0]
    cdef int width = imagedata.shape[1]
    
    #print (length,width)
    cdef double[:,:] mlvmap = np.zeros((length,width))
    cdef i,j
    
    #blocksx = np.arange(1,width,3)
    #blocksy = np.arange(1,length,3)
    
    for i in range(1,length-1):
        for j in range(1,width-1):
            mlvmap[i,j]=fastmlv(imagedata,i,j)
            
    mlvmap=mlvmap[1:length-1,1:width-1]
    
            
    return mlvmap