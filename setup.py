from setuptools import setup, find_packages
import os

version = "0.1"

setup(
    name="arv.pypes",
    version=version,
    description="Python data pipes.",
    long_description=(
        open("README.txt").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords="",
    author="Alexis Roda",
    author_email="alexis.roda.villalonga@gmail.com",
    url="",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["arv"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
    ],
    entry_points={
        # -*- Entry points: -*-
    },
)
