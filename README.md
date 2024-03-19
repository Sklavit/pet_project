# pet_project
Pet python project to experiment and show

# Environment

This project is conda based.

If you don't have conda installed, instal miniconda:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```

To install Conda shell use: `conda init`.
For better use:
`export PATH="~/miniconda3/bin:$PATH"`
and `source ~/.bashrc`

You can check that conda is really installed by `conda --version` command.

To create environment run
`conda create -n pet_project python=3.10 -p .`  --file=xxx --solver libmamba
or

```bash
conda create -p ./.env python=3.10
```

To activate this environment, use    
```bash
conda activate ./.env                                                                                                                                                      
```

To deactivate an active environment, use
```bash
conda deactivate
```

# How to update environment

```bash
conda env update -n env-name --file environment.yml
```
or
```bash
conda env update -p ./.env --file environment.yml
```

# How to contribute

## If you want to install extra dependency

1. Do it like:

```bash
conda install mamba -c conda-forge
```

2. Update `environment.yaml` file

```bash
conda env export > environment.yml
``` 

