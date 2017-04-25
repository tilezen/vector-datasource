import os.path
from setuptools import find_packages
from setuptools import setup

version_path = os.path.join(os.path.dirname(__file__), 'VERSION')
with open(version_path) as fh:
    version = fh.read().strip()

setup(name='vector-datasource',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'mapbox-vector-tile',
          'ModestMaps >= 1.3.0',
          'pycountry',
          'simplejson',
          'StreetNames',
          'tilequeue',
          'kdtree',
          'webcolors',
      ],
      test_suite='test',
      tests_require=[
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
