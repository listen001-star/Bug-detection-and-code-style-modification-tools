<<<<<<< HEAD
Software Engineering
# Pylint is a static code analyser for Python 2 or 3. The latest version supports Python 3.9.0 and above.

# Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.

# Pylint is not trusting your typing and is inferring the actual values of nodes (for a start because there was no typing when pylint started off) using its internal code representation (astroid). If your code is import logging as argparse, Pylint can check and know that argparse.error(...) is in fact a logging call and not an argparse call. This makes pylint slower, but it also lets pylint find more issues if your code is not fully typed.