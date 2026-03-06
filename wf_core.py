import subprocess
import sys

def run_script(script_name):
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(f"Script failed: {script_name}")

def main():
    run_script("wf_dataprocessing.py")
    run_script("wf_visualization.py")
    print("[wf_core] Pipeline complete.")

if __name__ == "__main__":
    main()