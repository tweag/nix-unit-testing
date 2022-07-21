let
  lib = (import <nixpkgs> {}).lib;
in rec {
  # Returns the factorial of a postive integer.
  factorial = x:
    if (x < 1) || (builtins.typeOf x != "int")
    then throw "factorial only takes positive integers. got x = ${toString x}"
    else if x == 1
    then 1
    else x * factorial (x - 1);
}
