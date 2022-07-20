{
  description = "A flake demonstrating nix unit testing.";

  outputs = { self, nixpkgs }: {

    nix-lib-test = import ./test.nix;

  };
}
