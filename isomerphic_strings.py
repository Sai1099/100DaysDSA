c1 = str(input())

c2 = str(input())
def ismorphic_str(c1,c2):
  mapST={}
  mapTS = {}
  ##if not using zip for i in rnage(len(c2)):
        # c1 = T[I]
         # C2 = S[I]
  for c1,c2 in zip(mapST,mapTS):
      if(c1 in mapST and mapST[c1] != c2 ) or c2 in mapTS and mapTS[c2] !=c1:
          return False
      mapST[c1] =c2
      mapTS[c2] =c1
        
  return True
