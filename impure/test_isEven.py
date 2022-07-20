'''
to run these tests:
nix-shell -p 'python3.withPackages (p: with p; [ pytest pythonix ])' --command 'pytest test.py'
'''

import nix
from pathlib import Path

test_file = Path(__file__).parent.resolve() / "math.nix"

def testIsEven_1():
    expr = nix.eval(
        f'''
        let
          math = import {test_file};
        in
          math.isEven 2
        ''');
    assert expr == True

def testIsEven_2():
    expr = nix.eval(
        f'''
        let
          math = import {test_file};
        in
          math.isEven (-3)
        ''');
    assert expr == False

