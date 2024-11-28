# -*- coding: utf-8 -*-
#                                                     #
#  __author__ = Adarsh Kalikadien                     #
#  __institution__ = TU Delft                         #
#  __contact__ = a.v.kalikadien@tudelft.nl            #

import os
import glob

import chemspax
from chemspax.main import main

current_directory = os.getcwd()
path_to_substituents = os.path.join(os.path.dirname(chemspax.__file__), 'substituents_xyz', 'manually_generated')
# # uncomment these 3 lines if you want to see the available substituents
# print("Available substituents: ")
# for file in glob.glob(os.path.join(path_to_substituents, "*.xyz")):
#     print(os.path.basename(file)[:-4])
path_to_database = os.path.join(path_to_substituents, "central_atom_centroid_database.csv")

substituent_list = ["CH3", "CH3", "CH3", "CH3"]
skeleton_list = glob.glob(os.path.join(current_directory, "skeletons", "*.xyz"))
path_to_skeletons = os.path.join(current_directory, "skeletons")
working_directory = current_directory
path_to_output = os.path.join(current_directory, "functionalized_skeletons")
main(skeleton_list, substituent_list, path_to_database, path_to_substituents, path_to_skeletons, working_directory, path_to_output)

# clean up, comment this part if you want to see the intermediately generated structures
# remove all xyz files in functionalized_skeletons
for file in glob.glob(os.path.join(path_to_output, "*.xyz")):
    os.remove(file)
# keep only the .mol file of the final structure
for file in glob.glob(os.path.join(path_to_output, "*.mol")):
    if not f"_func_{len(substituent_list)}" in file:
        os.remove(file)
