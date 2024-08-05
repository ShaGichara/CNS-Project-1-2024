from flask import Flask, request, render_template, url_for
import simpy
import random

app = Flask(__name__)

# Original function for ustomer behaviour
def customer(env, name, server):
    arrival_time = env.now
    with server.request() as request:
        yield request
        wait_time = env.now - arrival_time
        service_time = random.expovariate(1/10)
        yield env.timeout(service_time)
        
# Original function for setting up the simulation environment
def setup(env, num_servers):
    server = simpy.Resource(env, num_servers)
    for i in range(5):
        env.process(customer(env, f'Customer {i+1}', server))
    while True:
        yield env.timeout(random.expovariate(1/5))
        i += 1
        env.process(customer(env, f'Customer {i+1}', server))
        
# Home route
@app.route('/')
def index():
    return render_templates('index.html')
    
# Route to simulate the queue system
@app.route('/simulate')
def simulate():
    env = simpy.Environment()
    env.process(setup(env,1))
    env.run(until=100)
    return jsonify({"status": "Simulation complete"})
    
# Route to handle user interactions (if needed)
@app.route('/user_interactions')
def user_interactions():
    # Add your user interaction logic here
    pass
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3306, debug=True)
    
    
