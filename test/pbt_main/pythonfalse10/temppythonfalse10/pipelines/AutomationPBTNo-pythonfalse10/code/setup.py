from setuptools import setup, find_packages

setup(
    name='AutomationPBTNo-pythonfalse10',
    version='1.0',
    packages=find_packages(include=['automationpbtnopythonfalse10*']),
    description='AutomationPBTNo-pythonfalse10',
    install_requires=[
        'prophecy-libs==1.9.35'
    ],
    entry_points={
        'console_scripts': [
            'main = automationpbtnopythonfalse10.pipeline:main',
        ],
    },
    data_files=[(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)