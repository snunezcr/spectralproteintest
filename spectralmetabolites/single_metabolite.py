# Package for computing the eigenvalue spectral decomposition of
# metabolites as graphs.
#
# Illinois Informatics and National Center for Supercomputing Applications
# University of Illinois at Urbana-Champaign
#
# Santiago Nunez-Corrales (nunezco2@illinois.edu)
# Eric Jakobsson (jake@illinois.edu)

import spectralmetabolites.sptools as spt
import argparse as ap
import networkx as nx
import requests as rq


def main(target):
    g: nx.Graph = spt.obtain_graph(save_metabolite(target))
    print(spt.obtain_eigvals(g))
    spt.show_molecule(g, False)
    spt.plot_eigvals(spt.obtain_eigvals(g))
    save_metabolite(14)
    return


def parse_args():
    parser = ap.ArgumentParser()
    parser.add_argument("filenumber", help="Sequence numner of molecule to analyze as a graph")
    args = parser.parse_args()
    return int(args.filenumber)


def save_metabolite(seqval):
    if seqval > MOST_RECENT_METABOLITE():
        return "http://www.hmdb.ca/structures/metabolites/"

    else:
        baseurl = 'http://www.hmdb.ca/structures/metabolites/'
        filename = "HMDB{0:07d}.sdf".format(seqval)
        print(baseurl+filename)

        r = rq.get(baseurl+filename)

        with open(filename, 'wb') as f:
            f.write(r.content)

        return filename


def MOST_RECENT_METABOLITE():
    return 114100


if __name__ == '__main__':
    main(parse_args())
