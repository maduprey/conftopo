import os
from re import A
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import py3Dmol
import streamlit as st
import altair as alt

from conftopo.common.compute_persist_curves import compute_persist_curves
from conftopo.data.get_proteins import get_proteins
from conftopo.data.chimerax import chimerax


def main():
    @st.cache(suppress_st_warning=True, show_spinner=False)
    def compute_all_pcs(mol_1, mol_2, n_subsamp):
        """
        Primary function to compute all persistence curves.
        """

        get_proteins(mol_1, mol_2)
        chimerax()
        lcs = compute_persist_curves(
            'conftopo/data/tmp/morph/morph.pdb', verbose=1, n_perm=n_subsamp)
        return lcs

    # Streamlit app
    st.set_page_config(page_title='ConfTopo',
                       page_icon=':doughnut:', layout='wide')
    st.sidebar.title(':doughnut: ConfTopo')
    st.sidebar.write(
        'Topological changes across protein conformational changes')
    st.sidebar.write('##')
    about_expander = st.sidebar.expander(label='Examples')
    with about_expander:
        st.write(''' 
                    Try conformational changes:\n
                    * Calmodulin: `1cll` &rarr; `1ctr` \n
                    * AdK: `1ake` &rarr; `4ake` \n
                    * GroEL: `1ss8` &rarr; `1sx4`
                ''')

    # Sidebar options
    mol_1 = st.sidebar.text_input(
        'Molecule 1', value='1cm1', help='Initial conformation PDB code')
    mol_2 = st.sidebar.text_input(
        'Molecule 2', value='1cfd', help='Terminal conformation PDB code')
    n_subsamp = st.sidebar.number_input(
        'Number of atoms to subsample', min_value=0, value=400)
    homology_input = st.sidebar.multiselect(
        'Homology groups',
        ['H_0', 'H_1', 'H_2'],
        ['H_0', 'H_1', 'H_2'])

    # Primary function
    lcs = compute_all_pcs(mol_1, mol_2, n_subsamp)

    # Set plotting range to H_0, H_1, and H_2
    homology = []
    if 'H_0' in homology_input:
        homology.extend(list(range(0, 100)))
    if 'H_1' in homology_input:
        homology.extend(list(range(100, 200)))
    if 'H_2' in homology_input:
        homology.extend(list(range(200, 300)))

    # Set up two-column layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Persistence Curves')
        # Add an empty slot first so that the slider can appear below the plot
        pc_plot = st.empty()
        st.caption(
            """
            Concatenated normalized life curves for H_0, H_1, and_H_2, respectively.
            """
        )

        idx = st.slider('Conformation index', 0, 60, 0,
                        help='**Initial conformation**: `index=0`; **Terminal conformation**: `index=60`')
        conf_pd = pd.DataFrame({'value': lcs[idx, homology]})
        line_chart = alt.Chart(conf_pd.reset_index()).mark_line().encode(
            x='index',
            y='value'
        ).properties(
            # title='Persistence curves for conformations'
        )
        pc_plot.altair_chart(line_chart, use_container_width=True)

    with col2:
        st.subheader('L2 Norm')
        # Compute L^2 norm
        dist = []
        for k in range(len(lcs)):
            dist.append(np.linalg.norm(lcs[0, homology] - lcs[k, homology]))

        dist_pd = pd.DataFrame({'value': dist})
        line_chart = alt.Chart(dist_pd.reset_index()).mark_line().encode(
            x='index',
            y='value'
        ).properties(
            # title='L^2 norm between persistence curves for conformations '+mol_1+' to '+mol_2
        )
        st.altair_chart(line_chart, use_container_width=True)
        st.caption(
            """
            L2 norm between the initial molecule's persistence curves and 
            intermediate conformations persistence curves.
            """
        )

    st.subheader('Conformation')
    # Adding py3Dmol visualization of the selected conformation
    viewer = py3Dmol.view(width=400, height=400)
    viewer.setBackgroundColor(0x0f1116)
    viewer.setCameraParameters({'fov':45, 'z':150})

    viewer.addModelsAsFrames(
        open('conftopo/data/tmp/morph/morph.pdb', 'r').read(), 'pdb')
    viewer.setStyle({'cartoon': {'arrows':'true'}})
    viewer.setFrame(idx)
    viewer.update()
    viewer.zoomTo()
    viewer.render()

    t = viewer.js()
    f = open('conftopo/data/tmp/py3Dmol.html', 'w')
    f.write(t.startjs)
    f.write(t.endjs)
    f.close()

    st.components.v1.html(
        open('conftopo/data/tmp/py3Dmol.html', 'r').read(), width=400, height=400)


if __name__ == '__main__':
    main()
