# 3nir

### reflection.mtz

The orifinal R-free flags are unrecoverable, enable option: input.xray_data.r_free_flags.generate in Phenix GUI Comprehensive validation, refletion.mtz is the output.

Input: step_01_put_in_box/3nir_box.pdb step_00_get_files/3nir.mtz

## Problem detect:
res 1 BTHR CA-C-O angle 109, three hydrogen connect to N floating  
res 2 BTHR O-C-N angle 131, CA-HA  
res 7 BILE CA-HA,  CB-HB     
res 2002 EOH  no map fit, also clash with res 8 and 11  
res 8 
  * BVAL O-C-N angle 112,  CB-HB,  CG1,CG2 not fit map well (add a conformer?)   
  * AVAL O-C-N angle 130   

res 10 ARG side chain can add a conformer  

res 13   
  * BPHE O-C-N angle 111.6, CA-HA, hydrogen connect to ring floating  
  * APHE O-C-N angle 129 CA-HA  
       
res 18 HB2 clash with res 19 BPRO HD3  
res 19 CA-HA  
res 22 BSER C-N distance 1.24,N-CA-CB 103  
res 25 BILE peptide plane  
res 29 
  * TYR can add  a conformer
  * ATYR CA-HA, N-CA-CB 103 (110)
  * BTYR C-CA-CB 119 (110)
  * CTYR CB-CG-CD2 113 (120)
  * Hydrogen mess
       
res 34 
  * BILE C-CA-CB angle 122 (111),  CB-CG1-CD1 124 (113), O-C-N 131, CA-HA, CB-HB
  * AILE C-CA-CB 103
  
res 37 BGLY N-H  
res 38 AALA CA-HA  
res 39 
  * ATHR CA-HA
  * BTHR N-H, CA-HA, O-C-N 115
       
res 42 O-C-N(BASP) 132  
res 43 
  * BASP CA-CB-CG-OD1 168 (0), H point, CA-HA, OD2-HD2
  * AASP CA-CB-CG-OD1 162, OD2-HD2
       
res 2001 EOH  no map fit, also clash with res 46  
res 2003 EOH improved  
res 2004 EOH no map fit  

### Questionable waters
3112 clash with res 25 BLEU HD12
3006 3016 3017B 3021 3028 3033B 3035 3047 3051 3052B 3054 3071 3072 3083 3085
3088 3092 3093 3095 3096 3098 3101 3109 3110 3111 3112 3113 3114 3115 3116 3117
3118 3119 3120 3121 3123 

### Water can be improved:
3023 3025 3027 3031 3066B 3076 3081 3082B 3084 3099 

