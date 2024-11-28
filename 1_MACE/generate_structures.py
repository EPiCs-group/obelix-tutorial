# -*- coding: utf-8 -*-
#                                                     #
#  __author__ = Adarsh Kalikadien                     #
#  __institution__ = TU Delft                         #
#  __contact__ = a.v.kalikadien@tudelft.nl            #

import mace
import os

# example of SP structure generation
list_of_ligands = ['CCCCOC(=O)N1CC(CC1C[P:1](C2=CC=CC=C2)C3=CC=CC=C3)[P:1](C4=CC=CC=C4)C5=CC=CC=C5']
list_of_cas = ['BPPM']

# this is a loop for SP structures
for index, ligand in enumerate(list_of_ligands):
    ligands = [ligand, 'CC#[N:1]', 'CC#[N:1]']
    CA = '[Rh+]'  # SMILES of central atom
    geom = 'SP'

    X = mace.ComplexFromLigands(ligands, CA, geom)
    Xs = X.GetStereomers(regime='all', dropEnantiomers=True)
    print(f'{geom} Stereomers for ligand {list_of_cas[index]}:', len(Xs))

    for i, X in enumerate(Xs):
        X.AddConformers(numConfs=10)
        X.ToXYZ(f'{list_of_cas[index]}_{i}.xyz', confId='min')


# example of OH structure generation
list_of_ligands = ["C[N:1](CC[N+]1=[C-:1]N(C=C1)C1=C(C)C=C(C)C=C1C)CC1=CC=CC=C1[P:1](C1=CC=CC=C1)C1=CC=CC=C1"]
list_of_cas = ['MnCNP_CNP']

# this is a loop for OH structures
for index, ligand in enumerate(list_of_ligands):
    ligands = [ligand, "[C-:1]#[O+]", "[C-:1]#[O+]", "[C-:1]#[O+]"]
    CA = '[Mn+]'  # SMILES of central atom
    geom = 'OH'

    X = mace.ComplexFromLigands(ligands, CA, geom)
    Xs = X.GetStereomers(regime='all', dropEnantiomers=True)
    print(f'{geom} Stereomers for ligand {list_of_cas[index]}:', len(Xs))

    for i, X in enumerate(Xs):
        X.AddConformers(numConfs=50)
        X.ToXYZ(f'{list_of_cas[index]}_{i}.xyz', confId='min')