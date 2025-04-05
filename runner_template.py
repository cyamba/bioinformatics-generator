# runner_template.py

def get_runner_code(project_name, subpackage="modules"):
    return f"""#!/usr/bin/env python3

from importlib import import_module

def run_problem(problem_id):
    module_name = f'{{problem_id}}'
    try:
        mod = import_module(f'{project_name}.{subpackage}.' + module_name)
        if hasattr(mod, 'solve'):
            result = mod.solve()
            print(f'Result for {{problem_id}}:', result)
        else:
            print(f'Module {{module_name}} does not have a solve() function.')
    except ModuleNotFoundError:
        print(f'Problem module {{module_name}} not found in {subpackage}.')

if __name__ == '__main__':
    problem = input('Enter module name (e.g. problem_001_dna): ')
    run_problem(problem)
"""
