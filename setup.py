from setuptools import setup


setup(
    name='iterm_convert',
    version='0.1',
    description='iTerm color scheme conversion tools',
    url='http://github.com/davesque/iterm-convert',
    author='David Sanders',
    author_email='davesque@gmail.com',
    license='MIT',
    packages=['iterm_convert'],
    install_requires=[
        'lxml',
        'cssselect',
    ],
    zip_safe=False,
)
