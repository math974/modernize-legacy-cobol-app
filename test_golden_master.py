import subprocess
import json

def run_python(inputs):
    process = subprocess.Popen(
        ["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate("\n".join(inputs))
    return stdout

def test_against_golden_master():
    with open("golden_master.json") as f:
        golden_master = json.load(f)

    for name, data in golden_master.items():
        inputs = data["inputs"]
        expected_output = data["output"]

        python_output = run_python(inputs)

        # Here you can choose strict or tolerant comparison
        assert python_output.strip() == expected_output.strip(), f"Mismatch in {name}"
