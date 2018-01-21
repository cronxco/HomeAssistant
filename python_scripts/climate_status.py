# @Author: Will Scott <willscott>
# @Date:   21/01/2018 16:54
# @Project: Ambassadr Home Automation
# @Last modified by:   willscott
# @Last modified time: 21/01/2018 17:02

########################################
#
#          Climate UI Script
#      An over-engineered solution!
#
########################################

show_card = True

current = hass.states.get('sensor.heating_temperature')
target = hass.states.get('sensor.heating_set_temp')
power = hass.states.get('sensor.heating_heating')

if show_card:
    hass.states.set('sensor.summary', '', {
      'custom_ui_state_card': 'state-card-climate',
      'current': current,
      'target': target,
      'power': power
    })
