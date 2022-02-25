"""Create plot of L^2 norm between persistence curves of conformation between an
initial and terminal conformation."""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt

from conftopo.common.compute_persist_curves import compute_persist_curves
from conftopo.data.get_proteins import get_proteins
from conftopo.data.chimerax import chimerax


def main():
    st.title('ConfTopo')
    st.text('Topological changes across protein conformational changes')

    # Sidebar options
    mol_1 = st.sidebar.text_input('Molecule 1', value='1cm1')
    mol_2 = st.sidebar.text_input('Molecule 2', value='1cfd')
    n_subsamp = st.sidebar.number_input('Number of points to subsample', min_value=1, value=400)

    # TODO: This isn't set up yet
    homology = st.sidebar.multiselect(
        'Homology groups',
        ['H_0', 'H_1', 'H_2'],
        ['H_0', 'H_1', 'H_2'])

    # mol_1 = '1cm1'
    # mol_2 = '1cfd'

    # Temporarily commenting out
    get_proteins(mol_1, mol_2)
    chimerax()
    lcs = compute_persist_curves('conftopo/data/tmp/morph/morph.pdb', verbose=1, n_perm=n_subsamp)

    # Set plotting range to H_0, H_1, and H_2
    homology = range(000, 300)

    # Compute L^2 norm
    dist = []
    for k in range(len(lcs)):
        dist.append(np.linalg.norm(lcs[0, homology] - lcs[k, homology]))

    # Plot
    # plt.figure()
    # plt.subplots(figsize=(12, 6))
    # plt.title(
    #     "$L^2$ norm between persistence curves for conformations "+mol_1+" to "+mol_2)
    # plt.xlabel("Conformation")
    # plt.ylabel("$L^2$ norm")
    # plt.plot(dist)
    # plt.savefig('conftopo/data/norm_plot_'+mol_1+"_"+mol_2+'.png')

    data = pd.DataFrame({'value': dist})
    line_chart = alt.Chart(data.reset_index()).mark_line().encode(
        x='index',
        y='value'
    ).properties(
        title='$L^2$ norm between persistence curves for conformations '+mol_1+' to '+mol_2
    )

    st.altair_chart(line_chart, use_container_width=True)
    # st.line_chart(dist)


if __name__ == '__main__':
    main()
