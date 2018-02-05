from setuptools import setup, find_packages
setup(
    name="climoji",
    version="1.0",
    packages=find_packages(),
    author="Petru Rares Sincraian",
    description="A cli emoji finder",
    keywords="emoji cli finder",
    entry_points={
        'console_scripts': [
            'climoji = climoji.infrastructure:cli'
        ]
    }
)
