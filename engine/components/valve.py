from math import pow
class Valve:

    def __init__(self, **args):
        # initialize the super class
        super().__init__()

        # state properties (accessible from outside)
        self.res = 0.0
        self.real_flow = 0.0
        self.r_for = 1.0
        self.r_back = 1.0
        self.r_for_fac = 1.0
        self.r_back_fac = 1.0
        self.r_k1 = 0.0
        self.r_k2 = 0.0
        self.r_k1_fac = 1.0
        self.r_k2_fac = 1.0
        self.comp_from = {}
        self.comp_to = {}
        self.no_flow = False
        self.no_backflow = False

        # local state properties
        self._model = {}
        self._prev_flow = 0
        self._flow = 0
        self._comp1 = {}
        self._comp2 = {}

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
        # find the components and store them
        self._comp1 = self._model['components'][self.comp_from]
        self._comp2 = self._model['components'][self.comp_to]

        # calculate the current resistance
        self.res = self.calc_resistance()

        # find the flow direction
        if self.no_flow == False:
            if (self._comp1.pres > self._comp2.pres):
                # calculate the flow from comp1 to comp2
                self._flow = (self._comp1.pres - self._comp2.pres) / self.res
                # remove blood from comp1 (in litres)
                self._comp1.volume_out(self._flow * self._model['modeling_stepsize'])
                # add blood to comp2 (in litres0
                self._comp2.volume_in(self._flow * self._model['modeling_stepsize'], self._comp1)
                # store the real flow
                self.real_flow = self._flow
            else:
                if self.no_backflow:
                    self._flow = 0.0
                    self.real_flow = 0.0
                else:
                    # calculate the flow from comp2 to comp1
                    self._flow = (self._comp2.pres - self._comp1.pres) / self.res
                    # remove blood from comp2 (in litres)
                    self._comp2.volume_out(self._flow * self._model['modeling_stepsize'])
                    # add blood to comp1 (in litres0
                    self._comp1.volume_in(self._flow * self._model['modeling_stepsize'], self._comp2)
                    # store the real flow
                    self.real_flow = -self._flow
        else:
            self._flow = 0.0
            self.real_flow = 0.0

    def calc_resistance(self):
        # calculate the nonlinear flow dependent parts
        nonlin_fac1 = self.r_k1 * self.r_k1_fac * self._flow
        nonlin_fac2 = self.r_k2 * self.r_k2_fac * pow(self._flow, 2)

        # calculate the resistance depending on the flow direction
        if self._comp1.pres > self._comp2.pres:
            return self.r_for * self.r_for_fac + nonlin_fac1 + nonlin_fac2
        else:
            return self.r_back * self.r_back_fac + nonlin_fac1 + nonlin_fac2


