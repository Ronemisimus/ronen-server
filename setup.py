from setuptools import setup


setup(name="ronen-server",
    version=0.1,
    description="a calculator server",
    url="https://github.com/Ronemisimus/ronen-server",
    author="Ronen Margolin",
    license="MIT",
    packages=["ronen-server"],
    install_requires=[
        'flask',
        'waitress'
    ],
    zip_safe=False)