#/opt/homebrew/bin/python3
import os
home_directory = os.path.expanduser( '~' )
print( home_directory )
out = os.path.join( home_directory, "Downloads")
print(out)
name = os.path.dirname( home_directory, "Downloads")
print(name)
#abs = os.path.isabs( home_directory, "Downloads")
#print(abs)
