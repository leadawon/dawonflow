from setuptools import setup

setup(
    name = "dwfw",
    version="0.0.1",
    description = "ML/DL/NLP library for python",
    url = "https://github.com/leadawon/dawonflow.git",
    author="LEEDAWON",
    author_email = "dawon337@gmail.com",
    license = "dawonlicense",
    packages = ["dwfw"],
    zip_safe = False,
    install_requires = [
        "numpy==1.21.6"
    ]
)