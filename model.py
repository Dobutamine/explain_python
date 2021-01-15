import json
from engine import engine as model_engine


class Model:

    def __init__(self, model_definition_file):
        super().__init__()

        # instantiate a new model engine
        self.engine = model_engine.Engine()

        # declare an object holding the parsed JSON definition file and load the JSON model definition file
        self.definition = self.loadModelDefinition(model_definition_file)

        # inject parsed model definition into the model engine instance
        self.engine.inject_modeldefinition(self.definition)

        # declare an object holding the data coming back from the model engine
        self.data = []

        # declare an object holding the model properties coming from the model engine
        self.properties = {}

    def setDataloggerInterval(new_interval):
        pass

    def setDataloggerWatchedModels(models_to_watch):
        pass

    def setModelState(snapshot):
        pass

    def setProperty(model, property, new_value, in_time=0, at_time=0, mode="abs"):
        pass

    def getModelState(self):
        pass

    def getModelDefinition(self):
        pass

    def getProperties(model):
        pass

    def fastForwardModel(self, to_time):
        self.engine.fast_forward_model((to_time))

    def calculateModel(self, time_to_calculate):
        self.engine.calculate_model(time_to_calculate)

    def clearData(self):
        pass

    def receiveMessageFromModel(message):
        pass

    def loadModelDefinition(self, filename):
        with open('normal_neonate.json') as f:
            loaded_model = json.load(f)
        return loaded_model


if __name__ == '__main__':
    print('')
    print('Radboudumc Lumped Varying Elastance Model python version 0.1')
    print('')

    new_model = Model('normal_neonate.json')

    new_model.fastForwardModel(10)

