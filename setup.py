from setuptools import setup, find_packages
from distutils.command.clean import clean as _CleanCommand
import shutil
import glob
import re
import os

exec(open('hermione/_version.py').read())

here = os.getcwd()

class CleanCommand(_CleanCommand):
    """Custom clean command to tidy up the project root."""
    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info'.split(' ')

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        global here
        
        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob.glob(os.path.normpath(os.path.join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError("%s is not a path inside %s" % (path, here))
                print('removing %s' % os.path.relpath(path))
                shutil.rmtree(path)

setup(
    name='hermione-ml',
    version=__version__,
    author='A3Data',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'conda'
    ],
    entry_points='''
        [console_scripts]
        hermione=hermione.cli:cli
    ''',
    cmdclass={'clean':CleanCommand}
)


