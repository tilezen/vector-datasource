from setuptools import find_packages
from setuptools import setup

version = 'v1.0.0.dev0'

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
      ],
      test_suite='test',
      tests_require=[
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
