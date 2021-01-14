class Ecg:

  def __init__(self):
    self.is_enabled = False
    print('ecg initialized')

  def model_step(self):
    if (self.is_enabled):
      self.model_cycle()

  def model_cycle(self):
    pass