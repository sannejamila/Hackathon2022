import pystac_client
#change this to relevant
example_area_of_interest = {
"coordinates": [
[
[158.3, -19],
[158.4, -20],
[158.3, -19],
[158.4, -20]
],
],
}

def search(area_of_interest, collections=["landsat-8-c2-l2"]):
  api = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1/")
  search_2017 = api.search(
    intersects=area_of_interest,
    limit=500,
    collections=collections,
  )

