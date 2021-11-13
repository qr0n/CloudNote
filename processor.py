import os

def debug():
  if os.environ['debug'].lower() == "true":
    return bool(True)
  elif os.environ['debug'].lower() == "false":
    return bool(False)
  else:
    return bool(False)