from setuptools import setup, find_packages

setup(
    name='data-pipeline-helper',
    version='0.1.0',
    author='Gowtham SB',
    author_email='thedatatech.in@gmail.com',
    description='A helper library for building and managing data pipelines',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/data-pipeline-helper',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'boto3',
    ],
)
