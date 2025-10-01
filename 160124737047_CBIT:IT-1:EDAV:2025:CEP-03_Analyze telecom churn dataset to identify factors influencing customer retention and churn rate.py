# We must run this code in google colab
# if you need to run it in your system make sure you change the file path and install pandas using pip install pandas
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
df=pd.read_csv("/content/drive/My Drive/Colab Notebooks/telecom_customer_churn.csv")
print(df.head())
print(df.info())