# nix-unit-testing

A showcase of different unit testing frameworks for testing Nix code. Read the related [blog post][blog-post] that explains some of the examples here.

[blog-post]: https://www.tweag.io/blog/2022-09-01-unit-test-your-nix-code/

## impure

The `impure` directory contains minimal examples showing how to test a Nix function with impure methods.

## hypothesis

The `hypothesis` directory is similar to the `impure` directory. However, it only has a single test file that demonstrates how to perform property-based testing with [Hypothesis](https://hypothesis.readthedocs.io/en/latest/).

## flake

The `flake` directory demonstrates how to test a Nix function with pure methods using flakes.
