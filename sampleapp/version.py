from pathlib import Path
# Open version.txt file
sample_app_dir = Path(__file__).resolve().parent
def get_version(versionFile=sample_app_dir / 'version.txt'):
  f = open(versionFile, 'r')
  # Read APP_VERSION and display version
  version = f.readline()
  f.close()
  return version

if __name__ == "__main__":
  print(get_version(sample_app_dir / 'version.txt'))