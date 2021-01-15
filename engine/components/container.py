class Container:
  def __init__(self, **args):
    # initialize the super class
    super().__init__()

    # state properties (accessible from outside)
    self.pres = 0.0
    self.pres_recoil = 0.0
    self.pres_ext = 0
    self.pres_cont = 0
    self.vol = 0
    self.vol_u = 0
    self.el = 0.0
    self.el_min = 0.0
    self.el_max = 0.0
    self.el_k1 = 0.0
    self.el_k2 = 0.0
    self.el_max_fac = 1.0
    self.el_min_fac = 1.0
    self.vol_u_fac = 1.0
    self.el_k1_fac = 1.0
    self.el_k2_fac = 1.0
    self.el_act = 0.0
    self.comps = []

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

  def calc_volume(self):
    # define the total volume variable

    total_volume = 0
    for comp in self.comps:
      total_volume += self._model['components'][comp].vol

    return total_volume

  def calc_elastance(self):
    # calculate the base elastance
    el_base = self.el_min * self.el_min_fac

    # calculate the first nonlinear factor
    nonlin_fac1 = self.el_k1 * self.el_k1_fac * (self.vol - (self.vol_u * self.vol_u_fac))

    # calculate the second nonlinear factor
    nonlin_fac2 = self.el_k2 * self.el_k2_fac * pow((self.vol - (self.vol_u * self.vol_u_fac)), 2)

    # calculate the contraction (=varying elastance factor)
    el_cont = self.el_max * self.el_max_fac * self.el_act

    # return the total elastance
    return el_base + nonlin_fac1 + nonlin_fac2 + el_cont

  def calc_pressure(self):
    # calculate current elastance
    self.el = self.calc_elastance()

    # calculate the current recoil pressure
    self.pres_recoil = (self.vol - (self.vol_u * self.vol_u_fac)) * self.el

    # return the sum of all pressures
    return self.pres_recoil + self.pres_ext + self.pres_cont

  def change_volume(self, dvol):
    # change the volume
    self.vol += dvol

    # guard against negative volumes
    if self.vol < 0:
      self.vol = 0

  def model_cycle(self):
    # calculate the container volume by adding all volumes it contains together
    self.vol = self.calc_volume()

    # calculate the pressure
    self.pres = self.calc_pressure()

    # transfer the container pressure to the contained compartments
    for comp in self.comps:
      self._model['components'][comp].pres_cont = self.pres