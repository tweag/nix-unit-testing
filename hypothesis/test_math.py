'''
to run these tests:
nix-shell -p 'python3.withPackages (p: with p; [ hypothesis pytest pythonix ])' --command 'pytest test_math.py'
'''

import nix
from pathlib import Path
from hypothesis import given, strategies as st
import pytest

test_file = Path(__file__).parent.resolve() / "math.nix"

@given(st.integers(min_value=1, max_value=20))
def test_positive_integers(x):
    expr = nix.eval(
        f'''
        let
          math = import {test_file};
        in
          math.factorial {x}
        ''');
    assert expr > 0

@given(st.integers(max_value=0))
def test_negative_integers(x):
    with pytest.raises(nix.NixError):
        expr = nix.eval(
            f'''
            let
              math = import {test_file};
            in
              math.factorial {x}
            ''');

