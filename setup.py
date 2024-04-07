from setuptools import setup, find_packages

_long_description = ''
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        _long_description = f.read()
except Exception as e:
    _long_description = ''

setup(
    name='gpti',
    version='1.4',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='yandricr',
    author_email='yandribret@gmail.com',
    description='This package simplifies your interaction with various GPT models, removing the need for tokens or other methods to access GPT',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yandricr/gpti-py/',
    project_urls={
        'Documentation': 'https://nexra.aryahcr.cc/',
        'Funding': 'https://ko-fi.com/yandricr',
        'Source': 'https://github.com/yandricr/gpti-py/'
    },
    keywords='gpt gpt-3 gpt-3.5 gpt-4 gpti gpt-free ai generate-image prodia bing chat stream dalle dalle-2 llama-2 stable-diffusion pixart EMI render3d pixel-art playground animagine-xl',
    license='MIT',
    package_data={'': ['LICENSE']},
    include_package_data=True
)