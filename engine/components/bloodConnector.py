class BloodConnector:

  def __init__(self, **args):
    super().__init__()

    # set the attributes
    for key, value in args.items():
      setattr(self, key, value)

    print('blood connector initialized')

  def model_step(self):
    if (self.is_enabled):
      self.model_cycle()

  def model_cycle(self):
    pass