from setuptools import setup
# see requirements.txt for dependencies

setup(
    name = "servee_blog",
    version = "0.1.1.dev9",
    author = "Servee LLC, Bibilion (the base) originally by Eldarion",
    author_email = "issac@servee.com",
    description = "The Servee Blog was originally extacted from servee_blog",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/servee/servee_blog",
    packages = [
        "servee_blog",
        "servee_blog.templatetags",
        "servee_blog.migrations",
    ],
    package_data = {
        "servee_blog": [
            "templates/servee_blog/*.xml",
            "templates/servee_blog/*.html",
            "fixtures/*.json",
        ]
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
