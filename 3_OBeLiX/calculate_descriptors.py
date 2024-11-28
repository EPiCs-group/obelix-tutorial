# -*- coding: utf-8 -*-
#                                                     #
#  __author__ = Adarsh Kalikadien                     #
#  __institution__ = TU Delft                         #
#  __contact__ = a.v.kalikadien@tudelft.nl            #

import os

import pandas as pd
from obelix.descriptor_calculator import Descriptors


# calculate descriptors from xyz file

descriptors = Descriptors(central_atom='Rh',
                          path_to_workflow=os.path.join(os.getcwd(), 'xyz_files'),
                          output_type='xyz')
descriptors.calculate_morfeus_descriptors(geom_type='BD',
                                          solvent=None,
                                          printout=False,
                                          metal_adduct='nbd',
                                          plot_steric_map=False)
descriptors.descriptor_df.to_csv('xyz_descriptors.csv', index=False)


# # calculate descriptors from CREST folder
#
# conformer_descriptors = Descriptors(central_atom='Rh',
#                                     path_to_workflow=os.path.join(os.getcwd()),
#                                     output_type='crest')
# conformer_descriptors.calculate_morfeus_descriptors(geom_type='BD',
#                                                     solvent=None,
#                                                     printout=False,
#                                                     metal_adduct='pristine')
# conformer_descriptors.descriptor_df.to_csv('conformer_descriptors.csv', index=False)


# # calculate descriptors from Gaussian log files
#
# path_to_dft_log_files = os.path.join(os.getcwd(), 'dft_log_files')
# dft_descriptors = Descriptors(central_atom='Rh',
#                               path_to_workflow=path_to_dft_log_files,
#                               output_type='gaussian')
# dft_descriptors.calculate_dft_descriptors_from_log(geom_type='BD',
#                                                    solvent=None,
#                                                    extract_xyz_from_log=True,
#                                                    printout=False,
#                                                    metal_adduct='nbd',
#                                                    plot_steric_map=True)
# dft_descriptors.descriptor_df.to_csv('DFT_descriptors.csv', index=False)

# extract free ligand from Gaussian log file
# iterate over log files and extract the free ligand as an xyz file

# from tqdm import tqdm
# from morfeus.io import read_cclib, write_xyz
# from obelix.molecular_graph import molecular_graph
# import glob
#
# path_to_dft_log_files = os.path.join(os.getcwd(), 'dft_log_files')
# complexes_to_calc_descriptors = glob.glob(os.path.join(path_to_dft_log_files, '*.log'))
# dictionary_for_properties = {}
#
# for metal_ligand_complex in tqdm(complexes_to_calc_descriptors):
#     elements, coordinates = read_cclib(metal_ligand_complex)
#     if not len(coordinates[-1]) == 3:  # if this is true, there is only 1 coordinates array
#         coordinates = coordinates[-1]
#     base_with_extension = os.path.basename(metal_ligand_complex)
#     split_base = os.path.splitext(base_with_extension)
#     filename = split_base[0]
#     molecular_graph(elements=elements, coordinates=coordinates, extract_ligand=True, path_to_workflow=path_to_dft_log_files, filename=filename)


# calculate free ligand descriptors

# from obelix.free_ligand import FreeLigand
# from obelix.tools.utilities import dataframe_from_dictionary
#
# ligand_number_list = ['L9', 'L10']
# dictionary_for_properties = {}
# complex_descriptors_df = pd.read_csv('DFT_descriptors.csv')
#
# for ligand_number in ligand_number_list:
#     path_to_free_ligand_files = os.path.join('free_ligand')
#     free_ligand = FreeLigand(path_to_workflow=path_to_free_ligand_files,
#                              xyz_filename=f'free_ligand_{ligand_number}.xyz',
#                              dft_log_file=f'free_ligand_{ligand_number}_SP.log')
#     # read the min/max donor indices from the excel file and match them with free_ligand.complex_xyz_bidentate_1_idx and free_ligand.complex_xyz_bidentate_2_idx
#     # if complex_xyz_bidentate_1 is min donor, then free_ligand_xyz_bidentate_1 is min donor for our free ligand class
#     # first check if index_donor_min from excel is equal to complex_xyz_bidentate_1_idx or complex_xyz_bidentate_2_idx
#     complex_bidentate_min_donor_idx = \
#         complex_descriptors_df.loc[complex_descriptors_df['Ligand#'] == ligand_number, 'index_donor_min'].values[0]
#     if complex_bidentate_min_donor_idx == free_ligand.complex_xyz_bidentate_1_idx:
#         # if this is true, then the free ligand bidentate 1 is the min donor
#         free_ligand.min_donor_idx = free_ligand.free_ligand_xyz_bidentate_1_idx
#         free_ligand.max_donor_idx = free_ligand.free_ligand_xyz_bidentate_2_idx
#     else:
#         # otherwise the free ligand bidentate 2 is the min donor
#         free_ligand.min_donor_idx = free_ligand.free_ligand_xyz_bidentate_2_idx
#         free_ligand.max_donor_idx = free_ligand.free_ligand_xyz_bidentate_1_idx
#
#     free_ligand.initialize_dft_extractor(free_ligand.dft_log_file, None, free_ligand.min_donor_idx,
#                                          free_ligand.max_donor_idx, metal_adduct='pristine')
#     # free_ligand.assign_min_max_donor_dft()
#     properties = free_ligand.calculate_dft_descriptors()
#     dictionary_for_properties[ligand_number] = properties
# new_descriptor_df = dataframe_from_dictionary(dictionary_for_properties)
# # reset the index and name that column to 'Ligand#' for consistency with the complex descriptor df
# new_descriptor_df = new_descriptor_df.reset_index().rename(columns={'index': 'Ligand#'})
# new_descriptor_df.to_csv('free_ligand_descriptors.csv', index=False)
