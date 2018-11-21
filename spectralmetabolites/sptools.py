# Package for computing the eigenvalue spectral decomposition of
# metabolites as graphs.
#
# Illinois Informatics and National Center for Supercomputing Applications
# University of Illinois at Urbana-Champaign
#
# Santiago Nunez-Corrales (nunezco2@illinois.edu)
# Eric Jakobsson (jake@illinois.edu)

import matplotlib.pyplot as plt
import spectralmetabolites.moltograph as mtg
from numpy.linalg import eigvals
import scipy.sparse.csr as scsr
import networkx as nx
import numpy as np


def obtain_graph(filename):
    converter = mtg.MolToGraph()
    converter.set(filename)
    converter.parse()
    g = converter.graph
    return g


def show_molecule(g, spectral=False, save=False):
    options = {
        'node_color': 'orange',
        'edge_color': 'black',
        'node_size': 250,
        'width': 2,
    }

    if spectral:
        nx.draw_spectral(g, **options)
    else:
        nx.draw_kamada_kawai(g, **options)
    plt.show()
    return


def obtain_eigvals(g):
    L: scsr.csr_matrix = nx.normalized_laplacian_matrix(g)
    ev = eigvals(L.toarray())
    return ev


def plot_eigvals(ev: np.ndarray):
    x = np.arange(1, ev.size + 1)
    plt.stem(x, ev, linefmt='g-', markerfmt=' ')
    plt.show()
