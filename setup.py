from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    __long_description:str = f.read()

__version = "0.0.1"

requirements = [
    'fastapi>=0.62.0',
    'SQLAlchemy==1.4.35',
    'django==4.1.6'
]

setup(
    name='simple_crud_py_api',
    version=__version,
    description='Simple CRUD API developed in Python',
    license="MIT",
    long_description=__long_description,
    long_description_content_type='text/markdown',
    author='Lucas Machado',
    url='https://github.com/lfjmachado/simple-crud-py-api',
    download_url='https://github.com/lfjmachado/simple-crud-py-api.git',
    packages=find_packages(exclude=['tests','tests.*']),
    python_requires='>=3.7',
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    keywords=[
        "cookiecutter",
        "Python",
        "projects",
        "project templates",
        "Jinja2",
        "skeleton",
        "scaffolding",
        "project directory",
        "package",
        "packaging",
    ],
)
# setup.py sdist bdist_wheel