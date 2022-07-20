{
  description = "A flake demonstrating nix unit testing.";

  inputs = {
    nixt.url = "github:nix-community/nixt";
    nixt.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, nixt }: {
    nix-lib-test = import ./myLib/test.nix {inherit nixpkgs;};
    # nixt-test = import ./myLib/test.nixt {inherit nixpkgs nixt;};
  };
}
