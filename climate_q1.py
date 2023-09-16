import matplotlib.pyplot as plt

import sqlite3


connection = sqlite3.connect("climate.db")
cursor = connection.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
res = cursor.fetchall()
    

for table_data in res:
    table_name = table_data[0]
    cursor.execute(f"SELECT * FROM {table_name}")
    column_names = sqlite3.Row(cursor,(1,)).keys()
    print(column_names)
da = cursor.execute("SELECT * FROM ClimateData;")
for j in da:
    print(j)

years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
