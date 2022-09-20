# -*- coding: utf-8 -*-

TITLE = "Title"
TRI = "Tri"
CATEGORY = "Category"
TAGS = "Tags"
TRAD = "Trad"

KEYS = ( TITLE,
  TRI,
  CATEGORY,
  TAGS,
  TRAD,
)

SEP = ":"

class Word:
    
    def __init__( self, **kwargs ):
        self.__dict__.update((key, kwargs[key])
                     for key in ( k.lower() for k in KEYS )
                     if key in kwargs)

    def __lt__( self, other ):
        return self.tri < other.tri


    def __repr__( self ):
        return f"<{self.__class__} {self.category} > {self.tags}:{self.title}>"


    @classmethod
    def from_file( cls , path ):
        word_dict = {}
        with open( path ) as f:
            for line in f.readlines():
                splits = line.split( SEP )
                if splits[0] not in KEYS:
                    continue 
                key = splits[0]
                value = splits[1]
                if key in KEYS:
                    word_dict[key.strip().lower()] =  value.strip()
        return Word( **word_dict )
        
