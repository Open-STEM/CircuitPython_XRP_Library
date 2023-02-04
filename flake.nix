{
  description = "XRP Dependency for NIX";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release-22.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
      in {
        # Nix flakes really wants packages
        packages.hello = pkgs.hello;

        # We only care about the shell
        devShell = pkgs.mkShell {
          inputsFrom = builtins.attrValues self.packages.${system};
          buildInputs = [
            pkgs.poetry
            pkgs.sphinx
            (pkgs.python310.withPackages (pyPkgs: with pyPkgs; [
              sphinx-rtd-theme
            ]))
          ];
        };
      });
}
