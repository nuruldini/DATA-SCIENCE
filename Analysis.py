import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Streamlit title
st.title('Data Visualization and Analysis')

# Load the dataset from the CSV file
file_path_dist = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/population_district.csv'
file_path_income = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/hh_income_district.csv'
file_path_filtered = 'https://raw.githubusercontent.com/tirasyaz/ayam-super/refs/heads/main/filtered_pricecatcher_data.csv'

df_dist = pd.read_csv(file_path_dist)
df_income = pd.read_csv(file_path_income)
data = pd.read_csv(file_path_filtered)

# Filter data based on districts
st.header('Filter District Data')
district_names = ['Jelebu', 'Kuala Pilah', 'Jempol', 'Port Dickson', 'Rembau', 'Tampin', 'Seremban']
df_newdist = df_dist[df_dist['district'].isin(district_names)]

df_newincome = df_income[df_income['district'].isin(district_names)]

# Display filtered data
st.subheader('Filtered Population Data')
st.write(df_newdist)

st.subheader('Filtered Income Data')
st.write(df_newincome)

# Bar chart: Population by district
st.header('Total Population by District')
population_by_district = df_newdist.groupby('district')['population'].sum()
st.bar_chart(population_by_district)

# Bar chart: Average income by district
st.header('Average Income by District')
income_summary = df_newincome.groupby('district')['income_median'].mean()
st.bar_chart(income_summary)

# Box plot: Income distribution
st.header('Income Distribution Across Districts')
fig_box, ax_box = plt.subplots()
sns.boxplot(data=df_newincome, x='income_median', ax=ax_box)
ax_box.set_title('Income Distribution Across Districts')
ax_box.set_xlabel('Median Income')
st.pyplot(fig_box)

# Heatmap: Correlation Matrix
st.header('Correlation Matrix')
numerical_df = df_newincome.select_dtypes(include=['number'])
correlation_matrix = numerical_df.corr()
fig_heatmap, ax_heatmap = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax_heatmap)
ax_heatmap.set_title('Correlation Matrix')
st.pyplot(fig_heatmap)




# Heatmap: Average price by premise and month
st.header('Average Price Heatmap by Premise and Month')
data = data.reset_index()
data['month'] = data['date'].dt.to_period('M')
monthly_avg_price = data.groupby(['premise', 'month'])['price'].mean().reset_index()
heatmap_data = monthly_avg_price.pivot_table(index='premise', columns='month', values='price')

fig_heatmap2, ax_heatmap2 = plt.subplots(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt=".2f", ax=ax_heatmap2)
ax_heatmap2.set_title('Average Price Heatmap by Premise and Month')
st.pyplot(fig_heatmap2)
