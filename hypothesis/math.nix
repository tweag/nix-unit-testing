{ pkgs ? import <nixpkgs> {} }:
let
  inherit (pkgs) lib;
in rec {
  # Returns the factorial of a non-negative integer.
  factorial = x:
    if (x < 0) || !(builtins.isInt x)
    then throw "factorial only takes positive integers, got x = ${toString x}"
    else if x == 0
    then 1
    else x * factorial (x - 1);
}
