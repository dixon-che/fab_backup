from setuptools import setup


setup(
    name='fab_backup',
    version='0.1',
    url='https://github.com/dixon-che/fab_backup',
    license='MIT',
    author='Aleksey Radchenko',
    author_email='dixon.che@gmail.com',
    description='fab functions for backups db and files to remote server',
    long_description=__doc__,
    zip_safe=True,
    py_modules=[
        'fab_backup'
    ],
    zip_safe=True,
    install_requires=[
        'fabric',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
