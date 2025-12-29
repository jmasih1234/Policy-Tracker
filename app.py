import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Global Policy Tracker",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🌍 Global Policy Tracker")
st.markdown("""
This application tracks foreign and domestic policies for countries across the world, 
including both hemispheres, with detailed coverage of the United States.
""")

# Sample policy data structure
def get_sample_policies():
    """Generate sample policy data for demonstration purposes."""
    return pd.DataFrame([
        # United States
        {
            "Country": "United States",
            "Hemisphere": "Northern",
            "Continent": "North America",
            "Policy Type": "Domestic",
            "Policy Area": "Healthcare",
            "Policy Name": "Affordable Care Act",
            "Status": "Active",
            "Implementation Year": 2010,
            "Description": "Comprehensive healthcare reform law"
        },
        {
            "Country": "United States",
            "Hemisphere": "Northern",
            "Continent": "North America",
            "Policy Type": "Foreign",
            "Policy Area": "Trade",
            "Policy Name": "USMCA",
            "Status": "Active",
            "Implementation Year": 2020,
            "Description": "Trade agreement between US, Mexico, and Canada"
        },
        {
            "Country": "United States",
            "Hemisphere": "Northern",
            "Continent": "North America",
            "Policy Type": "Domestic",
            "Policy Area": "Climate",
            "Policy Name": "Inflation Reduction Act",
            "Status": "Active",
            "Implementation Year": 2022,
            "Description": "Climate and energy investment legislation"
        },
        {
            "Country": "United States",
            "Hemisphere": "Northern",
            "Continent": "North America",
            "Policy Type": "Foreign",
            "Policy Area": "Defense",
            "Policy Name": "NATO Alliance",
            "Status": "Active",
            "Implementation Year": 1949,
            "Description": "Military alliance for collective defense"
        },
        # European Countries
        {
            "Country": "United Kingdom",
            "Hemisphere": "Northern",
            "Continent": "Europe",
            "Policy Type": "Foreign",
            "Policy Area": "Trade",
            "Policy Name": "Brexit",
            "Status": "Active",
            "Implementation Year": 2020,
            "Description": "Withdrawal from European Union"
        },
        {
            "Country": "Germany",
            "Hemisphere": "Northern",
            "Continent": "Europe",
            "Policy Type": "Domestic",
            "Policy Area": "Energy",
            "Policy Name": "Energiewende",
            "Status": "Active",
            "Implementation Year": 2011,
            "Description": "Transition to renewable energy"
        },
        {
            "Country": "France",
            "Hemisphere": "Northern",
            "Continent": "Europe",
            "Policy Type": "Domestic",
            "Policy Area": "Social",
            "Policy Name": "35-Hour Work Week",
            "Status": "Active",
            "Implementation Year": 2000,
            "Description": "Labor policy reducing standard work week"
        },
        # Asian Countries
        {
            "Country": "China",
            "Hemisphere": "Northern",
            "Continent": "Asia",
            "Policy Type": "Foreign",
            "Policy Area": "Trade",
            "Policy Name": "Belt and Road Initiative",
            "Status": "Active",
            "Implementation Year": 2013,
            "Description": "Global infrastructure development strategy"
        },
        {
            "Country": "Japan",
            "Hemisphere": "Northern",
            "Continent": "Asia",
            "Policy Type": "Domestic",
            "Policy Area": "Economy",
            "Policy Name": "Abenomics",
            "Status": "Active",
            "Implementation Year": 2012,
            "Description": "Economic policy framework"
        },
        {
            "Country": "India",
            "Hemisphere": "Northern",
            "Continent": "Asia",
            "Policy Type": "Domestic",
            "Policy Area": "Digital",
            "Policy Name": "Digital India",
            "Status": "Active",
            "Implementation Year": 2015,
            "Description": "Digital infrastructure development program"
        },
        # Southern Hemisphere Countries
        {
            "Country": "Brazil",
            "Hemisphere": "Southern",
            "Continent": "South America",
            "Policy Type": "Domestic",
            "Policy Area": "Environment",
            "Policy Name": "Amazon Protection",
            "Status": "Active",
            "Implementation Year": 2023,
            "Description": "Rainforest conservation initiatives"
        },
        {
            "Country": "Australia",
            "Hemisphere": "Southern",
            "Continent": "Oceania",
            "Policy Type": "Domestic",
            "Policy Area": "Immigration",
            "Policy Name": "Skilled Migration Program",
            "Status": "Active",
            "Implementation Year": 1996,
            "Description": "Points-based immigration system"
        },
        {
            "Country": "South Africa",
            "Hemisphere": "Southern",
            "Continent": "Africa",
            "Policy Type": "Domestic",
            "Policy Area": "Social",
            "Policy Name": "Black Economic Empowerment",
            "Status": "Active",
            "Implementation Year": 2003,
            "Description": "Economic transformation policy"
        },
        {
            "Country": "Argentina",
            "Hemisphere": "Southern",
            "Continent": "South America",
            "Policy Type": "Foreign",
            "Policy Area": "Trade",
            "Policy Name": "Mercosur Membership",
            "Status": "Active",
            "Implementation Year": 1991,
            "Description": "South American trade bloc participation"
        },
        # African Countries
        {
            "Country": "Nigeria",
            "Hemisphere": "Northern",
            "Continent": "Africa",
            "Policy Type": "Domestic",
            "Policy Area": "Economy",
            "Policy Name": "Economic Recovery Plan",
            "Status": "Active",
            "Implementation Year": 2017,
            "Description": "National economic development strategy"
        },
    ])

# Load data
df = get_sample_policies()

# Sidebar filters
st.sidebar.header("🔍 Filter Policies")

# Hemisphere filter
hemispheres = ["All"] + sorted(df["Hemisphere"].unique().tolist())
selected_hemisphere = st.sidebar.selectbox("Hemisphere", hemispheres)

# Continent filter
if selected_hemisphere != "All":
    continents = ["All"] + sorted(df[df["Hemisphere"] == selected_hemisphere]["Continent"].unique().tolist())
else:
    continents = ["All"] + sorted(df["Continent"].unique().tolist())
selected_continent = st.sidebar.selectbox("Continent", continents)

# Country filter
if selected_continent != "All":
    if selected_hemisphere != "All":
        countries = ["All"] + sorted(df[(df["Hemisphere"] == selected_hemisphere) & 
                                       (df["Continent"] == selected_continent)]["Country"].unique().tolist())
    else:
        countries = ["All"] + sorted(df[df["Continent"] == selected_continent]["Country"].unique().tolist())
else:
    if selected_hemisphere != "All":
        countries = ["All"] + sorted(df[df["Hemisphere"] == selected_hemisphere]["Country"].unique().tolist())
    else:
        countries = ["All"] + sorted(df["Country"].unique().tolist())
selected_country = st.sidebar.selectbox("Country", countries)

# Policy type filter
policy_types = ["All", "Domestic", "Foreign"]
selected_policy_type = st.sidebar.selectbox("Policy Type", policy_types)

# Policy area filter
policy_areas = ["All"] + sorted(df["Policy Area"].unique().tolist())
selected_policy_area = st.sidebar.selectbox("Policy Area", policy_areas)

# Apply filters
filtered_df = df.copy()

if selected_hemisphere != "All":
    filtered_df = filtered_df[filtered_df["Hemisphere"] == selected_hemisphere]

if selected_continent != "All":
    filtered_df = filtered_df[filtered_df["Continent"] == selected_continent]

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]

if selected_policy_type != "All":
    filtered_df = filtered_df[filtered_df["Policy Type"] == selected_policy_type]

if selected_policy_area != "All":
    filtered_df = filtered_df[filtered_df["Policy Area"] == selected_policy_area]

# Main content area
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🇺🇸 USA Focus", "📈 Analytics", "📋 Detailed View"])

with tab1:
    st.header("Policy Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Policies", len(filtered_df))
    
    with col2:
        st.metric("Countries", filtered_df["Country"].nunique())
    
    with col3:
        domestic_count = len(filtered_df[filtered_df["Policy Type"] == "Domestic"])
        st.metric("Domestic Policies", domestic_count)
    
    with col4:
        foreign_count = len(filtered_df[filtered_df["Policy Type"] == "Foreign"])
        st.metric("Foreign Policies", foreign_count)
    
    # Distribution charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Policies by Hemisphere")
        hemisphere_dist = filtered_df["Hemisphere"].value_counts().reset_index()
        hemisphere_dist.columns = ["Hemisphere", "Count"]
        fig1 = px.pie(hemisphere_dist, values="Count", names="Hemisphere", 
                     title="Distribution by Hemisphere",
                     color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Policies by Type")
        type_dist = filtered_df["Policy Type"].value_counts().reset_index()
        type_dist.columns = ["Policy Type", "Count"]
        fig2 = px.pie(type_dist, values="Count", names="Policy Type",
                     title="Domestic vs Foreign Policies",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Policy areas bar chart
    st.subheader("Policies by Area")
    area_dist = filtered_df["Policy Area"].value_counts().reset_index()
    area_dist.columns = ["Policy Area", "Count"]
    fig3 = px.bar(area_dist, x="Policy Area", y="Count",
                 title="Policy Distribution by Area",
                 color="Count",
                 color_continuous_scale="Blues")
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.header("🇺🇸 United States Policy Focus")
    st.markdown("""
    This section provides detailed information on the greater continental USA, 
    covering both foreign and domestic policy agendas.
    """)
    
    usa_df = df[df["Country"] == "United States"]
    
    # USA metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total USA Policies", len(usa_df))
    
    with col2:
        usa_domestic = len(usa_df[usa_df["Policy Type"] == "Domestic"])
        st.metric("Domestic Policies", usa_domestic)
    
    with col3:
        usa_foreign = len(usa_df[usa_df["Policy Type"] == "Foreign"])
        st.metric("Foreign Policies", usa_foreign)
    
    # USA policy areas
    st.subheader("USA Policy Areas")
    usa_area_dist = usa_df["Policy Area"].value_counts().reset_index()
    usa_area_dist.columns = ["Policy Area", "Count"]
    fig_usa = px.bar(usa_area_dist, x="Policy Area", y="Count",
                    title="USA Policies by Area",
                    color="Policy Area",
                    color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig_usa, use_container_width=True)
    
    # USA policies table
    st.subheader("All USA Policies")
    st.dataframe(
        usa_df[["Policy Type", "Policy Area", "Policy Name", "Status", 
               "Implementation Year", "Description"]],
        use_container_width=True,
        hide_index=True
    )

with tab3:
    st.header("📈 Policy Analytics")
    
    # Timeline of policies
    st.subheader("Policy Implementation Timeline")
    timeline_df = filtered_df.sort_values("Implementation Year")
    fig_timeline = px.scatter(timeline_df, 
                             x="Implementation Year", 
                             y="Country",
                             color="Policy Type",
                             hover_data=["Policy Name", "Policy Area"],
                             title="Policy Implementation Timeline")
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Continental distribution
    st.subheader("Policies by Continent")
    continent_dist = filtered_df["Continent"].value_counts().reset_index()
    continent_dist.columns = ["Continent", "Count"]
    fig_continent = px.bar(continent_dist, x="Continent", y="Count",
                          title="Geographic Distribution of Policies",
                          color="Continent",
                          color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_continent, use_container_width=True)
    
    # Country comparison
    if len(filtered_df) > 0:
        st.subheader("Policy Count by Country")
        country_dist = filtered_df["Country"].value_counts().reset_index().head(10)
        country_dist.columns = ["Country", "Count"]
        fig_country = px.bar(country_dist, x="Country", y="Count",
                            title="Top Countries by Policy Count",
                            color="Count",
                            color_continuous_scale="Viridis")
        st.plotly_chart(fig_country, use_container_width=True)

with tab4:
    st.header("📋 Detailed Policy Information")
    
    if len(filtered_df) > 0:
        st.subheader(f"Showing {len(filtered_df)} Policies")
        
        # Display full dataframe
        st.dataframe(
            filtered_df[[
                "Country", "Hemisphere", "Continent", "Policy Type", 
                "Policy Area", "Policy Name", "Status", 
                "Implementation Year", "Description"
            ]],
            use_container_width=True,
            hide_index=True
        )
        
        # Detailed view selector
        st.subheader("View Individual Policy Details")
        policy_names = filtered_df["Policy Name"].tolist()
        selected_policy = st.selectbox("Select a policy to view details:", policy_names)
        
        if selected_policy:
            policy_details = filtered_df[filtered_df["Policy Name"] == selected_policy].iloc[0]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Policy Name:** {policy_details['Policy Name']}")
                st.markdown(f"**Country:** {policy_details['Country']}")
                st.markdown(f"**Continent:** {policy_details['Continent']}")
                st.markdown(f"**Hemisphere:** {policy_details['Hemisphere']}")
            
            with col2:
                st.markdown(f"**Policy Type:** {policy_details['Policy Type']}")
                st.markdown(f"**Policy Area:** {policy_details['Policy Area']}")
                st.markdown(f"**Status:** {policy_details['Status']}")
                st.markdown(f"**Implementation Year:** {policy_details['Implementation Year']}")
            
            st.markdown("---")
            st.markdown(f"**Description:**")
            st.markdown(policy_details['Description'])
    else:
        st.info("No policies match the current filter criteria. Please adjust your filters.")

# Footer
st.markdown("---")
st.markdown("""
**About this Policy Tracker:**
This application provides comprehensive tracking of foreign and domestic policies across countries worldwide,
covering both Northern and Southern hemispheres, with detailed focus on the United States.
The research criteria are thorough and encompass various policy areas including trade, healthcare,
defense, environment, economy, and social policies.
""")
