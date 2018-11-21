# Package for computing the eigenvalue spectral decomposition of
# metabolites as graphs.
#
# Illinois Informatics and National Center for Supercomputing Applications
# University of Illinois at Urbana-Champaign
#
# Santiago Nunez-Corrales (nunezco2@illinois.edu)
# Eric Jakobsson (jake@illinois.edu)


import networkx as nx
import spectralmetabolites.convertmol as cm


class MolToGraph:
    '''
    This class extracts the MOL matrix format and uses it to output and adjacency matrix.
    '''

    def __init__(self):
        self.__file = ""
        self.__data = None

    def set(self, molfile):
        self.__file = molfile

    def parse(self):
        if self.__file == "":
            return None

        self.__data = cm.parse_sdf_file(self.__file)

    @property
    def graph(self):
        if self.__data is None:
            return None

        g = nx.Graph()

        # Add all nodes
        for i in range(1, self.__data[0]["num_atoms"] + 1):
            g.add_node(i)

        # Add all edges
        for i in range(1, self.__data[0]["num_bonds"] + 1):
            g.add_edge(self.__data[0]["bonds"][i]["i"], self.__data[0]["bonds"][i]["j"])

        return g
