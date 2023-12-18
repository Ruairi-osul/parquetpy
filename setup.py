from setuptools import setup, find_packages

# Read requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="parquetpy",
    version="0.1.0",
    description="CLI for basic operations on Parquet files",
    author="Ruairi O'Sullivan",
    author_email="ruairi.osullivan.work@gmail.com",
    url="https://github.com/yourusername/parquetpy",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={"console_scripts": ["parquetpy = parquetpy.app:app"]},
)
