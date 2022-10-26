# for every row in dataframe, find the griddcell index in the dataset
import numpy as np

def gridcellfinder(df, xrds, i, ): 
  '''returns all the gridcell indices for row i as single number
  example: df = obs_dataframe, xrds = nemo_mask, i = 0
  '''
  if type(df) == dict: # if the input is a dictionary (ex: AMS-data)
    mask = xrds['nav_lon'].where((xrds['nav_lat'] > df['latmin']) & (xrds['nav_lat'] < df['latmax']) &
                           (xrds['nav_lon'] > df['lonmin']) & (xrds['nav_lon'] < df['lonmax']),0)
  else: # if the input is a dataframe (ex: Christine Michel)
    mask = xrds['nav_lon'].where((xrds['nav_lat'] > df['latmin'][i]) & (xrds['nav_lat'] < df['latmax'][i]) &
                           (xrds['nav_lon'] > df['lonmin'][i]) & (xrds['nav_lon'] < df['lonmax'][i]),0)
  fu = np.array(mask)
  fu2 = np.where(fu != 0)
  Y = fu2[0][:] # Updated, becasue the NAA xarray is T,Z,Y,X somehow.
  X = fu2[1][:]
  
  return X, Y

'''
def gridcellfinder(df, xrds, i): 
  """returns all the gridcell indices for row i as single number"""
  mask = xrds['nav_lon'].where((xrds['nav_lat'] > df['latmin'][i]) & (xrds['nav_lat'] < df['latmax'][i]) &
                           (xrds['nav_lon'] > df['lonmin'][i]) & (xrds['nav_lon'] < df['lonmax'][i]),0)
  fu = np.array(mask)
  fu2 = np.where(fu != 0)
  X = fu2[0][:]
  Y = fu2[1][:]
  
  return X, Y

  
  
  
   '''