
# !!! it is not working for unknown reason.

Also install
```bash
conda install -c conda-forge conda-lock
```

Create the lock file from the environment.yml file
```bash
conda lock
```

A “lock file” contains a concrete list of package versions (with checksums) to be installed. Unlike
e.g. `conda env create`, the resulting environment will not change as new package versions become
available, unless you explicitly update the lock file.
Install this environment as "YOURENV" with:
```bash
conda-lock install -n YOURENV --file conda-lock.yml
```

To update a single package to the latest version compatible with the version constraints in the source:
```bash
conda-lock lock --lockfile conda-lock.yml --update PACKAGE
```
To re-solve the entire environment, e.g. after changing a version constraint in the source file:
```bash
conda-lock -f environment.yml -f C:\MyComputer\01Algorithms\Hydrology\Hapi\environment.yml -f C:\gdrive\01Algorithms\Hydrology\Hapi\environment.yml --lockfile conda-lock.yml
```
