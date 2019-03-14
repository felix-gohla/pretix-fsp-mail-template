import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix_fsp_mail',
    version='0.1.0',
    description='Dieses Plugin beinhaltet eine E-Mail Vorlage für den FSP Ticket Shop.',
    long_description=long_description,
    url='https://gitlab.hpi.de/felix.gohla/pretix_fsp_mail',
    author='Felix Gohla',
    author_email='felix.gohla@gmail.com',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_fsp_mail=pretix_fsp_mail:PretixPluginMeta
""",
)
