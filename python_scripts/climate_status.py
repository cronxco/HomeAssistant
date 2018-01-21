# @Author: Will Scott <willscott>
# @Date:   21/01/2018 16:54
# @Project: Ambassadr Home Automation
# @Last modified by:   willscott
# @Last modified time: 21/01/2018 20:10

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

current = round(float(hass.states.get('sensor.heating_temperature').state),1)
target = round(float(hass.states.get('sensor.heating_set_temp').state),1)
power = round(float(hass.states.get('sensor.heating_heating').state),0)

if show_card:
    hass.states.set('sensor.heating', target, {
      'custom_ui_state_card': 'state-card-heating',
      'current': current,
      'target': target,
      'power': power
    })
