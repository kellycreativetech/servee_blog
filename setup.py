from setuptools import setup

# see requirements.txt for dependencies



setup(
    name = "biblion",
    version = "0.1.1.dev7",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    description = "the eldarion.com blog app intended to be suitable for site-level company and project blogs",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/eldarion/biblion",
    packages = [
        "biblion",
        "biblion.templatetags",
        "biblion.migrations",
    ],
    package_data = {
        "biblion": [
            "templates/biblion/*.xml",
            "templates/biblion/*.html",
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
