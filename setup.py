from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.2",
    author="genbid007",
    description="ANN implementation with Tensorboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="#",
    author_email="genbid007.ml@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)