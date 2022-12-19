import xarray as xr
'''March 2022 -> model intercomparison project'''
def readDat(yr = 2015, forcing = None): 
  '''
  wrapper function to read the files from DATA/
  Forcing: either DFS (= 1) or CGRF (= 2)
  yr: year of interest. 
  Returns the dataset, output path 
  '''
  op = str()
  mid = str(yr) +'0101_'+str(yr)
  if forcing == 'DFS':
    op= 'OUT/DFS/'+str(yr)+'/NAA_DFS_'
    folder = 'DATA/G510_10_EXP00/'
    flag = 'past'
  elif forcing == 'CGRF': 
    op= 'OUT/CGRF/'+str(yr)+'/NAA_CGRF_' 
    folder = 'DATA/G510_10_EXP13/'
    flag = 'past'
    
  elif forcing == 'RCP85': 
    op= 'OUTPUT/RCP85/'+str(yr)+'/NAA_' 
    folder = 'DATA/85_canoe-dmsv5_15_EXP01/'
    flag = 'future'
  elif forcing == 'RCP45': 
    op= 'OUTPUT/RCP45/'+str(yr)+'/NAA_'
    folder = 'DATA/45_canoe-dmsv5_15b_EXP05/' 
    flag = 'future'
  elif forcing == 'RCP45f_co2': # wrong pCO2 forcing
    op= 'OUTPUT/RCP45f_co2/'+str(yr)+'/NAA_' 
    folder = 'DATA/45f_canoe-dmsv5_15b_EXP00/'
    flag = 'future'
  elif forcing == 'RCP45f_flow': # wrong northward flow 
    op= 'OUTPUT/RCP45f_flow/'+str(yr)+'/NAA_' 
    folder = 'DATA/45_canoe-dmsv5_15b_EXP02/' 
    flag = 'future'
    
  else: print('wrong input: ', forcing)
  if flag == 'past':
    ds = xr.open_mfdataset([folder+'/NAA_730h_'+mid+'1231_grid_T.nc',
                          folder+'/NAA_730h_'+mid+'1231_diad_T.nc',
                          folder+'/NAA_730h_'+mid+'1231_ptrc_T.nc'])#,
  else : # if flag == 'future'
    ds = xr.open_mfdataset([folder+ str(yr) +'_grid_T_reduced.nc',
                            folder+ str(yr) +'_diad_T_reduced.nc',
                            folder+ str(yr) +'_ptrc_T_reduced.nc',
                            ])
      
  return(op, ds)#,ds_ice)  


##############################################################################
def readDat_multiyear(yr = [], forcing = None, file_end = 'grid_T.nc'):
  '''read in a single filetype for all years given in yr'''
  op = str()
  fname1 = []
  if forcing == 'DFS':
    op= 'OUT/DFS/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_DFS_'
    folder = 'DATA/G510_10_EXP00/NAA_730h_'
    flag = 'past'
  elif forcing == 'CGRF': 
    op= 'OUT/CGRF/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_CGRF_' 
    folder = 'DATA/G510_10_EXP13/NAA_730h_'
    flag = 'past'
    
  elif forcing == 'RCP85': 
    op= 'OUTPUT/RCP85/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_' 
    folder = 'DATA/85_canoe-dmsv5_15_EXP01/'
    flag = 'future'
  elif forcing == 'RCP45': 
    op= 'OUTPUT/RCP45/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_'
    folder = 'DATA/45_canoe-dmsv5_15b_EXP05/' 
    flag = 'future'
  elif forcing == 'RCP45f_co2': # wrong pCO2 forcing
    op= 'OUTPUT/RCP45f_co2/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_' 
    folder = 'DATA/45f_canoe-dmsv5_15b_EXP00/'
    flag = 'future'
  elif forcing == 'RCP45f_flow': # wrong northward flow 
    op= 'OUTPUT/RCP45f_flow/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_' 
    folder = 'DATA/45_canoe-dmsv5_15b_EXP02/' 
    flag = 'future'
    
  else: print('wrong input: ', forcing)
  if flag == 'past':
    if file_end == None: 
      for l in yr: 
        m1 = folder+str(l) +'0101_'+str(l) + '1231_grid_T.nc'
        m2 = folder+str(l) +'0101_'+str(l) + '1231_diad_T.nc'
        m3 = folder+str(l) +'0101_'+str(l) + '1231_ptrc_T.nc'
        fname1.append(m1)
        fname1.append(m2)
        fname1.append(m3)

    else: 
      for l in yr: 
        m1 = folder+str(l) +'0101_'+str(l) + '1231_'+file_end
        fname1.append(m1)
  else : # if flag == 'future'
    for l in yr: 
      m1 = folder+str(l) +'_grid_T_reduced.nc'
      m2 = folder+str(l) +'_diad_T_reduced.nc'
      m3 = folder+str(l) +'_ptrc_T_reduced.nc'
      fname1.append(m1)
      fname1.append(m2)
      fname1.append(m3)
      
  ds1 = xr.open_mfdataset(fname1)
 
  return(op, ds1)#, ds2, ds3, ds4)  

def read_multi_pyco2sys(yr = [], forcing = None):
  '''read in a single filetype for all years given in yr'''
  op = str()
  fname1 = []
  if forcing == 'DFS':
    op= 'OUT/DFS/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_DFS_'
    folder = 'DATA/G510_10_EXP00/NAA_730h_'
    flag = 'past'
  elif forcing == 'CGRF': 
    op= 'OUT/CGRF/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_CGRF_' 
    folder = 'DATA/G510_10_EXP13/NAA_730h_'
    flag = 'past'
    
  elif forcing == 'RCP85': 
    op= 'OUTPUT/RCP85/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_' 
    folder = 'DATA/85_canoe-dmsv5_15_EXP01/NAA_730h_'
    flag = 'future'
  elif forcing == 'RCP45': 
    op= 'OUTPUT/RCP45/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_'
    folder = 'DATA/45_canoe-dmsv5_15b_EXP05/NAA_730h_' 
    flag = 'future'
  elif forcing == 'RCP45f_co2': # wrong pCO2 forcing
    op= 'OUTPUT/RCP45f_co2/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_' 
    folder = 'DATA/45f_canoe-dmsv5_15b_EXP00/NAA_730h_'
    flag = 'future'
  elif forcing == 'RCP45f_flow': # wrong northward flow 
    op= 'OUTPUT/RCP45f_flow/'+str(yr[0])+'-'+str(yr[-1])+'/NAA_' 
    folder = 'DATA/45_canoe-dmsv5_15b_EXP02/NAA_730h_' 
    flag = 'future'
    
  else: print('wrong input: ', forcing)
  if flag == 'past':
    print( 'not there yet')
  #  if file_end == None: 
  #    for l in yr: 
  #      m1 = folder+str(l) +'0101_'+str(l) + '1231_grid_T.nc'
  #3      m2 = folder+str(l) +'0101_'+str(l) + '1231_diad_T.nc'
  #      m3 = folder+str(l) +'0101_'+str(l) + '1231_ptrc_T.nc'
  #      fname1.append(m1)
  #      fname1.append(m2)
  #      fname1.append(m3)

  #  else: 
  #    for l in yr: 
  #      m1 = folder+str(l) +'0101_'+str(l) + '1231_'+file_end
  #      fname1.append(m1)
  else : # if flag == 'future'
    for l in yr: 
      m1 = folder+str(l) +'0101_'+str(l) + '1231_pyco2sys.nc'

      fname1.append(m1)
      
  ds1 = xr.open_mfdataset(fname1)
 
  return(op, ds1)#, ds2, ds3, ds4)  

def readDat_my_pyco2(yr = [], region = 'AG'):
  '''read in a single filetype for all years given in yr'''
  op= 'OUT/CGRF/multiyear/NAA_CGRF_'
  #out_pyco2sys_BS_500m2016
  fname_start = 'pyco2sys/out_pyco2sys_'+region+'_500m'
  fname1 = []
  for l in yr: 
    m1 = fname_start+str(l) +'.nc'
    fname1.append(m1)
    #fname4.append(m4)
   
  ds1 = xr.open_mfdataset(fname1)
 
  return(ds1)#

def readDat_my_organics(yr = []):
  '''read in a single filetype for all years given in yr'''

  fname_start = 'DATA/Organics/NAA_CGRF_sum_organics_'
  fname1 = []
  for l in yr: 
    m1 = fname_start+ str(l)+'.nc'
    fname1.append(m1)
    #fname4.append(m4)
  print(fname1) 
  ds1 = xr.open_mfdataset(fname1)
 
  return(ds1)#, ds2, ds3, ds4)  
