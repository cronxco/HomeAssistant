# @Author: Will Scott <willscott>
# @Date:   21/01/2018 16:54
# @Project: Ambassadr Home Automation
# @Last modified by:   willscott
# @Last modified time: 21/01/2018 19:52

########################################
#
#          Climate UI Script
#      An over-engineered solution!
#
########################################

show_card = True

current = ''
target = ''
power = ''

current = round(hass.states.get('sensor.heating_temperature').state,1)
target = round(hass.states.get('sensor.heating_set_temp').state,1)
power = round(hass.states.get('sensor.heating_heating').state,0)

if show_card:
    hass.states.set('sensor.heating', target, {
      'custom_ui_state_card': 'state-card-climate',
      'current': current,
      'target': target,
      'power': power
    })
