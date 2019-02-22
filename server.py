# server.py
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import SCGrowthModel

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5, "Layer": 0}

    colours = ["red", "blue", "green", "yellow", "purple", "orange", "brown", "grey", "black", "cyan"]
    # portrayal["Color"] = colours[agent.clone]
    portrayal["Color"] = "red"
    print(portrayal)

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(SCGrowthModel, [grid], "Spatially-Constrained Growth", {"N": 3, "width": 10, "height": 10})