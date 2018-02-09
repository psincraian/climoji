from setuptools import setup, find_packages

setup(
    name="climoji",
    version="1.0",
    packages=find_packages(),
    author="Petru Rares Sincraian",
    author_email="psincraian@gmail.com",
    description="A cli emoji finder",
    keywords="emoji cli finder",
    license="MIT",
    entry_points={
        'console_scripts': [
            'climoji = climoji.infrastructure:cli'
        ]
    },
)
