# metagenomics_pooling_notebook

A Jupyter notebook to assist wet lab shotgun pipeline.

## Installation

To install this notebook, first clone the repository from GitHub:

```bash
git clone https://github.com/biocore/metagenomics_pooling_notebook.git
```

Create a Python3 Conda environment in which to run the notebook:

```bash
conda create -n metapool 'python=3.9' scikit-learn pandas numpy scipy nose pep8 flake8 matplotlib jupyter 'seaborn>=0.7.1' pip openpyxl

```

Activate the Conda environment:

```bash
source activate metapool
```

Change directory to the downloaded repository folder and install:

```bash
cd metagenomics_pooling_notebook
pip install -e '.[all]'
```

For users of notebook version 7.0.0 or higher, table of contents is already
installed and can be activated from the pull-down menus. Notebook 6.5.5 users
or lower will need to perform the following two additional steps to install
and activate table of contents:

First, install the nbextension plugin:
```bash
jupyter contrib nbextension install --sys-prefix --skip-running-check
```

Second, install the table of contents (TOC) extension
```bash
jupyter nbextension enable toc2/main
```


## Use

The notebook itself contains detailed usage instructions. 

Ideally, you will copy this original notebook and use it for each plate you
create with the shotgun pipeline.

Just make sure to activate the right Conda environment before starting the
notebook.

Here's a quick example:

```bash
cp metagenomics_pooling.ipynb ~/New_project/new_project_pooling.ipynb
cd ~/New_project
source activate metapool
jupyter notebook
```
