import fiona

with fiona.open('data/coral-data/Benthic-Map/benthic.gpkg') as layer:
    for feature in layer:
        print(feature)
