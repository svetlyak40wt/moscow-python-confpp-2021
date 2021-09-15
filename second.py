import logging
import sys

from IPython.core.magic import Magics, magics_class, line_magic


def log_level(new_level):
    level = getattr(logging, new_level.upper(), None)

    if level is None:
        print(
            f'Level "{new_level}" is not supported. Use info, warn, etc..',
            file=sys.stderr,
        )
    else:
        logging.getLogger().setLevel(level)


@magics_class
class LogLevelManager(Magics):
    @line_magic
    def info(self, line):
        log_level('INFO')

    @line_magic
    def error(self, line):
        log_level('ERROR')


def load_ipython_extension(ipython):
    print('Loading "second" extension')
    
    logging.basicConfig(
        format='%(levelname)s [%(name)s]: %(message)s',
        force=True,
        level=logging.ERROR,
    )

    extension = LogLevelManager()
    ipython.register_magics(extension)

    ipython.user_ns['log_level'] = log_level
