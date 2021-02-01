# obsoletesource
a cython package with obsolete generated c-files (by Cython 0.27.1)

# Installation

This project is here to demostrate issues with cython-generated c-files which might become obsolete/wrong for future versions of Python.

The installation via 

    pip install https://github.com/realead/obsoletesource/zipball/master
    
will fail for Python3.9 and later.

Running istallation with 

   pip install --global-option build --global-option --force https://github.com/realead/obsoletesource/zipball/master
  
will trigger a recreation of stale c-file by cython.
