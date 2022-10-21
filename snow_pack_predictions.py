import math

# here we're going to predict snowpack of different areas based on their location, la nina/el nino years, maybe other's
# hopefully. I honestly just need to get a good idea of what things impact snowpack because I don't really know

# highest importance for snowfall appear to be relative humidity and longitude, so I can add if/else for that

def snowfall_predictor(pressure, temp, relative_humidity):

    # cold enough for snow?
    if cold_enough_for_snow(pressure, temp) == True:
        return 'Cold enough for snow'
    elif cold_enough_for_snow(pressure, temp) == False:
        return 'Not cold enough for snow, perhaps rain'
    # first, ask whether snow will fall under atmospheric conditions
    # need to figure out how to use that damn clausius equation first, but once I do that it's a linear model
        # if snow will fall, find the nearest stations using knn
            # use a knn to find and weight nearest altitude as well
            # find some way to weight the nearest stations and what not as well
                # after nearest stations have been found, check if it's an el nino/la nina year to narrow down predictions
                # might want to see if there's a way to split stations based on the side of the divide and then do knn for
                # the stations on that given side, look for GIS data perhaps
                    # if it's a la nina year, take x number of samples of y readings from the given month and conditions
                    # if it's a la nina year, take x number of samples of y readings from the given month and conditions
                        # take averages of the x samles of y sizes and return this data
                        # maybe even return the individual average of the samples of samples
        # if snow will not fall, return rain or sleet
    return ''

# will use this to determine the temperature needed for deposition that will lead to snow forming
def claus_clap(cur_press, temp):
    delta_h = 46700 # j/mol
    conv_fact = 8.314/0.08206 # J / L atm
    V_solid = 50.88 # mol/L
    # need to figure out the volume of the water vapor given the temperature and pressure at altitude
    # this may be less accurate as it relies on the ideal gas law, but again, this is all just an estimation
    V_gas = mol_vol_water(cur_press, temp)
    delta_v = V_gas - V_solid
    delta_p = abs(1 - cur_press)
    delta_T = 273 * math.e**(((delta_v * delta_p) / delta_h) * conv_fact)
    return delta_T

# assuming 1mol of h2o
# may change to have different mols based on the actual relative atmospheric humidity
# will need to look into this more I think
def mol_vol_water(press, temp):
    R = 0.082057 # L * atm * K^-1 * mol^-1
    return (R * temp) / press

# this just returns the results of the clause_clap formula and changes it into a true or false answer to move on to the
# next part of the prediction
def cold_enough_for_snow(press, temp):
    delta_t = claus_clap(press, temp) # delta_t is the temp needed to freeze while temp is the current temperature condition
    if temp <= delta_t:
        return True
    else:
        return False




print(claus_clap(1, 273))




snowfall_predictor(r'C:\Users\Camden\PycharmProject\machine_learning_practice\training_data\snowpack_data.xlsx')