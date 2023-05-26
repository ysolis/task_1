from setuptools import find_packages, setup

setup(
    name='package_module_b',
    version='0.0.1',
    description='Package Module B',
    author='Yonsy Solis',
    author_email='yonsy.solis@outlook.com',
    install_requires=[],
    packages=find_packages(
        where='.',
        include=['package_module_b'],
        exclude=['package_module_b.tests'],
    ),
    python_requires='>3.6',
)
