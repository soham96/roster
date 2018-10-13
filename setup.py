import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roster",
    version="0.0.1",
    author="Soham Chatterjee",
    author_email="96soham96@gmail.com",
    description="CLI for scheduling jobs for DL/ML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soham96/chum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
