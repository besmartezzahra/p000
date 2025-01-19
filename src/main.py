import subprocess

def run_javascript_file(file_path):
    try:
        result = subprocess.run(['node', file_path], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_javascript_file('src/script.js')
