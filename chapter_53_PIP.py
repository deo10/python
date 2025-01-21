# Working with PIP - package manager for python

# get list of installed packages
#-> pip3 list

# Package Version
# ------- -------
# pip     24.2

# install package
#-> pip3 install [package_name] 

# install ecxact version
#-> pip3 install [package_name==2.1.3.dev8] 

# after instllation we can use it in code
# import [package_name]

# create virt env via PIPENV
#-> pip3 install pipenv

# install package into virt env
# create folder .venv
# install package
# pipenv install requests

# it's not present globally
#-> pip3 list
# requests package not present

# activate pipenv shell run command:
# pipenv shell

# check list of packages:
#-> pip3 list
# requests package is present

# required files to recreate virt env are:
# - Pipfile
# - Pipfile.lock

# folder .venv is not required
# to recreate use 
# pipenv install

# to see all package dependecies use:
# pipenv graph
# requests==2.32.3
# ├── certifi 
# ├── charset-normalizer 
# ├── idna 
# └── urllib3 

# GPT Reply on topic:
# As a DevOps engineer, it's essential to have a solid understanding of PIP and Pipenv, as they are critical tools for managing Python packages and virtual environments. Here are some key aspects to know and real tasks that you may face:

# PIP (Python Package Installer):

# Package Installation and Management: PIP is the package installer for Python that allows you to install and manage libraries and dependencies for your Python projects. As a DevOps engineer, you might need to automate the installation of these packages as part of your deployment pipeline or ensure that the correct versions of packages are installed in different environments (e.g., development, testing, production).

# Requirements Files: You may encounter tasks that involve the creation and maintenance of requirements.txt files, which list all the necessary Python packages. These files ensure that all environments run the same versions of packages, minimizing "works on my machine" issues.

# Upgrading and Removing Packages: You should know how to upgrade packages to newer versions and how to remove unneeded packages. This is especially important for managing security vulnerabilities in dependencies.

# Pipenv:

# Virtual Environment Management: Pipenv combines package management and virtual environment management into one tool. As a DevOps engineer, you might need to set up isolated Python environments using Pipenv to ensure that each project has its own dependencies, separate from other projects.

# Pipfile and Pipfile.lock: You should be familiar with these two files. Pipfile replaces requirements.txt and is used to track which packages your project needs. Pipfile.lock is used to ensure deterministic builds by recording the exact versions of packages installed in your environment.

# Integration with CI/CD Pipelines: You may need to integrate Pipenv into your continuous integration and deployment pipelines. This might involve configuring CI tools to use Pipenv for setting up environments and installing dependencies during builds.

# Security and Compliance Checking: Pipenv provides built-in support for checking installed packages against known security vulnerabilities. Understanding how to use these features can be crucial for maintaining the security of your applications.

# Real Tasks Examples:

# Automating Environment Setup: Write scripts that use PIP to automatically set up Python environments and install all necessary dependencies when deploying an application.

# Dependency Updating: Create a routine operation that checks for outdated packages, updates them, and tests the application to ensure that the updates don't break anything.

# Integrating Pipenv with Docker: When using Docker containers, you might need to ensure that the Dockerfile correctly sets up Pipenv, installs dependencies from the Pipfile, and uses the locked versions from Pipfile.lock.

# Environment Bootstrapping for Development Teams: Ensure every member of the development team can bootstrap their local development environment with a single command using Pipenv, guaranteeing consistency across all developers' machines.

# Handling Dependency Conflicts: Resolve conflicts between packages that require different versions of the same dependency.

# By understanding how to leverage PIP and Pipenv effectively in these tasks, you can significantly improve the reliability, reproducibility, and security of your Python projects in a DevOps context.