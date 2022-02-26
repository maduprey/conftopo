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
    st.set_page_config(layout='wide')
    st.title('ConfTopo')
    st.write('Topological changes across protein conformational changes')
    
    # about_expander = st.expander(label='About')
    # with about_expander:
    #     'TODO: Insert description here.'
    
    # Sidebar options
    mol_1 = st.sidebar.text_input('Molecule 1', value='1cm1')
    mol_2 = st.sidebar.text_input('Molecule 2', value='1cfd')
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
        st.header('Persistence Curves')
        
        # Add an empty slot first so that the slider can appear below the plot
        pc_plot = st.empty()
        
        idx = st.slider('Conformation index', 0, 60, 0)
        conf_pd = pd.DataFrame({'value': lcs[idx, homology]})
        line_chart = alt.Chart(conf_pd.reset_index()).mark_line().encode(
            x='index',
            y='value'
        ).properties(
            # title='Persistence curves for conformations'
        )
        pc_plot.altair_chart(line_chart, use_container_width=True)

    with col2:
        st.header('L2 Norm')
        
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
        

if __name__ == '__main__':
    main()
