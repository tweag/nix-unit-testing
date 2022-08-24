import nix
from pathlib import Path

'''Note that the path to the file we want to test was declared in Python.
pythonix has some issues evaluating relative file paths.'''
test_file = Path(__file__).parent.resolve() / "math.nix"

def isEven_expr(file: Path, value: int) -> bool:
    '''Note that we could use f-strings here but we would have to escape all
    the curly braces which makes it more difficult to read.'''
    return '''
    (
      {pkgs ? import <nixpkgs> {}}: let
        inherit (pkgs) lib;
        math = import %s {inherit lib;};
      in
        math.isEven (%s)
    ) {}
    ''' % (file, str(value))

def test_isEven_1():
    expr = nix.eval(isEven_expr(file=test_file, value=2))
    assert expr == True

def test_isEven_2():
    expr = nix.eval(isEven_expr(file=test_file, value=-3))
    assert expr == False

