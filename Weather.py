from pyowm import OWM
#from pyowm.utils import config
#from pyowm.utils import timestamps

from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. French

#owm = OWM('823c1825a5d89946290e0a1d11172f2c')
owm = OWM('6d00d1d4e704068d70191bad2673e0cc',config_dict)
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Чебоксары')
w = observation.weather

print( "Сейчас в Чебоксарах " + w.detailed_status )
print( "Температура " + str(int(w.temperature('celsius')["temp"])) + " Градусов" )
input()
