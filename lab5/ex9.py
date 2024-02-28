import re
capitals = "Symbataminasomeoneaizhanbalzhan"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', capitals)
print(x)