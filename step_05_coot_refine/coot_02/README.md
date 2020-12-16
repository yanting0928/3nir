## Coot 02

res 22 add a conformer for altB SER (coot will add as resname PRO)   	
res 23 add a conformer to fit green blob, ini occpancy 0.5  
res 34 alt B refit to green density  
res 39 refit for both two conformers  
output file: 3nir_coot_02.pdb  

res 22 re-set occpancy for all conformers 0.33   
res 29 re-set occpancy 0.25   
output file: 3nir_coot_02_update.pdb   

rotate res22 conformer c to fit the green density   
rotate res25 conformer b CD1     
output file: 3nir_coot_02_final.pdb  
