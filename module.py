import sys

print(sys.version)

import pyjokes # type: ignore
joke = pyjokes.get_joke()
print (joke)
