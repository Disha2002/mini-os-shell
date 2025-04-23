from setuptools import setup, find_packages

setup(
    name="mini-os-shell",  # Name of the project
    version="0.1.0",  # Version of the project
    description="A Python-based shell with process management, system monitoring, and task scheduling.",
    author="Disha Kemparaju",
    author_email="your.email@example.com",  # Your email address
    url="https://github.com/yourusername/mini-os-shell",  # URL for the project (GitHub repo, for example)
    packages=find_packages(),  # Automatically discover and include all packages in the project
    install_requires=[  # Dependencies that are required to run the project
        "psutil==5.9.4",
        "subprocess32==3.5.4",  # If using subprocess32 instead of the default subprocess (for older Python versions)
    ],
    classifiers=[  # Classifiers to help users discover your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change to your license if necessary
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # The Python version required
)
