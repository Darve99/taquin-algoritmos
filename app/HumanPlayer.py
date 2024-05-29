## ========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## ========================================================================

import sys
sys.path.append( '../lib/python3' )
from Taquin import Taquin

w, h = [ int( v ) for v in sys.argv[ 1 : 3 ] ]
b = Taquin( w, h )

m = { 'a': 'left', 'd': 'right', 's': 'down', 'w': 'up' }

print( b )
print( b.is_solved( ) )
b.shuffle( )
print( '***********************' )
print( b )
print( b.is_solved( ) )
print( '***********************' )

while not b.is_solved( ):
  d = input( 'Move: ' )
  b.move( m[ d ] )
  print( '***********************' )
  print( b )
# end while

## eof - $RCSfile$
