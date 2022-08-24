# flake

This example has a `math.nix` and `test.nix` file similar to what is in the `impure` example. Rather than performaing an impure evaluation, we can use flakes to purely evaluate the tests. In the `flake.nix` file, we import the test and check its output. If the output is empty, we return a string, "all tests passed", and otherwise we return the output of the test. You can evaluate the tests by running the command below.

```shell
nix eval .#tests
```
