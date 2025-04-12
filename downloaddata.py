import urllib
import urllib.request
import os




file_path = os.path.join("datasets","housing")
os.makedirs(file_path,exist_ok=True)
file_path = os.path.join(file_path,"housing.csv")

urllib.request.urlretrieve("https://raw.githubusercontent.com/bjnaga/ML-lab/refs/heads/main/datasets/housing.csv", file_path)
