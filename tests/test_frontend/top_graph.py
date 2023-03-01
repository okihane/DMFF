from dmff.topology import top2graph, decompgraph, graph2top, top2rdmol
import openmm.app as app
import networkx as nx
import matplotlib.pyplot as plt 

app.Topology.loadBondDefinitions("tests/data/lig-top.xml")
pdb = app.PDBFile("tests/data/sum.pdb")
top = pdb.topology

graph = top2graph(top)
print(graph)

graphs = decompgraph(graph)
print(graph2top(graphs[0]))
print(graph2top(graphs[1]))
mol = top2rdmol(graph2top(graphs[1]), sanitize=False)
print(mol)

from rdkit.Chem import Draw

Draw.MolToFile(mol, "test.png")