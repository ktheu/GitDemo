#!/usr/bin/env python3
"""
File operations example in Python.
Demonstrates reading and writing files.
"""

import os

def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Written to {filename}")

def read_file(filename):
    """Read and return content from a file."""
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        return f.read()

def append_to_file(filename, content):
    """Append content to a file."""
    with open(filename, 'a') as f:
        f.write(content)
    print(f"Appended to {filename}")

def main():
    """Demonstrate file operations."""
    filename = "example.txt"
    
    print("File Operations Demo")
    print("====================")
    
    # Write to file
    write_file(filename, "Hello from Python!\n")
    
    # Read from file
    content = read_file(filename)
    print(f"Content: {content}")
    
    # Append to file
    append_to_file(filename, "This is an additional line.\n")
    
    # Read again
    content = read_file(filename)
    print(f"Updated content:\n{content}")
    
    # Clean up
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Cleaned up {filename}")

if __name__ == "__main__":
    main()
