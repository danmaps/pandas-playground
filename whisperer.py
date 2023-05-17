import arcpy

# select cities with population greater than average
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="cities",
    selection_type="NEW_SELECTION",
    where_clause="POPULATION > (SELECT AVG(POPULATION) FROM cities_sorted)",
    invert_where_clause=None
)

# clear the selection
arcpy.management.SelectLayerByAttribute("cities","CLEAR_SELECTION")

# select cities with population over 1 million in the state of california

arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="cities",
    selection_type="NEW_SELECTION",
    selection_type="NEW_SELECTION",
    where_clause="POPULATION > 1000000 AND STATE = 'CA'",
    invert_where_clause=None
    )

# clear the selection

arcpy.management.SelectLayerByAttribute("cities","CLEAR_SELECTION") 