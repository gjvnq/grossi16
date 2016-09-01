#!/usr/bin/env python3

from setuptools import setup, find_packages
setup(name='grossi16',
      version='0.0.2',
      description='An open-source easy to use classroom clicker system',
      author='Gabriel Queiroz',
      author_email='gabrieljvnq@gmail.com',
      license='MIT',
      package_dir={'gorssi16': 'grossi16'},
      package_data={'grossi.web': ['static/*.css', 'static/*.js', 'static/*.woff2', 'templates/*.html']},
      packages=['grossi16.web', 'grossi16.cli'],
      zip_safe=True,
      include_package_data=True,
      install_requires=[
        'flask==0.11.1',
        'click==6.6',
        'CommonMark==0.7.2',
        'FilterHTML==0.5.0'
      ],
      entry_points={
          'console_scripts': [
              'grossi16-cli=grossi16.cli:main'
          ],
          'setuptools.installation': [
              'eggsecutable=grossi16.cli:main'
          ],
      })
