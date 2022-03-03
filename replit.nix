{ pkgs }: {
	deps = [
		pkgs.cargo
		pkgs.rustfmt
		pkgs.python311
        pkgs.rust-analyzer
	];
}