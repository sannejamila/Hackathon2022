import fiona

with fiona.open('data/load_coral_data.gpkg'') as layer:
    for feature in layer:
        print(feature)
