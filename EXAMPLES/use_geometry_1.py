import sys
import alpha.mathlib.geometry as geometry  # find and run geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

print(geometry.PI)

# 1. current folder
# 2. folders in PYTHONPATH   Windows "dir1;dir2;dir3"  Mac/Linux "dir1:dir2:dir3"
# 3. <install-folder>/lib  or similar  .../site-lib

for path in sys.path:
    print(path)

# print(f"{sys.modules['geometry'] = }")
# import re
# print(f"{sys.modules['re'] = }")
