import json


f = open('Navinkumar Maharajan - sales_data.txt', 'r')
data = f.read()
data_1 = data.replace("'", '"')
data_2 = f"[\n{data_1}\n]"
finaldataset = data_2.replace("}\n{", "},\n{")
parsed_data = json.loads(finaldataset)
m = open("data.json", "w")
json.dump(parsed_data, m, indent=4)  
print("Data loaded and written to data.json successfully!")

