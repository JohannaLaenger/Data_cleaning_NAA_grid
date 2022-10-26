

def LonLat_cleaner(df, HS = 'W'):
  '''
  Takes the Longitude/Latitude from the analogoue format 70˚19.12	126˚25.07 to the digital format.
  HS = Hemisphere, if the data is in the western Hemisphere, but the coordinate is positive, it gets 
  multiplied by -1. 
  '''
  list_of_lons = []   
  list_of_lats = []
  # I need to include a switch for nan's
  # I need to include a switch for east/west
  lonsplit = df.Longitude.str.split('°', expand=True)
  latsplit = df.Latitude.str.split('°', expand=True)
  for x in [*range(0,len(latsplit),1)]:
      la = latsplit[1][x]
      lo = lonsplit[1][x]
      if "'" not in la: #70˚19.12	126˚25.07	
        y = float(latsplit[0][x])+float(la)/60
      else: #70˚19.12'	126˚25.07'	
        y = float(latsplit[0][x])+float(la[:-1])/60
      list_of_lats.append(y)

      if "'" not in lo:
            z = float(lonsplit[0][x])+float(lo)/60
      else:
            z = float(lonsplit[0][x])+float(lo[:-1])/60
      list_of_lons.append(z)   
         
  if HS == 'W':  # If we are in Western Hemisphere, check that the longitude gets the negative number
    for x in [*range(0,len(list_of_lons),1)]:  
      if list_of_lons[x] > 0: # account for some coordinates being positive
         list_of_lons[x] = list_of_lons[x] *-1     
                   
       
  df['Longitude'] = list_of_lons
  df['Latitude'] = list_of_lats
  return(df) 



#
"""

def LonLat_cleaner(df):
  list_of_lons = []   
  list_of_lats = []
  # I need to include a switch for nan's
  # I need to include a switch for east/west
  lonsplit = df.Longitude.str.split('°', expand=True)
  latsplit = df.Latitude.str.split('°', expand=True)
  for x in [*range(0,len(latsplit),1)]:
      la = latsplit[1][x]
      lo = lonsplit[1][x]
      if "'" not in la: #70˚19.12	126˚25.07	
        y = float(latsplit[0][x])+float(la)/60
      else: #70˚19.12'	126˚25.07'	
        y = float(latsplit[0][x])+float(la[:-1])/60
      list_of_lats.append(y)

      if "'" not in lo:
            z = float(lonsplit[0][x])+float(lo)/60
      else:
            z = float(lonsplit[0][x])+float(lo[:-1])/60
       
      if z > 0: # account for some coordinates being positive
           z = z *-1     
      else: 
             z = z         
      list_of_lons.append(z)
  
     
       
  df['Longitude'] = list_of_lons
  df['Latitude'] = list_of_lats
  return(df) 
  """