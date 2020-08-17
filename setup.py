import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bsd-builder-cloudbsdorg",  # Replace with your own username
    version="0.0.1",
    author="Mark LaPointe",
    author_email="mark@cloudbsd.org",
    description="Build a distribution based on FreeBSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudbsdorg/bsd-builder",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System',
        'Topic :: System :: Installation/Setup',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: FreeBSD',
    ],
    python_requires='>=3.7',
)
