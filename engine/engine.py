# import all the components
from engine.components.ecg import Ecg
from engine.components import bloodCompartment, bloodConnector, valve, gasCompartment, gasConnector, container, diffusor, exchanger

class Engine:

  def __init__(self):

    # define an object holding the entire model state and properties
    self.current_model = {}

    # define an object holding the model definition as defined by the json definition file
    self.model_definition = {}

    # define an object holding the interventions which need to be applied to the model
    self.interventions = {}

    # define an object holding the datalogger 
    self.datalogger = {}

    # define an object holding the current model time
    self.model_time_total = 0

    # signal that the engine class is initalized
    print('engine instantiated')

  def load_model(self, json_model_definition):
    pass

  def inject_modeldefinition(self, model_definition):

    # declare components object holding all the model components
    self.current_model['components'] = {}

    # initialize all the blood compartments
    _class = getattr(bloodCompartment, "BloodCompartment")
    for definition in model_definition['blood_compartment_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)

    # initialize all the blood connectors
    _class = getattr(bloodConnector, "BloodConnector")
    for definition in model_definition['blood_connector_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)

    # initialize all the valves
    _class = getattr(valve, "Valve")
    for definition in model_definition['valve_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)

    # initialize all the gas compartments
    _class = getattr(gasCompartment, "GasCompartment")
    for definition in model_definition['gas_compartment_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)

    # initialize all the gas connectors
    _class = getattr(gasConnector, "GasConnector")
    for definition in model_definition['gas_connector_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)

    # initialize all the containers
    _class = getattr(container, "Container")
    for definition in model_definition['container_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)

    # initialize all the exchangers
    _class = getattr(exchanger, "Exchanger")
    for definition in model_definition['exchanger_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)

    # initialize all the diffusors
    _class = getattr(diffusor, "Diffusor")
    for definition in model_definition['diffusor_definitions']:
        self.current_model['components'][definition['name']] = _class(**definition)



    for key, value in self.current_model['components'].items():
      print(key, '->', self.current_model['components'][key].name)

  def calculate_model(self, time_to_calculate):
    pass

  def fast_forward_model(self, time_to_calculate):
    pass

  def model_step(self):
    pass


