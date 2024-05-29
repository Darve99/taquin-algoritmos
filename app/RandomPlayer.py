## ========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## ========================================================================

import random, sys, time
sys.path.append( '../lib/python3' )
from Taquin import Taquin

w, h = [ int( v ) for v in sys.argv[ 1 : 3 ] ]
b = Taquin( w, h )

m = [ 'left', 'right', 'down', 'up' ]

print( b )
print( b.is_solved( ) )
b.shuffle( )
print( '***********************' )
print( b )
print( b.is_solved( ) )
print( '***********************' )

while not b.is_solved( ):
  b.move( m[ random.randint( 0, 3 ) ] )
  print( '***********************' )
  print( b )
  time.sleep( 0.1 )
# end while

## eof - $RCSfile$
