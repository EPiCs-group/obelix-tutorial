# Tutorial of the Open Bidentate Ligand eXplorer (OBeLiX) workflow
The tutorial consists of 3 parts in which we will start with generating structures of homogeneous catalysts from scratch
and move towards the calculation of physical-chemical descriptors. Each folder contains a Jupyter notebook (and sometimes a
Python script for people that hate Jupyter notebooks) with explanations and example code. 

## Installation instructions
The OBeLiX code requires Anaconda/Miniconda and a Unix operating system due to a dependency on the xtb-python package. You can still run parts 
of this tutorial on a Windows system, but slight modifications are needed. I will mention this in the instructions below. 

The repository of [obelix](https://github.com/epics-group/obelix) is included in this tutorial as a submodule, meaning 
that is a Github repository within this Github repository. This makes it easier to install everything at once.

**Clone this repository and the code for all included submodules to your pc:**
```commandline
git clone https://github.com/EPiCs-group/obelix-tutorial --recurse-submodules
```

**Navigate to the newly created folder on your pc:**
```commandline
cd obelix-tutorial
```

**Create the conda environment with all dependencies for the OBeLiX code:**\
_Note for if you run this tutorial on a Windows system: before running the `conda env create` command you need to put a # before the line with - xtb-python in the environment.yml file such that it is ignored._
```commandline
cd obelix
conda env create -f environment.yml
```

This installs a conda environment named 'obelix', **which we have to activate:**
```commandline
conda activate obelix
```

**Since we want to run Jupyter notebooks, we have to install the notebook package in this environment:**
```commandline
pip install notebook
```

**And finally we install the code of OBeLiX as a package in this environment:**
```commandline
pip install -e .
```

**Now we can move one folder up towards the root folder of this repository (obelix-tutorial) and run Jupyter:**
```commandline
cd ..
jupyter notebook
```

Now you should be ready to go through the tutorial! Feel free to create issues in this repository if you have any questions/comments/improvements.

## Contents
* 1_MACE
  * Generate structures from the SMILES of metal and ligands (generate_structures.ipynb)
* 2_ChemSpaX
  * Replace dummy atoms on a chemical scaffold in 3D with a functional group (functionalize_skeleton.ipynb)
* 3_OBeLiX
  * Automate the usage of MACE and ChemSpaX for high-throughput generation of homogeneous catalysts with bidentate ligands (structure_generation/structure_generation_workflow.ipynb)
  * Automate the calculation of different types of descriptors for different filetypes, allowing to create a ML-ready representation of homogeneous catalysts with bidentate ligands (calculate_descriptors.ipynb)
    * _Note: DFT_descriptors.csv and xyz_descriptors.csv have been provided for people that are working on a Windows system and are thus unable to run the descriptor calculation on their system._
