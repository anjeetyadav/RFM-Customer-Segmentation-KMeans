import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("data/olist_orders_dataset.csv")

# Convert date
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Create snapshot date
snapshot_date = df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

# RFM
rfm = df.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,
    'customer_id': 'count',
    'payment_value': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Scaling
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Save output
rfm.to_csv("rfm_kmeans_output.csv", index=False)