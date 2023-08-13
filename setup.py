import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imdbmovies",
    version="0.1.1",
    author="safevideo",
    description="IMDB API for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/safevideo/imdbmovies",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=["beautifulsoup4"]
)
