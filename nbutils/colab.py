# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

def check_for_colab():
  try:
      import google.colab
      return True
  except ImportError:
      return False