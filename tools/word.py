# -*- coding: utf-8 -*-

from slugify import slugify
import os.path

TITLE = "Title"
TRI = "Tri"
CATEGORY = "Category"
TAGS = "Tags"
TRAD = "Trad"
CONTENT_PATH = "content"

KEYS = ( TITLE,
  TRI,
  CATEGORY,
  TAGS,
  TRAD,
)

EQ_KEYS = ( TITLE,
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

    def __eq__( self, other ):
        for key in ( k.lower() for k in EQ_KEYS ):
            if self.__dict__[key] != other.__dict__[key]:
                return False
            return True

    def __repr__( self ):
        return f"<{self.__class__} path = {self.path} : {self.title}>"


    def to_french( self ):
        words, errors = [], []
        if any( self.__dict__[key] == UNDEFINED
                for key in ( k.lower() for k in KEYS )):
            return [],[self.path] 
        for trad in self.trad.split(TRAD_SEP):
            trad = trad.strip().capitalize()
            new = dict()
            new[TITLE.lower()] = trad
            new[TRI.lower()] = trad
            new[CATEGORY.lower()] = FRENCH
            new[TAGS.lower()] = slugify(trad).upper()[0]
            new[TRAD.lower()] = self.title
            words.append( Word( **new ) )
        return words, errors

    def set_path( self, path = CONTENT_PATH ):
        if self.path is not None:
            return
        slug_title = slugify( self.title )
        slug_category = slugify( self.category )
        self.path = f"{path}/{slug_category}/{self.tags}/{slug_title}.md"

    def save_or_update( self ):
        if self.path is None:
            raise ValueError( "Path is not defined" )
        if os.path.isfile(self.path):
            # We have to check for update
            # We don't want to update the tri field if there is no major change
            current = Word.from_file( self.path )
            if current == self :
                print( f"{self.path} already up to date" )
                return
        save_file = open( self.path, 'w' )
        save_file.write( f"""Title: {self.title}
 Tri: {self.tri}
 Date: 2010-12-03 10:20
 Category: {self.category}
 Tags: {self.tags}
 Trad: {self.trad}
 """)
        save_file.close()


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
        
