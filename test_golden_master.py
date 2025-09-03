import json
import subprocess

import main


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


def load_golden_master():
    with open("golden_master.json") as f:
        return json.load(f)


# Fonction générique pour créer un test
def create_test_function(test_name, inputs, expected_output):
    def test_func():
        python_output = run_python(inputs)
        assert python_output.strip() == expected_output.strip(), f"Test {test_name} failed"
    return test_func


# Génération automatique des tests à partir du golden master
golden_master = load_golden_master()

# Création dynamique des tests pour chaque scénario
for test_name, data in golden_master.items():
    test_func = create_test_function(test_name, data["inputs"], data["output"])
    # Attribution du nom du test pour pytest
    test_func.__name__ = f"test_{test_name}"
    # Ajout du test au module global
    globals()[f"test_{test_name}"] = test_func