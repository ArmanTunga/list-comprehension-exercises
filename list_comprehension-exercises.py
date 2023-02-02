##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

# # TASK 1: Using the List Comprehension structure, capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.
# ###############################################
#
# # Beklenen Çıktı
# # Expected Output
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.

# # Notes:
# # Non-numeric names should also grow.
# # Must be done with a single list comp structure.


import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns

# ANSWER ------->
# cols = [f"NUM_{col}".upper() if df[col].dtype in ["integer", "float"] else col.upper() for col in df]
# This is a different approach
cols = [f"NUM_{col}".upper() if pd.api.types.is_numeric_dtype(df[col]) else col.upper() for col in df]
cols
# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.

# # TASK 2: Using the List Comprehension structure, write "FLAG" after the names of the variables in the car_crashes data that do not contain "no" in their names.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.

# # Notes:
# # Non-numeric names should also grow.
# # Must be done with a single list comp structure.

# # Beklenen çıktı:
# # Expected Output:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']

# ANSWER ------->
df.head()  # only to check
cols = [f"{col}_FLAG".upper() if "no" not in col else col.upper() for col in df]
cols
# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

# # Task 3: Using the List Comprehension structure, select the names of the variables that are DIFFERENT from the variable names given below and create a new dataframe.
# ###############################################

og_list = ["abbrev", "no_previous"]

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.

## Notes:
# # First, create a new list named new_cols using list comprehension according to the list above.
# # Then create a new df by selecting these variables with df[new_cols] and name it new_df.

# # Beklenen çıktı:
# # Expected Output:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#

# ANSWER ------->
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df if col not in og_list]
#  new_cols
df_new = df[new_cols]
df_new.head()
