# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

def check_for_colab():
  try:
      import google.colab
      return True
  except ImportError:
      return False
  

def mount_gdrive(gdrive_mnt = '/content/drive'):
  if not check_for_colab():
    return
  
  from google.colab import drive
  drive.mount(gdrive_mnt, force_remount=True)



def unmount_gdrive():
  if not check_for_colab():
    return
  
  from google.colab import drive
  drive.flush_and_unmount()