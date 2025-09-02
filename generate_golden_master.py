import subprocess
import json

SCENARIOS = {
    "view_balance": ["1", "4"],
    "credit_100": ["2", "100", "1", "4"],
    "debit_50": ["3", "50", "1", "4"],
    "debit_too_much": ["3", "2000", "1", "4"],
    "exit": ["4"]
}

def run_cobol(inputs):
    process = subprocess.Popen(
        ["./accountsystem"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate("\n".join(inputs))
    return stdout

def main():
    golden_master = {}
    for name, inputs in SCENARIOS.items():
        output = run_cobol(inputs)
        golden_master[name] = {
            "inputs": inputs,
            "output": output
        }
    with open("golden_master.json", "w") as f:
        json.dump(golden_master, f, indent=2)

if __name__ == "__main__":
    main()
