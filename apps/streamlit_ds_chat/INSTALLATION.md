# Setting up a local development environment

Before we can actually start building Streamlit apps, we will first have to set up a development environment.

Let's start by installing and setting up a conda environment.

## **Install conda**
- Install `conda`:
  - visit https://docs.conda.io/en/latest/miniconda.html
  - choose your operating system (Windows, Mac or Linux) 
  - download and run the installer to install `conda`.

## **Create a new conda environment**
Now that you have conda installed, let's create a conda environment for managing all the Python library dependencies.

To create a new environment with Python 3.9, enter the following:
```bash
conda create -n stenv python=3.9
```
where `create -n stenv` will create a conda environment named `stenv` and `python=3.9` will setup the conda environment with Python version 3.9.

or

```bash
conda create -p ./env python=3.9
```
for local environment at `./env`


## **Activate the conda environment**

To use a conda environment that we had just created that is named `stenv`, enter the following into the command line:

```bash
conda activate stenv
```

## **Install the Streamlit library**

It's now time to install the `streamlit` library:

```bash
conda install streamlit
// or
pip install streamlit
```


## Other dependencies

### For HuggingFace transformers

```bash
pip install transformers
conda install pytorch
```

### For Google vertex AI

```bash
pip install google-cloud-aiplatform   // --upgrade ?
sudo snap install google-cloud-cli --classic
//pip3 install black
//conda install numpy"<2.0"
```

### Installing Ruff
Ruff is available as ruff on PyPI:

```bash
pip install ruff
```

Once installed, you can run Ruff from the command line:

```bash
ruff check   # Lint all files in the current directory.
ruff format  # Format all files in the current directory.
```

### Bokeh visualization

```bash
pip install bokeh -- already installed?
```

## Dask and Coiled installation

See https://github.com/Sklavit/pet_project/blob/c6278b67484558985faa9bd3a9a58e34e765cf6d/apps/streamlit_ds_chat/cloud_coiled_io/README.md

```bash
pip3 install coiled "dask[complete]"
coiled login
```

Expected result:

> Authentication successful 🎉
> Credentials have been saved at /home/< USERNAME >/.config/dask/coiled.yaml

