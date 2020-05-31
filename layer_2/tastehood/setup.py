from setuptools import setup, find_packages
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


if __name__ == '__main__':
    import sys
    print(sys.path)
    try:
        from tastehood_server import __version__
    except ImportError:
        __version__ = '0.0'

    setup(name='tastehood',
          version=__version__,
          description='Tastehood codebase for automating microgreen farming',
          url='https://github.com/smartmicrogreens/smartFarm',
          author='Robin + Nacho',
          packages=find_packages('.', exclude=['tests', 'tests.*']),
          package_data={
              'tastehood_server': ['version.txt']
          },
          use_scm_version={
              'write_to': 'tastehood_server/version.txt',
          },
          zip_safe=False,
          install_requires=[
              'sqlalchemy',
              'fastapi',
              'click',
              'uvicorn',
              'pydantic'
          ],
          entry_points={
              'console_scripts': ['tastehood_server=tastehood_server.cli.main:main', ]
          },
          python_requires='>=3.6',)