import data_provader as prov
import loger as log

def temperature_view(sensor):
    data = prov.get_temperature(sensor)
    log.temper_logger(data)
    return data

def pressure_view(sensor):
    data = prov.get_preassure(sensor)
    log.pressure_logger(data)
    return data

def wind_speed_view(sensor):
    data = prov.get_wide_speed(sensor)
    log.wind_speed_logger(data)
    return data