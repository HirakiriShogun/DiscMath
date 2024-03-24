class Graph:
    def __init__(self, countries):
        self.vertices = 0
        self.edges = 0
        self.min_deg = 100
        self.max_deg = 0
        self.radius = 0
        self.diameter = 0
        self.components = 0
        self.cyclomatic_number = 0
        self.center = []
        self.chromatic_number = 0
        self.pendant_nodes = []
        self.countries = countries
    
    def CountVertices(self):
        self.vertices = len(self.countries.keys())
        
    def CountEdges(self):
        for country in self.countries.values():
            self.edges += len(country)
        self.edges //= 2
        
    def CountMinDeg(self):
        for country in self.countries.values():
            self.min_deg = min(len(country), self.min_deg)
        
    def CountMaxDeg(self):
        for country in self.countries.values():
            self.max_deg = max(len(country), self.max_deg)
            
    def GetMinDeg(self):
        return self.min_deg
    
    def GetMaxDeg(self):
        return self.max_deg
    
    def GetVertices(self):
        return self.vertices

    def GetEdges(self):
        return self.edges
    
    def SetRadius(self, radius):
        self.radius = radius
    
    def GetRadius(self):
        return self.radius
    
    def SetDiameter(self, diameter):
        self.diameter = diameter
    
    def GetDiameter(self):
        return self.diameter
    
    def SetCenter(self, center):
        self.center = center
    
    def GetCenter(self):
        return self.center
    
    def SetComponents(self, components):
        self.components = components
    
    def GetComponents(self):
        return self.components
    
    def SetCyclomaticNumber(self, cyclomatic_number):
        self.cyclomatic_number = cyclomatic_number
    
    def GetCyclomaticNumber(self):
        return self.cyclomatic_number
    
    def SetChromaticNumber(self, chromatic_number):
        self.chromatic_number = chromatic_number
    
    def GetChromaticNumber(self):
        return self.chromatic_number
    
    def SetPendantNodes(self, pendant_nodes):
        self.pendant_nodes = pendant_nodes
    
    def GetPendantNodes(self):
        return self.pendant_nodes