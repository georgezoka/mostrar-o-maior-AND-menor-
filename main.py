#básico...
def meior(cole):
  maiori = cole[0]
  for i in cole:
    if i > maiori:
      maiori = i 
  return maiori
print(meior([0,1,2,3]), 'maior item')

def menor(lom):
  ver = lom[0]
  for i in lom:
    if i < ver:
      ver = i
  return ver 
  
print(menor([0,1,2,3]), 'menor item')