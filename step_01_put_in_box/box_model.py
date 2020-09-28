from __future__ import absolute_import, division, print_function
from iotbx import pdb



pdb_inp = pdb.input(file_name="3nir.pdb")
ph = pdb_inp.construct_hierarchy()
ph.shift_to_origin(crystal_symmetry=pdb_inp.crystal_symmetry())
ph.write_pdb_file(file_name="3nir_box.pdb",crystal_symmetry=pdb_inp.crystal_symmetry())

