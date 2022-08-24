{
  description = "A flake demonstrating nix unit testing.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = {
    self,
    nixpkgs,
  }: {
    tests = let
      results = import ./test.nix {inherit nixpkgs;};
    in
      if results == []
      then "all tests passed"
      else throw (builtins.toJSON results);
  };
}
