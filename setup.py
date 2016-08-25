#!/usr/bin/env python3

from setuptools import setup, find_packages
setup(name='grossi16',
      description='An open-source easy to use classroom clicker system',
      author='Gabriel Queiroz',
      author_email='gabrieljvnq@gmail.com',
      license='MIT',
      package_dir={'gorssi16': 'grossi16'},
#      package_data={'grossi16': ['tex_packages/*.sty', 'tex_packages/emoji/pdf/*.pdf', 'web_files/*.css', 'web_files/*.html', 'web_files/*.css', 'web_files/*.js']},
      packages=['grossi16'],
      include_package_data=True,
      install_requires=['flask'],
      entry_points={
          'console_scripts': [
              'grossi16=grossi16:main'
          ],
          'setuptools.installation': [
              'eggsecutable=grossi16:main'
          ],
      })
