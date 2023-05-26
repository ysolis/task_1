from setuptools import find_packages, setup

setup(
    name='package_module_a',
    version='0.0.1',
    description='Package Module A',
    author='Yonsy Solis',
    author_email='yonsy.solis@outlook.com',
    install_requires=[],
    packages=find_packages(
        where='.',
        include=['package_module_a'],
        exclude=['package_module_a.tests'],
    ),
    python_requires='>3.6',
)
