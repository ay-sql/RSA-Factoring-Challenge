import subprocess
import os

def run_test(test_file, expected_output):
    """Run the rsa executable with the specified test file and compare the output to expected results."""
    # Build the command to run the rsa script
    command = f"./rsa {test_file}"
    # Execute the command
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        output = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running test {test_file}: {e}")
        return False
    
    # Compare the output with the expected results
    if output == expected_output.strip():
        print(f"Test {test_file} passed.")
        return True
    else:
        print(f"Test {test_file} failed.\nExpected:\n{expected_output}\nGot:\n{output}")
        return False

def main():
    # Define test cases, pairing filenames with their expected outputs
    tests = {
        'rsa-1.txt': '6=3*2',
        'rsa-2.txt': '77=11*7',
        'rsa-3.txt': '143=13*11',
        # Additional cases can be added here
    }

    # Run the tests
    for test_file, expected_output in tests.items():
        if not os.path.exists(test_file):
            print(f"Test file {test_file} does not exist.")
            continue
        run_test(test_file, expected_output)

if __name__ == "__main__":
    main()
