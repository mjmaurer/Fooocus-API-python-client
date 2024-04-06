let
    pkgs = import <nixpkgs> { };
    lib = pkgs.lib;
    stdenv = pkgs.stdenv;
in pkgs.mkShell {
    buildInputs = with pkgs; [
        python311
        (poetry.override { python3 = python311; })
        openapi-generator-cli
    ];
    shellHook =
    ''
        export PYTHONPATH=$PYTHONPATH:$(pwd)
        # https://github.com/python-poetry/poetry/issues/1917
        export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring;
        alias init_gen="openapi-generator-cli generate --additional-properties=packageName=fooocusapi_client -g python -i https://raw.githubusercontent.com/mrhan1993/Fooocus-API/main/docs/openapi.json"
        alias build="poetry run python -m build"
        alias publish="twine upload dist/*"
    '';

}