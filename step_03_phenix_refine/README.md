### running with phenix.refine

COMMAND: phenix.refine 3nir_update.pdb 3nir.mtz main.ordered_solvent=true wc=0.05 wu=0.1 main.max_number_of_iterations=50 main.number_of_macro_cycles=5 refinement.input.xray_data.r_free_flags.generate=True

3nir_update_refine_data.mtz is data file after r free flags generate

#### Get map:

phenix.maps skip_twin_detection=True 3nir_update_refine_001.pdb 3nir_update_refine_data.mtz

OUTPUT: 3nir_update_refine_001_map_coeffs.mtz
