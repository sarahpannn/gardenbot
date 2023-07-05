import matplotlib.pyplot as plt

class Plant:
    def __init__(self, species, location, plant_data, colors):
        self.species = species
        self.location = location
        self.water_freq = int(plant_data[species][0]['H_water_freq'])
        self.mature_radius = int(plant_data[species][0]['mature_radius'])
        self.days_to_mature = int(plant_data[species][0]['days_to_mature'])
        self.color = list(map(int, colors[species].split(" ")))
        self.alive = 1
        self.water = int(plant_data[species][0]['H_water_freq']) / 2 # water is measured in hours
        
    # time is measured in days
    def get_radius(self, dt):
        if dt < self.days_to_mature:
            return self.mature_radius * (dt / self.days_to_mature)
        if dt > self.days_to_mature + 5: # has a 5 day ripe period
            self.alive = 0
            dead_radius = 0.55 * self.mature_radius
            decay_factor = math.exp(-0.2 * (dt - self.days_to_mature - 5))
            decayed_radius = self.mature_radius * decay_factor
            return max(decayed_radius, dead_radius)
        return self.mature_radius
        
    def overlap_area(self, map):
        return 0

    def get_health(self):
        score = 1
        if (self.water < 0): score += 0.006 * (self.water / self.water_freq)
        if (self.overlap_area(map) > 0): score -= 0.5 * (self.overlap_area(map) / (self.mature_radius ** 2 * math.pi))
        if score < 0: self.alive = 0
        return score
        
    def get_color(self):
        if self.get_health() < 0:
            return [0, 0, 0]
        return (self.color[0] * self.get_health()/255, self.color[1] * self.get_health()/255, self.color[2] * self.get_health()/255)
    
    def get_circle_object(self, dt):
        radius = self.get_radius(dt)
        color = self.get_color()
        return plt.Circle(self.location, radius=radius, color=color)
        
    