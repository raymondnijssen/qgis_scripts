# qgis_scripts
Handy scripts for qgis :)


# scratchlayer.py

## ScratchLayer()

Quickly creates a memory layer for displaying geometries.

Usage:

```python
lsl = ScratchLayer('lines', 'LineString')
lsl.addGeometry(QgsGeometry('LINESTRING((0 0, 1 0, 1 1))', 'line1'))
lsl.addGeometry(QgsGeometry('LINESTRING((1 1, 0 2, 2 2))', 'line2'))
lsl.refresh()
```
