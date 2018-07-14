
import pymysql


def do(command, vars):
    """
    Execute a SQL command

    Args:
        command (str): a command
        vars (tuple): variables

    Note:
        truc

    Examples:
        dâd

    """
    db = pymysql.connect("localhost", "root", "marram34", "wow")
    cursor = db.cursor()
    try:
        if vars is not None:
            cursor.execute(command,vars)
        else:
            cursor.execute(command)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        cursor.close()

def add_guild(name, server):
    """
    Add a guild to thed database

    .. _NEAR CLIFFORD:
        https://arxiv.org/abs/1703.00111

    Args:
        name (str): name of the guild :meth:`MyBDD.do`
        server (str): name of the server

    """
    name = name.replace(' ', '_')
    command = "INSERT INTO guilds (name, server) VALUES (%s, %s)"
    vars = (name, server)
    do(command, vars)
    command = """CREATE TABLE IF NOT EXISTS %s
        (
            `ID` INT AUTO_INCREMENT NOT NULL,
            `name` VARCHAR( 200 ) NOT NULL,
            `rang` INT NOT NULL,
            `level` INT NOT NULL,
            PRIMARY KEY ( `ID` )
        )"""%(name)

    vars = None
    do(command, vars)

        
def add_member(guild_name, name, rang, level):
    """
    Add a member in a guild table

    Args:
        guild_name (str): name of the guild
        name (str): name of the member to add
        rang (int): rank of the member
        level (int): level of the member
    """
    guild_name = guild_name.replace(' ', '_')
    command = "INSERT INTO "+guild_name+" (name, rang, level) VALUES (%s, %s, %s)"
    vars = (name, rang, level)
    do(command, vars)

class ExampleError(Exception):
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (Optional[int]): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
