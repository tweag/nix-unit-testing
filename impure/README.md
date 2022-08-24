# impure

The `math.nix` file defines a function that checks if an integer is even. There are 3 test files that use different frameworks for testing: `test.nix` uses Nix, `test.nixt` uses [Nixt][nixt], and 'test_isEven.py' uses [Pythonix][pythonix]. To run these tests, run the commands in the relevant sections below.

[nixt]: https://github.com/nix-community/nixt
[pythonix]: https://github.com/Mic92/pythonix

### Nix
```shell
nix eval --impure --expr 'import ./test.nix {}'
```

### Nixt
```shell
nix run github:nix-community/nixt -- ./test.nixt
```

### Pythonix
```shell
nix shell --impure --expr '(import <nixpkgs> {}).python3.withPackages (p: with p; [ pytest pythonix ])' --command pytest test_isEven.py
```
