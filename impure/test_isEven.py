'''
to run these tests:
nix-shell -p 'python3.withPackages (p: with p; [ pytest pythonix ])' --command 'pytest test.py'
'''

import nix
from pathlib import Path

test_file = Path(__file__).parent.resolve() / "math.nix"

def isEven_expr(file: Path, value: int) -> bool:
    return '''
    (
      {pkgs ? import <nixpkgs> {}}: let
        inherit (pkgs) lib;
        math = import %s {inherit lib;};
      in
        math.isEven %s
    ) {}
    ''' % (file, str(int))

def test_isEven_1():
    expr = '''
        (
          {pkgs ? import <nixpkgs> {}}: let
            inherit (pkgs) lib;
            math = import %s {inherit lib;};
          in
            math.isEven 2
        ) {}
    ''' % test_file
    assert nix.eval(expr) == True

def test_isEven_2():
    expr = '''
        (
          {pkgs ? import <nixpkgs> {}}: let
            inherit (pkgs) lib;
            math = import %s {inherit lib;};
          in
            math.isEven (-3)
        ) {}
    ''' % test_file
    assert nix.eval(expr) == False

