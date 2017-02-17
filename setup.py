from distutils.core import setup

setup(
    name='chimera_fakepolarimeter',
    version='0.0.1',
    packages=['chimera_fakepolarimeter', 'chimera_fakepolarimeter.instruments'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-fakepolarimeter',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='A fake polarimeter instrument driver for chimera'
)
