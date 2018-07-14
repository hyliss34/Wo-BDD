
key = "8kwsy7n2nwxbepk857uuhf9ycer9rmg5"
base_wow = "https://eu.api.battle.net/wow/"

# Guild members
guild = "guild"
server = "Ysondre"
name = "Waít for it"
method = "fields=members"
locale = "&locale=fr_FR"
api = "&apikey="+key




def get_and_add_guild_to_DB(name, server):
    """
    Add a new guild to the database

    Args:
        name (str): name of the guild
        server (str): name of the server
    """
    add_guild(name, server)
    update_guild_members(name, server)

def update_guild_members(name, server):
    """
    Update data of a guild in the database

    Args:
        name (str): name of the guild
        server (str): name of the server
    """
    url = base_wow + guild+"/"+ server+"/"+ name+"?"+ method + locale + api
    r = requests.get(url)
    data = r.json()
    guilde = data['name']
    for member in data["members"]:
        add_member(guilde, member['character']['name'], member['rank'], member['character']['level'])
