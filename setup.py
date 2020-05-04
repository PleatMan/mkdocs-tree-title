from setuptools import setup, find_packages


setup(
    name='mkdocs-tree-title',
    version='0.1.1',
    description='A MkDocs plugin to add the tree titles on pages',
    long_description='A MkDocs plugin that adds a tree title for each page. It is composed from the ancestors tree titles and the page title and it is set on the page as tree_title attribute.',
    keywords='mkdocs',
    url='https://github.com/PleatMan/mkdocs-tree-title',
    author='George B',
    author_email='pleat_man@yahoo.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'tree-title = mkdocs_tree_title.plugin:TreeTitlePlugin'
        ]
    }
)
