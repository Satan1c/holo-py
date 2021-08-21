import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="holo_py",
    version="1.0.0",
    author="Satan1c",
    author_email="satan1c@ukr.net",
    description="An async wrapper for Holo API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Satan1c/holo-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.6",
)
