import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = []
with open("requirements.txt") as req_f:
    for line in req_f:
        requirements.append(line.strip())


setuptools.setup(
    name="cache_manager",
    version="0.0.1",
    author="Chenyu Zhang",
    author_email="goodzhcy@gmail.com",
    description="A small python package for managing (downloading) cache files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChenyuZhang16/cache_manager",
    project_urls={
        "Bug Tracker": "https://github.com/ChenyuZhang16/cache_manager/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    install_requires=requirements
)
