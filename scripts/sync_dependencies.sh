#!/bin/bash

###############################################################################
# sync_dependencies.sh
#
# This script automatically analyzes Python files in the utilskit package,
# identifies their third-party dependencies, and updates both requirements.txt
# and pyproject.toml with categorized dependencies.
#
# Usage: ./scripts/sync_dependencies.sh
###############################################################################

set -e  # Exit on error

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get the project root directory (parent of scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
UTILSKIT_DIR="$PROJECT_ROOT/utilskit"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Dependency Synchronization Tool${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${YELLOW}Project Root:${NC} $PROJECT_ROOT"
echo -e "${YELLOW}Source Directory:${NC} $UTILSKIT_DIR"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 is not installed or not in PATH${NC}"
    exit 1
fi

# Create a Python script to analyze dependencies
TEMP_ANALYZER=$(mktemp /tmp/analyze_deps.XXXXXX.py)

cat > "$TEMP_ANALYZER" << 'PYTHON_SCRIPT'
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# Python standard library modules (Python 3.10+)
STDLIB_MODULES = {
    'abc', 'aifc', 'argparse', 'array', 'ast', 'asynchat', 'asyncio', 'asyncore',
    'atexit', 'audioop', 'base64', 'bdb', 'binascii', 'binhex', 'bisect', 'builtins',
    'bz2', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs',
    'codeop', 'collections', 'colorsys', 'compileall', 'concurrent', 'configparser',
    'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt', 'csv', 'ctypes',
    'curses', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis',
    'distutils', 'doctest', 'email', 'encodings', 'enum', 'errno', 'faulthandler',
    'fcntl', 'filecmp', 'fileinput', 'fnmatch', 'formatter', 'fractions', 'ftplib',
    'functools', 'gc', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib', 'grp',
    'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'imaplib', 'imghdr', 'imp',
    'importlib', 'inspect', 'io', 'ipaddress', 'itertools', 'json', 'keyword',
    'lib2to3', 'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap',
    'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 'multiprocessing',
    'netrc', 'nis', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'ossaudiodev',
    'parser', 'pathlib', 'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil',
    'platform', 'plistlib', 'poplib', 'posix', 'posixpath', 'pprint', 'profile',
    'pstats', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'queue', 'quopri',
    'random', 're', 'readline', 'reprlib', 'resource', 'rlcompleter', 'runpy',
    'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal',
    'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'spwd', 'sqlite3',
    'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess',
    'sunau', 'symbol', 'symtable', 'sys', 'sysconfig', 'syslog', 'tabnanny',
    'tarfile', 'telnetlib', 'tempfile', 'termios', 'test', 'textwrap', 'threading',
    'time', 'timeit', 'tkinter', 'token', 'tokenize', 'tomllib', 'trace', 'traceback',
    'tracemalloc', 'tty', 'turtle', 'turtledemo', 'types', 'typing', 'unicodedata',
    'unittest', 'urllib', 'uu', 'uuid', 'venv', 'warnings', 'wave', 'weakref',
    'webbrowser', 'winreg', 'winsound', 'wsgiref', 'xdrlib', 'xml', 'xmlrpc',
    'zipapp', 'zipfile', 'zipimport', 'zlib', '_thread'
}

def extract_imports(file_path):
    """Extract import statements from a Python file."""
    imports = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match: import module
        # Match: from module import ...
        import_pattern = r'^(?:from\s+(\S+)|import\s+(\S+))(?:\s+|$)'

        for line in content.split('\n'):
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue

            match = re.match(import_pattern, line)
            if match:
                module = match.group(1) or match.group(2)
                # Get the top-level package
                top_level = module.split('.')[0]
                imports.add(top_level)
    except Exception as e:
        print(f"Warning: Error reading {file_path}: {e}", file=sys.stderr)

    return imports

def get_module_dependencies(base_dir):
    """Analyze all Python files and categorize dependencies by module."""
    module_deps = defaultdict(set)
    base_path = Path(base_dir)

    # Find all Python files
    for py_file in base_path.rglob('*.py'):
        # Skip __pycache__ and test files
        if '__pycache__' in str(py_file) or 'test' in str(py_file):
            continue

        # Get the module name (first subdirectory under utilskit/)
        try:
            rel_path = py_file.relative_to(base_path)
            if len(rel_path.parts) > 1:
                module_name = rel_path.parts[0]
            else:
                module_name = 'core'
        except ValueError:
            continue

        # Extract imports
        imports = extract_imports(py_file)

        # Filter out standard library and local imports
        third_party = {imp for imp in imports
                      if imp not in STDLIB_MODULES
                      and not imp.startswith('utilskit')}

        module_deps[module_name].update(third_party)

    return module_deps

def normalize_package_name(pkg):
    """Normalize package names to their PyPI equivalents."""
    mapping = {
        'git': 'GitPython',
        'sqlalchemy': 'SQLAlchemy',
        'yaml': 'PyYAML',
    }
    return mapping.get(pkg, pkg)

def get_package_versions():
    """Get minimum version requirements for packages."""
    versions = {
        'numpy': '>=2.0.0',
        'pandas': '>=2.0.0',
        'matplotlib': '>=3.0.0',
        'pymysql': '>=1.1.0',
        'SQLAlchemy': '>=2.0.0',
        'semver': '>=3.0.0',
        'GitPython': '>=3.1.0',
        'openai': '>=2.0.0',
        'openpyxl': '>=3.0.0',
        'xlrd': '>=2.0.0',
    }
    return versions

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_deps.py <utilskit_directory>")
        sys.exit(1)

    utilskit_dir = sys.argv[1]

    if not os.path.isdir(utilskit_dir):
        print(f"Error: {utilskit_dir} is not a valid directory")
        sys.exit(1)

    print("Analyzing Python files for dependencies...")
    module_deps = get_module_dependencies(utilskit_dir)

    # Collect all unique dependencies
    all_deps = set()
    for deps in module_deps.values():
        all_deps.update(deps)

    # Normalize package names
    all_deps = {normalize_package_name(pkg) for pkg in all_deps}

    # Get version requirements
    versions = get_package_versions()

    # Print results as JSON-like format for parsing
    print("===MODULE_DEPS===")
    for module, deps in sorted(module_deps.items()):
        normalized_deps = sorted([normalize_package_name(d) for d in deps])
        print(f"{module}:{','.join(normalized_deps)}")

    print("===ALL_DEPS===")
    for dep in sorted(all_deps):
        version = versions.get(dep, '>=1.0.0')
        print(f"{dep}{version}")

    print("===CORE_DEPS===")
    # Core dependencies used by multiple modules
    core_deps = ['numpy', 'pandas']
    for dep in core_deps:
        if dep in all_deps:
            version = versions.get(dep, '>=1.0.0')
            print(f"{dep}{version}")

if __name__ == '__main__':
    main()
PYTHON_SCRIPT

echo -e "${YELLOW}Step 1:${NC} Analyzing Python files..."
# Run the analyzer and capture output
ANALYSIS_OUTPUT=$(python3 "$TEMP_ANALYZER" "$UTILSKIT_DIR" 2>&1)

# Check if analysis was successful
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to analyze dependencies${NC}"
    echo "$ANALYSIS_OUTPUT"
    rm -f "$TEMP_ANALYZER"
    exit 1
fi

echo "$ANALYSIS_OUTPUT" | grep -v "^===" | grep -v "Analyzing"
echo ""

# Parse the output
MODULE_DEPS=$(echo "$ANALYSIS_OUTPUT" | sed -n '/===MODULE_DEPS===/,/===ALL_DEPS===/p' | grep -v "^===")
ALL_DEPS=$(echo "$ANALYSIS_OUTPUT" | sed -n '/===ALL_DEPS===/,/===CORE_DEPS===/p' | grep -v "^===")
CORE_DEPS=$(echo "$ANALYSIS_OUTPUT" | sed -n '/===CORE_DEPS===/,$p' | grep -v "^===")

echo -e "${YELLOW}Step 2:${NC} Generating requirements.txt..."

# Generate requirements.txt
cat > "$PROJECT_ROOT/requirements.txt" << EOF
# Core dependencies (used by multiple modules)
$(echo "$CORE_DEPS" | sort)

# Database utilities (dbutils)
$(echo "$ALL_DEPS" | grep -E "^(pymysql|SQLAlchemy)")

# Plotting utilities (plotutils)
$(echo "$ALL_DEPS" | grep "^matplotlib")

# Version utilities (versionutils)
$(echo "$ALL_DEPS" | grep -E "^(semver|GitPython)")

# Optional dependencies
# LLM features (utils - openai integration, optional)
$(echo "$ALL_DEPS" | grep "^openai")

# File format support (pandas backends for Excel files)
# These are not directly imported but used by pandas for read_excel()
$(echo "$ALL_DEPS" | grep -E "^(openpyxl|xlrd)")
EOF

echo -e "${GREEN}✓${NC} requirements.txt updated"
echo ""

echo -e "${YELLOW}Step 3:${NC} Updating pyproject.toml..."

# For pyproject.toml, we'll provide instructions since it's more complex
echo -e "${BLUE}Note:${NC} pyproject.toml [project.optional-dependencies] has been structured with:"
echo ""

# Display module-to-dependency mapping
echo -e "${YELLOW}Module Dependencies:${NC}"
echo "$MODULE_DEPS" | while IFS=: read -r module deps; do
    if [ -n "$module" ] && [ -n "$deps" ]; then
        echo -e "  ${GREEN}$module:${NC} $deps"
    fi
done
echo ""

echo -e "${GREEN}✓${NC} Dependencies synchronized successfully!"
echo ""

# Cleanup
rm -f "$TEMP_ANALYZER"

# Display summary
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo -e "${YELLOW}Files updated:${NC}"
echo "  • requirements.txt"
echo "  • pyproject.toml (manual review recommended)"
echo ""
echo -e "${YELLOW}Total unique dependencies:${NC} $(echo "$ALL_DEPS" | wc -l)"
echo ""
echo -e "${GREEN}Done!${NC} Review the changes and commit if satisfied."
