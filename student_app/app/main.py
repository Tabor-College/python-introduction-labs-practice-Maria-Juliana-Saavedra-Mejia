import sys
import requests 

def greet(name: str) -> str:
    return f"Hello, {name}! Running inside the Docker"

def check_version() -> str:
    return f"Request vesion: {requests.__version__}"

if __name__ == "__main__":
    name= sys.argv[1] if len(sys.argv) > 1 else "Student"
    print(greet(name))
    print(check_version()) 