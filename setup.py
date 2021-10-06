import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'unMinable',
    version = '0.0.1',
    author = 'Andrea Previtali',
    author_email = 'andreafprevitali@gmail.com',
    description = 'unMinable calculator',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'http://github.com/1marte/unMinable',
    project_urls = {
    },
    license = 'MIT',
    packages = ['unMinable'],
    install_requires = ['requsts', 'binance'],
)
