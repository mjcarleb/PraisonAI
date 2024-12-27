# test_env.py

import sys
import pkg_resources

def test_environment():
    print(f"Python Version: {sys.version}")
    print(f"Python Path: {sys.executable}")
    
    # Check core dependencies
    required_packages = [
        "rich",
        "markdown",
        "pyparsing",
        "praisonaiagents",
        "python-dotenv",
        "instructor",
        "PyYAML"
    ]
    
    print("\nChecking core dependencies:")
    for package in required_packages:
        try:
            version = pkg_resources.get_distribution(package).version
            print(f"✓ {package}: {version}")
        except pkg_resources.DistributionNotFound:
            print(f"✗ {package}: Not found")

    # Check if optional dependencies are installed
    optional_groups = [
        "ui",
        "gradio",
        "api",
        "agentops",
        "google",
        "openai",
        "anthropic",
        "cohere",
        "chat",
        "code",
        "realtime",
        "call",
        "crewai",
        "autogen"
    ]
    
    print("\nChecking optional dependency groups:")
    for group in optional_groups:
        try:
            # Try to import a key package from each group
            if group == "ui" or group == "chat" or group == "code":
                import chainlit
                print(f"✓ {group}")
            elif group == "gradio":
                import gradio
                print(f"✓ {group}")
            elif group == "api":
                import flask
                print(f"✓ {group}")
            elif group == "openai":
                import openai
                print(f"✓ {group}")
            elif group == "crewai":
                import crewai
                print(f"✓ {group}")
            elif group == "autogen":
                import autogen
                print(f"✓ {group}")
            else:
                print(f"? {group} (status unknown)")
        except ImportError:
            print(f"✗ {group}")

if __name__ == "__main__":
    test_environment()