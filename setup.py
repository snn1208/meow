from setuptools import setup, find_packages

setup(
    name="myapp",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'flask==2.0.3',
        'werkzeug==2.0.3',
    ],
    python_requires='>=3.9',
)