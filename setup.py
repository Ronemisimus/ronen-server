from setuptools import setup

setup(
    name="ronen-server",
    version="0.0.1",
    description="Greet the world.",
    py_modules=["main","server","calculate","stack","global_strings","logs","log_manager"],
    install_requires=['flask','waitress'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": ["main=main:start_server"],
    },
)