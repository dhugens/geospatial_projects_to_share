from arcgis.gis import GIS
import pandas as pd
import datetime as dt

# Connect to ArcGIS Online (You may need OAuth or stored credentials)
print("enter ArcGIS Online org name")
print("this is the name before 'maps.arcgis.com...'")
AGOL_Org = input()

print("enter ArcGIS Online username:")
print("please note: this requires a username/password combo and WILL NOT work with a SAML or other SSO config")
username = input()

print("enter password:")
password = input()

print("enter folder path for intended library index:")
agol_path = input()
agol_library = agol_path + "_index" + str(dt.datetime) + "index.csv"

agolurl = "https://" + AGOL_Org + ".maps.arcgis.com/home/organization.html"
gis = GIS(agolurl, username, password)

# Get the items in My Content
user = gis.users.me
items = user.items(max_items=750)  # Adjust max_items if needed

# Extract details
data = []
for item in items:
    data.append({
        "Title": item.title,
        "Type": item.type,
        "ID": item.id,
        "Created": item.created,
        "Modified": item.modified,
        "Owner": item.owner,
        "Folder": item.ownerFolder or "Root",
        "Tags": ", ".join(item.tags) if item.tags else "",
        "Categories": ", ".join(item.categories) if hasattr(item, "categories") else ""
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv(agol_library, index=False)

print("Export complete!")