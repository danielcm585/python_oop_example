class GasPedal:
  def __init__(self, acceleration: Acceleration):
    self.acceleration = acceleration
  
  def step(self, percentage: float):
    acceleration.value += percentage / 100 * 10 
  
  
class Measure:
  def __init__(self, key, value):
    self.key = key
    self.value = init_value
  
  
class Acceleration(Measure):
  def __init__(self, init_value = 0):
    super("ACC", init_value)
    
  def __repr__(self): 
    return self.value
  
  
class BrakePedal:
  def __init__(self, acceleration: Acceleration, brake_light: BrakeLight):
    self.acceleration = acceleration
    self.brake_light = brake_light

  def step(self, percentage: float):
    acceleration.value -= percentage / 100 * 10 
    brake_light.value = "ON"


class BrakeLight(Measure):
  def __init__(self, init_value = "OFF"):
    super("BRAKE_LIGHT", init_value)
    
  def __repr__(self): 
    return self.value
    

class Temperature(Measure):
  def __init__(self, init_value = 29):
    super("TEMP", init_value)
    
  def __repr__(self):
    return self.value
  
  
class MonitorSystem:
  def __init__(self)
    self.measures = []
    
  def add_parameter(self, measure: Measure):
    self.measures.append(measure)
    
  def log_event():
    for measure in measures:
      print(f"{measure.key}: {measure.value}")
    print()
  
  
# def log_event(acceleration: Acceleration, brake_light: BrakeLight, temperature: Temperature):
#   print(f"ACC: {acceleration}, BRAKE_LIGHT: {brake_light}, TEMP: {temperature}")

def main():
  acceleration = Acceleration()
  brake_light = BrakeLight()
  
  gas_pedal = GasPedal(acceleration)
  brake_pedal = BrakePedal(acceleration, brake_light)
  
  monitor_system = MonitorSystem()
  monitor_system.add_parameter(acceleration)
  monitor_system.add_parameter(brake_light)
  
  # 1 ms
  gas_pedal.step(10) # Gas 10%
  monitor_system.log_event()
  
  # 2 ms
  gas_pedal.step(30) # Gas 30%
  monitor_system.log_event()
  
  # 3 ms 
  gas_pedal.step(15)
  brake_pedal.step(50)
  monitor_system.log_event()
  
  # 4 ms 
  gas_pedal.step(0)
  brake_pedal.step(100)
  monitor_system.log_event()
  
  # 5 ms
  temperature = Temperature()
  monitor_system.add_parameter(temperature)
  brake_pedal.step(100)
  monitor_system.log_event()
  
  
  
