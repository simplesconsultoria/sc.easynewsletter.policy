# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

version = '1.0.3'

setup(name='sc.easynewsletter.policy',
      version=version,
      description="Policy configuration for Products.EasyNewsletter",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='python simples_consultoria',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='http://www.simplesconsultoria.com.br',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['sc', 
                         'sc.easynewsletter'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'five.grok',
          # -*- Extra requirements: -*-
          'Products.EasyNewsletter>2.6.1'
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )