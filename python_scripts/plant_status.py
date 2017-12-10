# @Author: Will Scott <willscott>
# @Date:   04/09/2017 20:06
# @Project: Ambassadr Home Automation
# @Last modified by:   willscott
# @Last modified time: 10/12/2017 11:15

problemPlants = 0
allproblemPlants = []
waterPlants = []
numberWater = 0
fertilizePlants = []
numberFertilize = 0
whichIcon = "mdi:help-circle-outline"

for entity_id in hass.states.entity_ids('plant'):
    state = hass.states.get(entity_id)
    boolean_entity = entity_id.replace('plant.', 'input_boolean.plant_')
    boolean_state = ass.states.get(switch_entity)
    if state.state == 'problem' and switch_state.state == 'on':
        problemPlants = problemPlants + 1
        allproblemPlants.append(state.name)
        problem = state.attributes.get('problem') or 'none'
        if "conductivity low" in problem:
          fertilizePlants.append(state.name)
          numberFertilize = numberFertilize + 1
        if "moisture low" in problem:
          waterPlants.append(state.name)
          numberWater = numberWater + 1

# Set icon
if problemPlants > 0:
  whichIcon = "mdi:alert-circle-outline"
else:
  whichIcon = "mdi:check-circle-outline"

# Set states
hass.states.set('sensor.water_plants', problemPlants, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Problem Plants',
    'icon': whichIcon,
    'problem_plants': allproblemPlants,
    'water': waterPlants,
    'water_number': numberWater,
    'fertilize': fertilizePlants,
    'fertilize_number': numberFertilize
})
