# hypothesis

The `math.nix` file defines the [factorial][factorial] function for non-negative integers. The `test_math.py` file defines two test: the first checks that non-negative inputs produce a positive output and the second checks that a negative input throws an error. To run these tests, run the command shown below.

[factorial]: https://en.wikipedia.org/wiki/Factorial

```shell
nix shell --impure --expr '(import <nixpkgs> {}).python3.withPackages (p: with p; [ hypothesis pytest pythonix ])' --command pytest test_math.py
```
