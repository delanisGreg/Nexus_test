from setuptools import setup

setup(
        name='helloworls',
        inclide_package_data=True,
        version='0.test.2',
        description='Hello!',
        py_module=["hello"],
        packages=['src'],
        package_data={
        'src': ['dockerfile'],
        },
        package_dir={'src':'src'},
)
