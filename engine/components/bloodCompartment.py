class BloodCompartment:

    def __init__(self, **args):
        super().__init__()

        # set the attributes
        for key, value in args.items():
            setattr(self, key, value)

        print('blood compartment {} initialized'.format(self.name))

    def model_step(self):
        # only update the model if it is enabled
        if self.is_enabled:
            self.model_cycle()

    def model_cycle(self):
        pass
