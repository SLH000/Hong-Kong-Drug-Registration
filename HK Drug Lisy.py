#%%
import xml.etree.ElementTree as ET
import pandas as pd


#%%
# Load and parse the XML file
xml_file = "DrugList.xml"  
tree = ET.parse(xml_file)
root = tree.getroot()

#%%
# Initialize a list to store drug data
drug_data = []

# Extract data and store in the list
for drug in root.findall('drug'):
    product_name = drug.find('productName').text
    reg_cert_holder = drug.find('regCertHolderName').text
    permit_no = drug.find('permitNo').text
    active_ings = ", ".join([ing.text for ing in drug.find('activeIngs').findall('activeIng')])
    
    # Append the data as a dictionary
    drug_data.append({
        "Product Name": product_name,
        "Reg. Certificate Holder": reg_cert_holder,
        "Permit No": permit_no,
        "Active Ingredients": active_ings
    })
    
#%%
# Create a DataFrame
df = pd.DataFrame(drug_data)

# Display the DataFrame
print(df)

#%%
# Save to a CSV file
df.to_csv("drug_data.csv", index=False)
# %%
