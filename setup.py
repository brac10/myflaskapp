from setuptools import setup, find_packages
import setuptools
 
TEST_DEPENDENCIES = [
    "isort>=4.2.4,<5",
    "pylint==1.9.5",
    "valildator==0.7.0",
    "validators==0.18.2",
    "pytask==1.0.2",
    "pytest==3.0.7"
]
EXTRA_DEPENDENCIES = {
    "test": TEST_DEPENDENCIES,
    "test:python_version>='3.7'": ["black==19.10.b0", "tox=3.14.6"],
}
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="myflaskapp", # Replace with your own username
    version="1.0.0",
    author="Scott Braconnier",
    author_email="Scott.Braconnier@Centauricorp.com",
    description="Example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "six==1.15.0",
        "click==7.1.2",
        "ruamel.yaml[jinja2]==0.16.10",
        "wtforms==2.3.3",
        "ipaddress==1.0.16",
        "flask==1.1.2",
        "hvac==0.9.2",
        "pycurl==7.43.0.0"
    ]
)
 
