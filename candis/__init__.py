# module - candis
from candis.config  import Config, get_config, CONFIG
from candis.manager import Cache
from candis.data    import entrez, cdata
from candis.cli     import main

__version__ = CONFIG.VERSION
