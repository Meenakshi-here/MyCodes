#Manual Garbage Collection


import gc
collected = gc.collect()
print("Garbage collector: collected",
          "%d objects." % collected)
