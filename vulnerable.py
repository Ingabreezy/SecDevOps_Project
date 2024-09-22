import os
import subprocess

# Vulnerable to hardcoded secrets
API_KEY = "12345-ABCDE-FGHIJ-67890"

# Vulnerable to command injection
def list_files(directory):
    # Unsafe command execution
    command = "ls -l " + directory
    return subprocess.check_output(command, shell=True)

# Vulnerable to arbitrary code execution
def eval_expression(expr):
    # Insecure use of eval
    return eval(expr)

if __name__ == "__main__":
    # Example usage that exposes vulnerabilities
    directory_input = input("Enter a directory to list: ")
    print("Listing files in directory:")
    print(list_files(directory_input))

    expr_input = input("Enter an expression to evaluate: ")
    print("Result of evaluation:")
    print(eval_expression(expr_input))
