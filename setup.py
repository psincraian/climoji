from setuptools import setup, find_packages

setup(
    name="climoji",
    version="1.0.1",
    packages=find_packages(),
    author="Petru Rares Sincraian",
    author_email="psincraian@gmail.com",
    description="A cli emoji finder",
    keywords="emoji cli finder",
    url="https://github.com/psincraian/climoji",
    license="MIT",
    entry_points={
        'console_scripts': [
            'climoji = climoji.infrastructure:cli'
        ]
    },
    install_requires=[
        'click>=6.7,<7'
    ]
)
