{
  description = "A flake demonstrating nix unit testing.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = {
    self,
    nixpkgs,
  }: {
    tests = import ./test.nix {inherit nixpkgs;};
  };
}
