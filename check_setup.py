from importlib.metadata import version

packages = [
    "langchain",
    "langchain-community",
    "langchain-text-splitters",
    "langchain-chroma",
    "langchain-google-genai",
    "pypdf",
    "python-dotenv",
]

for package in packages:
    print(f"{package}: {version(package)}")

print("\nEnvironment setup successful.")