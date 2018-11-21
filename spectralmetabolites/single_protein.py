# Package for computing the eigenvalue spectral decomposition of
# metabolites as graphs.
#
# Illinois Informatics and National Center for Supercomputing Applications
# University of Illinois at Urbana-Champaign
#
# Santiago Nunez-Corrales (nunezco2@illinois.edu)
# Eric Jakobsson (jake@illinois.edu)

import spectralmetabolites.sptools as spt
import biographs as bg
import argparse as ap


def main(target):
    process_single_prot(target)
    return


def process_single_prot(target, list=False, graph=False):
    protein = bg.Pmolecule(target)
    g = protein.network()
    if list:
        print(spt.obtain_eigvals(g))
    if graph:
        spt.plot_eigvals(spt.obtain_eigvals(g))
    return g


def return_single_prot_eigvals(g):
    return spt.obtain_eigvals(g)

def parse_args():
    parser = ap.ArgumentParser()
    parser.add_argument("proteinfile", help="PDB of protein to analyze as a graph")
    args = parser.parse_args()
    return str(args.proteinid)


if __name__ == '__main__':
    main(parse_args())
