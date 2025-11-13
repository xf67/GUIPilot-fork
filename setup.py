from setuptools import setup, find_packages
from pathlib import Path
import yaml
import re

HERE = Path(__file__).parent

def load_long_description() -> str:
    readme = HERE / "README.md"
    return readme.read_text(encoding="utf-8") if readme.exists() else ""

def parse_requirements_txt(path: Path):
    reqs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # ignore -e, git+ urls are preserved
        if line.startswith("-e"):
            continue
        reqs.append(line)
    return reqs

def load_install_requires():
    req_file = HERE / "requirements.txt"
    if req_file.exists():
        return parse_requirements_txt(req_file)

    env_file = HERE / "environment.yml"
    if env_file.exists():
        try:
            data = yaml.safe_load(env_file.read_text(encoding="utf-8"))
            deps = data.get("dependencies", []) or []
            install = []
            for d in deps:
                if isinstance(d, str):
                    # conda style "package=version" -> "package>=version" fallback
                    install.append(re.sub(r"=+", ">=", d, count=1))
                elif isinstance(d, dict) and "pip" in d:
                    install.extend(d["pip"])
            return install
        except Exception:
            pass

    # Fallback common dependencies (conservative)
    return [
        "numpy",
        "opencv-python",
        "Pillow",
        "python-dotenv",
        "pydantic",
        "ultralytics",
        "supervision",
    ]

setup(
    name="guipilot",
    version="0.1.0",
    description="GUIPilot: Consistency-based Mobile GUI Testing",
    long_description=load_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/guipilot",
    author="GUIPilot Authors",
    license="MIT",
    packages=find_packages(exclude=("tests", "examples")),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=load_install_requires(),
    extras_require={
        "dev": ["black", "isort", "flake8", "pre-commit"],
        "test": ["pytest", "pytest-cov"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)