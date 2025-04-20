from setuptools import setup

setup(
    name="github-activity",
    version="0.1",
    py_modules=["github_activity"],
    install_requires=["typer[all]", "requests"],
    entry_points={
        "console_scripts": [
            "github-activity = github_activity:app",
        ],
    },
)