from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')
# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='dgenies',
    version='0.9',
    packages=find_packages('src'),
    package_dir={'dgenies': 'src/dgenies'},
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
    data_files=[('/etc/dgenies', ['application.properties'])],
    scripts=['bin/dgenies'],
)
