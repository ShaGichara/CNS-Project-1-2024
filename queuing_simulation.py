import numpy as np

def run_simulation(arrival_rate, service_rate, simulation_time):
    np.random.seed(42)
    inter_arrival_times = np.random.exponential(1/arrival_rate, simulation_time)
    service_times = np.random.exponential(1/service_rate, simulation_time)
    
    arrival_times = np.cumsum(inter_arrival_times)
    departure_times = np.zeros(simulation_time)
    
    for i in range(simulation_time):
        if i == 0:
            departure_times[i] = arrival_times[i] + service_times[i]
        else:
            departure_times[i] = max(arrival_times[i], departure_times[i-1]) + service_times[i]
        
    wait_times = departure_times - arrival_times
    return wait_times

