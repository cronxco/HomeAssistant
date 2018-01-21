# @Author: Will Scott <willscott>
# @Date:   21/01/2018 16:54
# @Project: Ambassadr Home Automation
# @Last modified by:   willscott
# @Last modified time: 21/01/2018 17:37

########################################
#
#          Climate UI Script
#      An over-engineered solution!
#
########################################

show_card = True

current = hass.states.get('sensor.heating_temperature').state
target = hass.states.get('sensor.heating_set_temp').state
power = hass.states.get('sensor.heating_heating').state

if show_card:
    hass.states.set('sensor.heating', '', {
      'custom_ui_state_card': 'state-card-climate',
      'current': current,
      'target': target,
      'power': power
    })
