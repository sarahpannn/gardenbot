import matplotlib.pyplot as plt

class GardenEnv(gym.Env):
    def __init__(self, box_size, crop_data, state):
        super().__init__()
        self.t = 0
        self.box_size = box_size
        self.crop_data = crop_data
        self.actions = ['plant', 'water', 'abstain', 'notify']
        self.state = state
        
        with open('../data/render_colors.json') as json_file:
            colors = json.load(json_file)
        self.colors = colors
        
    def step(self, action):
        self.t += 1
        """ Takes a step with given action and returns the resulting environment.
        Args:
            action: int 
            
        Returns:
            env: state_dict: {
                    plant1: [type, location, radius, water_status],
                    plant2: [type, location, radius, water_status],
                    ...
                }
        """
        return env
    
    def reset(self):
        self.t = 0
        return 0
    
    def human_render(self, state):
        fig, ax = plt.subplots()
        ax.set_xlim = self.box_size[0]
        ax.set_ylim = self.box_size[1]
        for plant in state.keys():
            ax.add_patch(plt.Circle(state[k][1], radius=state[k][2], color=self.colors[state[k][0]]))
        fig.savefig(f'env_at_time_{self.t}.png')
    
    def machine_render(self, state):
        return 0
    
    def render(self, mode='human'):
        if (mode=='human'):
            self.human_render(self.state)
        else:
            return self.machine_render(self.state)
            

            