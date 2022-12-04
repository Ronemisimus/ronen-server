from setuptools import setup

setup(
    name="ronen-server",
    version="0.0.1",
    description="Greet the world.",
    py_modules=["hello","server","calculate","stack","global_strings"],
    install_requires=['flask','waitress'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": ["hello=hello:main"],
    },
)