let
  lib = (import <nixpkgs> {}).lib;
  inherit (lib) runTests;
  math = import ./math.nix;
in
  runTests {
    testIsEven_1 = {
      expr = math.isEven 2;
      expected = true;
    };

    testIsEven_2 = {
      expr = math.isEven (-3);
      expected = false;
    };
  }

