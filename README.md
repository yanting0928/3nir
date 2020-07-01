# 3nir

1.	Box the model 

Script: box_model.py 

OUTPUT: 3nir_box.pdb

2.	Re-build H

COMMAND: phenix.pdbtools remove="element H " 3nir_box.pdb

phenix.reduce  3nir_box.pdb

OUTPUT:  3nir_update.pdb

3.	Run phenix.refine

COMMAND: phenix.refine ../3nir_update.pdb  ../3nir.mtz  main.ordered_solvent=true wc=0.05 wu=0.1 main.max_number_of_iterations=50 main.number_of_macro_cycles=5 refinement.input.xray_data.r_free_flags.generate=True

OUTPUT:  Fold prefine_00/    

3nir_update_refine_data.mtz is data file after r free flags generate

4.	Get map

COMMAND: phenix.maps skip_twin_detection=True 3nir_update_refine_001.pdb 3nir_update_refine_data.mtz

OUTPUT: prefine_00/3nir_update_refine_001_map_coeffs.mtz


## CHANGES
### Coot_01
Map fit ligand 2001

Remove ligand 2002 A,B

Add water chain s 81 water

### Coot_02
Remove ligand 2004

Remove water71

Remove ligand 2001,2003

### Coot_03

Resseq 2B map fit

S 53 water map fit

Remove water 66

Chain a res 10 ARG  add a conformer   
