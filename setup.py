from setuptools import setup, find_packages

packages = find_packages()
setup(
    name="carta-work-tests",
    version="0.1",
    packages=packages,
    package_data={k: ["*.csv", "*.yml", "*.html"] for k in packages},
    scripts=[],
    entry_points={},
)
