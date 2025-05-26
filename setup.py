from setuptools import setup, find_packages

setup(
    name="myapp",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'flask==2.0.3',
        'werkzeug==2.0.3',
    ],
)