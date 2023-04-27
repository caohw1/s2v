
def str_to_float_with_unit(s, unit_map):
  assert isinstance(s, str)
  u = ""
  l = len(s)
  for i in range(l-1, -1, -1):
    c = s[i];
    if (c.isdigit()): u = s[i+1:l]; s = s[0:i+1]; break
  #print("s=%s:%s" % (s, u)
  try: v = float(s)  
  except ValueError: Msg.error(s + " is not vlaue"); return None
  if (u == ""): return v
  k = unit_map.get(u)
  if (k == None): Msg.error("unknown unit " + u); return v
  return v * k  
  
  
length_unit_map = {"u"  : 1.e-6, "um" : 1.e-6,
                   "n"  : 1.e-9, "nm" : 1.e-9}    

a = str_to_float_with_unit("20u", length_unit_map)
print("a=%e" % a)

b = str_to_float_with_unit("20nm", length_unit_map)
print("a=%e" % b)
  
