"""
Compiler script to assemble all tests into all_tests.js
Supports any number of tests (Test 1, Test 2, Test 3, etc.)
"""
import glob
import json
import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def compile_tests():
    # Only match test1.json, test2.json, test3.json etc.
    all_files = glob.glob('test*.json')
    files = [f for f in all_files if re.match(r'^test\d+\.json$', os.path.basename(f))]
    files.sort(key=natural_sort_key)
    
    if not files:
        # Fallback to questions.json and test2_data.json
        if os.path.exists('questions.json'):
            files.append('questions.json')
        if os.path.exists('test2_data.json'):
            files.append('test2_data.json')

    tests = []
    print(f"Found {len(files)} test definition file(s):")
    for idx, f in enumerate(files, start=1):
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            # Ensure clean title
            if not data.get("test_title") or "Mock Test" not in data.get("test_title"):
                data["test_title"] = f"Infosys SE Mock Test {idx} — 2027 Batch Pattern"
            total_q = len(data.get("questions", []))
            print(f"  [{idx}] {f} -> '{data['test_title']}' ({total_q} questions)")
            tests.append(data)

    output = {
        "generated_at": "2026-10-02",
        "tests": tests
    }

    js_content = "window.ALL_TESTS = " + json.dumps(output, ensure_ascii=True, indent=2) + ";\nvar ALL_TESTS = window.ALL_TESTS;\n"

    with open('all_tests.js', 'w', encoding='utf-8') as fp:
        fp.write(js_content)

    print(f"\nSuccessfully compiled {len(tests)} test(s) into all_tests.js ({os.path.getsize('all_tests.js')} bytes)")

if __name__ == '__main__':
    compile_tests()
