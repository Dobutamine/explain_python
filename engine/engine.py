# import all the components
from engine.components import bloodCompartment, bloodConnector, valve, gasCompartment, gasConnector, container, \
    diffusor, exchanger
from engine.components import ecg, heart, ans, breathing, lungs, kidneys, metabolism, brain, adaption, birth, cvvh, \
    drugs, ecmo, liver, placenta, uterus, ventilator


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

        # initialize the ecg model
        self.current_model['components']['ecg'] = ecg.ECG(**model_definition['ecg'])

        # initialize the heart model
        self.current_model['components']['heart'] = heart.Heart(**model_definition['heart'])

        # initialize the ans model
        self.current_model['components']['ans'] = ans.ANS(**model_definition['ans'])

        # initialize the breathing model
        self.current_model['components']['breathing'] = breathing.Breathing(**model_definition['breathing'])

        # initialize the lungs model
        self.current_model['components']['lungs'] = lungs.Lungs(**model_definition['lungs'])

        # initialize the kidneys model
        self.current_model['components']['kidneys'] = kidneys.Kidneys(**model_definition['kidneys'])

        # initialize the metabolism model
        self.current_model['components']['metabolism'] = metabolism.Metabolism(**model_definition['metabolism'])

        # initialize the brain model
        self.current_model['components']['brain'] = brain.Brain(**model_definition['brain'])

        # initialize the adaptation model
        self.current_model['components']['adaptation'] = adaption.Adaptation(**model_definition['adaptation'])

        # initialize the birth model
        self.current_model['components']['birth'] = birth.Birth(**model_definition['birth'])

        # initialize the cvvh model
        self.current_model['components']['cvvh'] = cvvh.CVVH(**model_definition['cvvh'])

        # initialize the drugs model
        self.current_model['components']['drugs'] = drugs.Drugs(**model_definition['drugs'])

        # initialize the ecmo model
        self.current_model['components']['ecmo'] = ecmo.ECMO(**model_definition['ecmo'])

        # initialize the liver model
        self.current_model['components']['liver'] = liver.Liver(**model_definition['liver'])

        # initialize the placenta model
        self.current_model['components']['placenta'] = placenta.Placenta(**model_definition['placenta'])

        # initialize the uterus model
        self.current_model['components']['uterus'] = uterus.Uterus(**model_definition['uterus'])

        # initialize the ventilator model
        self.current_model['components']['ventilator'] = ventilator.Ventilator(**model_definition['ventilator'])

        # for key, value in self.current_model['components'].items():
        #   print(key, '->', self.current_model['components'][key].name)

    def calculate_model(self, time_to_calculate):
        pass

    def fast_forward_model(self, time_to_calculate):
        pass

    def model_step(self):
        pass
