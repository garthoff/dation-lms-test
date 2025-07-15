from setuptools import setup, find_packages
import re
import ast

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# extract version string from branded_lms/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open("branded_lms/__init__.py", "rb") as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode("utf-8")).group(1)))

setup(
    name="branded_lms",
    version=version,
    description="LMS App",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
