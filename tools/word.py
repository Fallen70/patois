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
TRAD_SEP = "/"
UNDEFINED = "Undefined"
FRENCH = "français"

class Word:
    
    def __init__( self, path=None, **kwargs ):
        # Valeurs par défaut
        self.__dict__.update((key, UNDEFINED )
                     for key in ( k.lower() for k in KEYS ))
        self.path = path
        self.__dict__.update((key, kwargs[key])
                     for key in ( k.lower() for k in KEYS )
                     if key in kwargs)

    def __lt__( self, other ):
        return self.tri < other.tri


    def __repr__( self ):
        return f"<{self.__class__} {self.path} : {self.title}>"


    def to_french( self ):
        words, errors = [], []
        if any( self.__dict__[key] == UNDEFINED
                for key in ( k.lower() for k in KEYS )):
            return [],[self.path] 
        for trad in self.trad.split("/"):
            trad = trad.strip().capitalize()
            new = dict()
            new[TITLE.lower()] = trad
            new[TRI.lower()] = trad
            new[CATEGORY.lower()] = FRENCH
            new[TAGS.lower()] = trad[0]
            new[TRAD.lower()] = self.title
            words.append( Word( **new ) )
        return words, errors
        


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
        return Word( path=path, **word_dict )
        
