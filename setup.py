from setuptools import setup, find_packages

# Dynamically calculate the version based on django.VERSION.
version = __import__('poll').get_version()

print find_packages()

setup(
    name='calixos-poll',
    version=version,
    description='djangoCMS Poll',
    author='Thomas Meitz',
    author_email='calixos@web.de',
    url='https://github.com/retailif/calixos-poll',
    download_url='https://github.com/retailify/calixos-poll/tarball/v1.0.0',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
)
