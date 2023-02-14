# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:34:29 2023

@author: npl71
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import build_ext

ext_modules = [Extension("fastmlv",
                         ["fastmlv.pyx"],
                         
                         extra_compile_args = ["--ffast-math"])]

setup(
      name="fastmlv",
      cmdclass = {"build_ext":build_ext},
      ext_modules = ext_modules)