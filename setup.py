from setuptools import setup, find_packages

setup(
    name="arctis",
    version="0.0.0",
    description="A python library for Arctis headsets",
    url="https://github.com/ShayBox/Arctis.git",
    license="MIT",
    author="Shayne Hartford",
    packages=find_packages(),
    install_requires=["hidapi"],
    entry_points={
        "console_scripts": ["arctis=arctis.main:main"],
    },
)
