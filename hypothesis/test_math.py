import nix
from pathlib import Path
from hypothesis import given, strategies as st
import pytest

test_file = Path(__file__).parent.resolve() / "math.nix"

def expression(file: Path, value: int) -> int:
  return '''
  ( {pkgs ? import <nixpkgs> {}}: let
      math = import %s {inherit pkgs;};
    in
      math.factorial (%s)
  ) {}
  ''' % (file, str(value))

# max value limited to 20 because larger values go beyond 64-bit precision
@given(st.integers(min_value=0, max_value=20))
def test_positive_integers(x):
    expr = nix.eval(expression(file=test_file, value=x))
    assert expr > 0

@given(st.integers(max_value=-1))
def test_negative_integers(x):
    with pytest.raises(nix.NixError):
        expr = nix.eval(expression(file=test_file, value=x))

