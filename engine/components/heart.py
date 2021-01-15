import math
class Heart:

  def __init__(self, **args):
    # initialize the super class
    super().__init__()

    # state properties (accessible from outside)
    self.aaf = 0.0
    self.vaf = 0.0

    # local state properties
    self._model = {}

    # set the attributes from the model definition file
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
    # get the modeling stepsize
    t = self._model['modeling_stepsize']

    # get the relevant timings from the ecg model
    ncc_atrial = self._model['components']['ecg'].ncc_atrial
    atrial_duration = self._model['components']['ecg'].pq_time
    ncc_ventricular = self._model['components']['ecg'].ncc_ventricular
    ventricular_duration = self._model['components']['ecg'].cqt_time + self._model['components']['ecg'].qrs_time

    # varying elastance activation function of the atria
    if ncc_atrial >= 0 and (ncc_atrial < atrial_duration / t):
      self.aaf = math.pow(math.sin(math.pi * (ncc_atrial / atrial_duration) * t), 2)
    else:
      self.aaf = 0

    # varying elastance activation function of the ventricles
    if ncc_ventricular >= 0 and (ncc_ventricular < ventricular_duration / t):
      self.vaf = math.pow(math.sin(math.pi * (ncc_ventricular / ventricular_duration) * t), 2)
    else:
      self.vaf = 0

    # increase the atrial and ventricular activation function timers
    self._model['components']['ecg'].ncc_atrial += 1
    self._model['components']['ecg'].ncc_ventricular += 1

    # transfer the activation function to the heart compartments
    self._model['components']['RA'].el_act = self.aaf
    self._model['components']['RV'].el_act = self.vaf
    self._model['components']['LA'].el_act = self.aaf
    self._model['components']['LV'].el_act = self.vaf



