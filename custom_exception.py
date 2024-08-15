
class WombatException(Exception):
    pass

def animals():
    raise WombatException("there are no wombats!")


try:
    animals()
except WombatException as err:
    print(err)
