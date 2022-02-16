import setuptools

setuptools.setup(
    name="ASTBuilderFib",
    version="2.0",
    author="Sheremeev Andrey",
    description="AST builder",
    url="https://github.com/shershen0/Advanced_Python",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)