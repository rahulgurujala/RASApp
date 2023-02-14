from setuptools import setup, find_packages

setup(
    name="rasApp",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi==0.91.0",
        "pydantic==1.10.4",
        "PyMySQL==1.0.2",
        "SQLAlchemy==2.0.3",
        "uvicorn==0.20.0",
        "Werkzeug==2.2.2",
        "python_dateutil==2.8.2",
        "pytest==7.2.1",
        "factory-boy==3.2.1",
    ],
)
