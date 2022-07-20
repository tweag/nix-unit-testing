let
  lib = (import <nixpkgs> {}).lib;
in {
  # Returns true if integer is even.
  isEven = x: (lib.mod x 2) == 0;
}
