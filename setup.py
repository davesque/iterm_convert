from setuptools import setup


setup(
    name='iterm_convert',
    version='0.1',
    description='iTerm color scheme conversion tools',
    keywords='iterm convert color scheme',
    url='http://github.com/davesque/iterm_convert',
    author='David Sanders',
    author_email='davesque@gmail.com',
    license='MIT',
    packages=['iterm_convert'],
    install_requires=[
        'lxml',
        'cssselect',
        'pyyaml',
    ],
    zip_safe=False,
)
