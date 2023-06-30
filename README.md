# ICPC-like competition template

This is a template for myself, and is only usable on Windows systems. (This is because, `subprocess.popen` without `shell=True` will not seperate arguments automatically)

Compile (and run) the file using `run.py`, you will get the following feature on your local machine, but your submitted program will remain clean.

- `debugp()` will print information to `stderr`.
- `debuge()` will execute function passed to it.
- program reads input from `in.txt`.

Supported argument:

- Mode switching. Switching mode will make all regular parameters invalid.
  - `--pyrun-hack`: Switch to hack mode. Input and output will be redirected. Execution time will be shown. `debugp()` and `debuge()` won't work. 
  - `--pyrun-hackgen`: Switch to hackgen mode. Output will be redirected to `in.txt`.

- `--pyrun-random`: (Not recommended) Run `utils/randgen.exe` first. You could compile it from `randgen.cpp`.

- `--pyrun-interactive`: Input will not be redirected.

- `--pyrun-nodebug`: `debugp()` and `debuge()` won't work. 

- `--pyrun-longcheck`: Output will be redirected to `out.txt`.

- All other arguments will be passed to compiler.