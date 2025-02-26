def build_bridge(chunk,goal):
  if chunk%(2.5*goal)==0:
    return True
  else:
    return False

print(build_bridge(18,2))


# rozwiązanie Kodilli
# def build_bridge(chunk, goal):
#   junction = chunk / 2
#   x = (goal + (junction * 1))/(chunk + junction)
#   return True if x.is_integer() else False