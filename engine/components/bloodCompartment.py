class BloodCompartment:

    def __init__(self, **args):
        # initialize the super class
        super().__init__()

        # state properties (accessible from outside)

        # local state properties
        self._model = {}

        # set the attributes
        for key, value in args.items():
            setattr(self, key, value)

    def model_step(self, current_model):
        # only calculate the model cycle if this model is enabled
        if self.is_enabled:
            # store a reference to the current model so this model can access the other models
            self._model = current_model
            # do the model cycle
            self.model_cycle()

    def model_cycle(self):
        pass



