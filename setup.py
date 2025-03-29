from setuptools import setup, find_packages

setup(
    name="PyCodeObfuscator",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "PyCodeObfuscator=PyCodeObfuscator.PCO:main",
        ],
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
