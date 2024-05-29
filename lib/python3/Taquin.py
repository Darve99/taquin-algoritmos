## ========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## ========================================================================

import random

class Taquin:

  m_Board = None
  m_Size = None

  '''
  '''
  def __init__( self, w, h ):
    self.m_Size = ( w, h )
    self.m_Board = [ i for i in range( w * h ) ]
  # end if

  '''
  '''
  def __str__( self ):
    s = ''
    i = 0
    m = len( self.m_Board ) - 1
    for y in range( self.m_Size[ 1 ] ):
      s += '| '
      for x in range( self.m_Size[ 0 ] ):
        if self.m_Board[ i ] == m:
          s += '  |'
        else:
          s += chr( self.m_Board[ i ] + ord( 'A' ) ) + ' |'
        # end if
        if x < self.m_Size[ 0 ] - 1:
          s += ' '
        # end if
        i += 1
      # end for
      if y < self.m_Size[ 1 ] - 1:
        s += '\n'
      # end if
    # end for
    return s
  # end def
  
  '''
  '''
  def move( self, m ):
    v = \
      { \
      'left' : ( -1, 0 ), \
      'right': ( 1, 0 ), \
      'down' : ( 0, 1 ), \
      'up'   : ( 0, -1 ) \
      }
    p = self.m_Board.index( max( self.m_Board ) )
    c = ( p % self.m_Size[ 0 ], p // self.m_Size[ 1 ] )
    d = ( c[ 0 ] + v[ m ][ 0 ], c[ 1 ] + v[ m ][ 1 ]  )
    
    if \
      0 <= d[ 0 ] and d[ 0 ] < self.m_Size[ 0 ] \
      and \
      0 <= d[ 1 ] and d[ 1 ] < self.m_Size[ 1 ] \
      :
      q = ( self.m_Size[ 0 ] * d[ 1 ] ) + d[ 0 ]
      self.m_Board[ p ], self.m_Board[ q ] \
      = \
      self.m_Board[ q ], self.m_Board[ p ]
      return True
    else:
      return False
    # end if
  # end def
  
  '''
  '''
  def shuffle( self, N = 128 ):
    m = [ 'left', 'right', 'down', 'up' ]
    n = N
    while n > 0:
      if self.move( m[ random.randint( 0, 3 ) ] ):
        n -= 1
      # end if
    # end while
  # end def

  '''
  '''
  def __getitem__( self, d ):
    if \
      0 <= d[ 0 ] and d[ 0 ] < self.m_Size[ 0 ] \
      and \
      0 <= d[ 1 ] and d[ 1 ] < self.m_Size[ 1 ] \
      :
      return self.m_Board[ ( self.m_Size[ 0 ] * d[ 1 ] ) + d[ 0 ] ]
    else:
      return None
    # end if
  # end def

  '''
  '''
  def is_solved( self ):
    return self.m_Board == sorted( self.m_Board )
  # end def
  def __lt__(self, other):
    return self.m_Board < other.m_Board

  def copy(self):
    copied_taquin = Taquin(self.m_Size[0], self.m_Size[1])
    copied_taquin.m_Board = self.m_Board[:]  # Copia profunda de la lista
    return copied_taquin
# end class

## eof - $RCSfile$
