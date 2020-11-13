from setuptools import setup

setup(
    name="TOPSIS-PARNEET-101803281",
    packages=["TOPSIS-PARNEET-101803281"],
    version="0.1",
    description="TOPSIS IMPLEMENTAION python package ",
    url="https://github.com/parneetpp/Topsis-implementstion",
    download_url="https://github.com/jasmehakKaur/TOPSIS_PYTHON/archive/v_0.1.tar.gz",
    author="Parneet Singh",
    author_email="psingh3_be18@thapar.edu",
    license="MIT",
    keywords = ['IMPLEMENTATION','TOPSIS','PYTHON'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=[
                      'numpy',
                      'pandas'
    
        ],

)
