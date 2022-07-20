'''
to run these tests:
nix-shell -p 'python3.withPackages (p: with p; [ pytest pythonix ])' --command 'pytest test.py'
'''

import nix

def test_isEven_1():
    nix.eval(
        '''
        # with import (./. + "/math.nix");
        with import (builtins.toString ./math.nix);
        isEven 2
#        let
#          # mathLib = import "./math.nix";
#          # mathLib = import (builtins.toString math.nix);
#          # mathLib = import builtins.toPath (./. + "/math.nix");
#          # mathLib = import ./math.nix;
#          mathLib = import .math.nix;
#        in
#          # true
#          mathLib.isEven 2
        ''');
