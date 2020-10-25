### do phenix.refine

COMMAND: phenix.refine ../step_03_readd_H/3nir_H.pdb ../reflections.mtz wc=0.1 wu=0.1 ordered_solvent=true ordered_solvent.new_solvent=anisotropic main.number_of_macro_cycles=10 refine.occupancies.individual=water refinement.main.max_number_of_iterations=50


### List of problems or place can be improved

res 8 altB CG1 point to negative density, positive density around alt A CG1 and CG2, cosider another conformer.   
res 10 non-spherical density along arginine side chain, can add a conformen   
res 11 HG point to negative density   
res 13 positive and negative on opposite sides of O   
res 18 HB2 clash with res BPRO HD3   
res 21 HG1 can be rotate to positive density    
res 22 there are a green blob around HB2 altB, consider a conformer for altA?   
res 23 can be another conformer to fit green density, also non-spherical density    
res 25 negative density around CD1, positive density around altA CD2, should be refit, can put altB CD1 in same blob with altA CD2   
res 29 conformer A not fit the map well, can be refit to the positive density or add the fourth conformer    
res 34 altB CD1 in negative density, can be refit to the positive density   
res 36 positive and negative on opposite sides of CB, can be refit    
res 39 positive density around OG1 for both conformers    
res 46 OD1 clash with 2001 EOH H12     
res 2001 C2 in negative density   
res 2003 altB C2 in negative density   

###Questionable waters
69 70 71 77 78 79 81
