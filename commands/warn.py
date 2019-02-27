from discord.utils import get

settings = {
    'name': 'warn',
    'mod_cmd': True,
}

async def main(client, message, params):
    not_warned = []
    punishrole = get(client.get_guild(531445761733296130).roles, id=533336650139435021)
    
    for member in message.mentions:
        warned = punishrole in member.roles
        if not warned:
            await member.add_roles(punishrole)
        else:
            not_warned.append(member)
    
    await message.channel.send(content=len(message.mentions) + ' Benutzer verwarnt!' 
                                       if len(not_warned) == 0 
                                       else 'Benutzer ' +
                                            ', '.join(map(lambda member: member.name, not_warned)) +
                                            ' wurden bereits einmal verwarnt!')
