from model.model import Model

mdl = Model()
mdl.buildGraph(1500)
com = mdl.getConnessa(226)
print(com[0])