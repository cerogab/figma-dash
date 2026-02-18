from setuptools import setup, find_packages

setup(
    name="figma-dash",
    version="0.1.0",
    description="A tool to outline design features from Figma files",
    author="cerogab",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "figma-dash=figma_dash.cli:main",
        ],
    },
    python_requires=">=3.7",
)
