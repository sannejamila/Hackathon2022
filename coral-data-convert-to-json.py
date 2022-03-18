import fiona
import json
import os
data = []
with fiona.open('data/coral-data/Benthic-Map/benthic.gpkg') as layer:
    for feature in layer:
        if (feature['properties']['class'] == 'Coral/Algae'):
            data.append(feature)


os.makedirs("data", exist_ok=True)

with open("data/benthic.json", "w") as f:
    json.dump(data, f)