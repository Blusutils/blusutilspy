import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blusutils",
    version="0.0.1.1",
    author="Blusutils",
    author_email="contact@blusutils.net",
    description="Library with random functionality.",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blusutils/blusutilspy",
    project_urls={
        "Bug Tracker": "https://github.com/Blusutils/blusutilspy/issues",
        'Blusutils GitHub': 'https://github.com/Blusutils/',
        'Blusutils Website': 'https://blusutils.net'
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    packages=setuptools.find_packages(where='.'),
    python_requires=">=3.9",
    install_requires = ['rapidjson'],#(reqs:=open('requirements.txt')).readlines(),
    zip_save = False
)
#reqs.close()