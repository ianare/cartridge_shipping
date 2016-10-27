import io
import sys
from setuptools import setup, find_packages
from shutil import rmtree

from cartridge_shipping import __version__ as version

if sys.argv[:2] == ["setup.py", "bdist_wheel"]:
    # Remove previous build dir when creating a wheel build,
    # since if files have been removed from the project,
    # they'll still be cached in the build dir and end up
    # as part of the build, which is really neat!
    try:
        rmtree("build")
    except:
        pass


long_description = (
    io.open('README.rst', encoding='utf-8').read()
)

setup(
    name='cartridge_shipping',
    version=version,
    description="Multiple zone shipping handler for Cartridge.",
    long_description=long_description,
    maintainer="Ianaré Sevi",
    license="LGPLv3+",
    url="https://github.com/ianare/cartridge_shipping",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    keywords='django mezzanine cartridge shipping',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'cartridge >= 0.12',
    ],
    extras_require=dict(
        countries_utf8_sorting=['pyuca'],
    ),
)
