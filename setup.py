from setuptools import setup

setup(
        name='helloworls',
        inclide_package_data=True,
        version='0.test.1',
        description='Hello!',
        py_module=["hello"],
        packages=['src'],
        package_data={
        'src': ['dockerfile'],
        '':['gregdelanis/hello_py:1.0'],
        },
        package_dir={'src':'src'},
)
