# nix-unit-testing

A showcase of different unit testing frameworks for testing Nix code.

## impure

The `impure` directory contains minimal examples showing how to test a Nix function with impure methods. In the directory, is a `math.nix` file containing a simple math function. The other files are used to unit test the math function. Each test file has comments, at the top of the file, with instructions on how to run the tests.

## hypothesis

The `hypothesis` directory is similar to the `impure` directory. It has a `math.nix` file with a simple containing a math function. However, it only has a single test file that demonstrates how to perform property-based testing with [Hypothesis](https://hypothesis.readthedocs.io/en/latest/). As before, the test file has embedded instructions on how to run the tests.
