from distutils.core import setup
from Cython.Build import cythonize
setup(name='hello cython app',ext_modules=cythonize("cythonlib.pyx"))