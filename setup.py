import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abcexp",
    version="1.0",
    author="Rohan Gala",
    description="Exploratory analysis of the ABC dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["abcexp"],
    python_requires='>=3.8',
)