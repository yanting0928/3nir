from __future__ import absolute_import, division, print_function 
import mmtbx 
import iotbx 
from mmtbx import model 
from libtbx.utils import null_out 
from scitbx.array_family import flex 
from scitbx.matrix import rotate_point_around_axis

def run(pdb_file_name):
  pdb_inp = iotbx.pdb.input(file_name=pdb_file_name)
  params =  mmtbx.model.manager.get_default_pdb_interpretation_params()
  model = mmtbx.model.manager(
    model_input       = pdb_inp,
    pdb_interpretation_params = params,
    build_grm         = True,
    stop_for_unknowns = False,
    log               = null_out())
  pdb_hierarchy = model.get_hierarchy()
  sites_cart_dc = model.get_sites_cart().deep_copy()
  angle = 0.
#  points_i_seqs = [483]
#  axis = [479,482]
  points_i_seqs = [559]
  axis = [556,557]
  while angle <= 360:  
    atoms_xyz_tmp  = flex.vec3_double(len(points_i_seqs))
    atom_xyz_new = rotate_point_around_axis(
        axis_point_1 = sites_cart_dc[axis[0]],
        axis_point_2 = sites_cart_dc[axis[1]],
        point        = sites_cart_dc[points_i_seqs[0]],
        angle        = angle,
        deg          = True)
    print (atom_xyz_new)
    atoms_xyz_tmp[0] = atom_xyz_new
    sites_cart_dc[points_i_seqs] = atoms_xyz_tmp[0]
    model.set_sites_cart(sites_cart = sites_cart_dc)      

    with open(str(angle)+".pdb", "w") as of:
      print (model.model_as_pdb(),file=of)
    angle += 30.


if __name__ == '__main__':
  run(pdb_file_name="test.pdb")

