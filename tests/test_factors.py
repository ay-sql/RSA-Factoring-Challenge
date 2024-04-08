import subprocess
import os

def run_test(test_file, expected_output):
    """ Run the factors executable with the specified test file and compare the output to expected results. """
    # Build the command to run the factors script
    command = f"./factors {test_file}"
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
        'test00.txt': '4=2*2\n12=6*2\n34=17*2\n128=64*2\n1024=512*2',
        # Add more test cases as needed
    }

    # Run the tests
    for test_file, expected_output in tests.items():
        if not os.path.exists(test_file):
            print(f"Test file {test_file} does not exist.")
            continue
        run_test(test_file, expected_output)

if __name__ == "__main__":
    main()
