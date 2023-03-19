class reward():
    """The reward function class generates an instantaneous reward given a 
    particular state based on the following parameters
    
    1. Legality of state:
        - x for x overlaps
    
    2. Conservation of water:
        - for each water used
        
    3. Diversity of garden:
        + x for x > 3 plant species
        0 for 3 species
        - x for x < 3 plant species
    
    4. Density of garden
        +% for %density > 75
        -% for %density < 75
    """