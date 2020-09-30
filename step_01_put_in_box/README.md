### make a box 

Script: box_model.py 

OUTPUT: 3nir_box.pdb

## generate map for ori pdb

phenix.maps 3nir.pdb ../3nir_update_refine_data.mtz  skip_twin_detection=True

Output: 3nir_box_map_coeffs.mtz, 3nir_box_2mFo-DFc_map.ccp4


