# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [ pkgs.python3 pkgs.postgresql pkgs.stdenv.cc.cc.lib pkgs.gcc ];
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [ "ms-python.python" ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      };
      onStart = {
        # The following command will start a PostgreSQL database server
        postgres = '''
          mkdir -p ~/.postgres/run
          pg_ctl -D postgresql-data -l logfile -o "-h 127.0.0.1 -p 5432 -k ~/.postgres/run" start
        ''';
      };
    };
    # Enable previews and customize configuration
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "./devserver.sh" ];
          env = { PORT = "$PORT"; };
          manager = "web";
        };
      };
    };
  };
}
