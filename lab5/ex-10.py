import re
capitals = "SymatWillTravelArroundTheWorld"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', capitals)
x = x.lower()
print(x)