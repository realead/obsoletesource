from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

with open("README.md", "r") as fh:
    long_description = fh.read()

extensions = Extension(
            name='obsoletesource.obsoletesource',
            sources = ["src/obsoletesource/obsoletesource.pyx"]
    )
extensions = cythonize(extensions, compiler_directives={'language_level' : 3})

kwargs = {
      'name':'obsoletesource',
      'version':'0.1.0',
      'description':'a project',
      'long_description':long_description,
      'long_description_content_type':"text/markdown",
      'author':'Egor Dranischnikow',
      'url':'https://github.com/realead/obsoletesource',
      'packages':find_packages(where='src'),
      'package_dir':{"": "src"},
      'license': 'MIT',
      'classifiers': [
            "Programming Language :: Python :: 3",
       ],
      'ext_modules':  extensions,

       #ensure pxd-files:
      'package_data' : { 'obsoletesource': ['*.pxd','*.pxi']},
      'include_package_data' : True,
      'zip_safe' : False  #needed because setuptools are used
}
setup(**kwargs)
