from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="climoji",
    version="2.0.1",
    packages=find_packages(),
    author="Petru Rares Sincraian",
    author_email="psincraian@gmail.com",
    description="A cli emoji finder",
    keywords="emoji cli finder",
    long_description=long_description,
    url="https://github.com/psincraian/climoji",
    license="MIT",
    entry_points={
        'console_scripts': [
            'climoji = climoji.infrastructure:cli'
        ]
    },
    install_requires=[
        'click>=6.7,<7', 'editdistance<1.0'
    ]
)
