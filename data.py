import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Simulate 5000 users
n_users = 5000
user_ids = np.arange(1, n_users + 1)

# Funnel conversion rates
conversion_rates = {
    'home_page': 1.0,            # 100% start here
    'product_view': 0.75,        # 75% go to view product
    'add_to_cart': 0.50,         # 50% add to cart
    'checkout': 0.25             # 25% complete checkout
}

# Create events for each user based on probabilities
events = []

for user_id in user_ids:
    if np.random.rand() < conversion_rates['home_page']:
        events.append((user_id, 'home_page'))
        if np.random.rand() < conversion_rates['product_view']:
            events.append((user_id, 'product_view'))
            if np.random.rand() < conversion_rates['add_to_cart']:
                events.append((user_id, 'add_to_cart'))
                if np.random.rand() < conversion_rates['checkout']:
                    events.append((user_id, 'checkout'))

# Create DataFrame
funnel_df = pd.DataFrame(events, columns=['user_id', 'event'])

#Additional Fields
funnel_df['timestamp'] = pd.to_datetime('2025-01-01') + pd.to_timedelta(np.random.randint(0, 30, len(funnel_df)), unit='d')
funnel_df['device_type'] = np.random.choice(['mobile', 'laptop', 'tablet'], size=len(funnel_df))
funnel_df['marketing'] = np.random.choice(['organic', 'paid_ads', 'referral', 'email'], size=len(funnel_df))



# Preview 
print(funnel_df.info)
print(funnel_df['event'].value_counts())


# Analyze
# Count unique users at each stage
funnel_counts = funnel_df['event'].value_counts()
print(funnel_counts)

# Convert to DataFrame and calculate drop-offs
funnel_summary = funnel_counts.to_frame(name='users')
funnel_summary['conversion_rate'] = funnel_summary['users'] / funnel_summary['users'].iloc[0]
funnel_summary['drop_off'] = funnel_summary['users'].diff(periods=-1).abs()

print(funnel_summary)

#Combined event/device Funnel Analysis 
device_counts = funnel_df[['event', 'device_type']].value_counts()

device_summary = device_counts.to_frame(name='device')
device_summary['conversion_rate'] = device_summary['device'] / device_summary['device'].iloc[0]
device_summary['drop_off'] = device_summary['device'].diff(periods=-1).abs()

print(device_summary)


#Combined event/marketing Funnel Analysis 
marketing_counts = funnel_df[['event', 'marketing']].value_counts()

marketing_summary = marketing_counts.to_frame(name='marketing')
marketing_summary['conversion_rate'] = marketing_summary['marketing'] / marketing_summary['marketing'].iloc[0]
marketing_summary['drop_off'] = marketing_summary['marketing'].diff(periods=-1).abs()

print(marketing_summary)

#Total Summary
total_counts = funnel_df[['event', 'device_type', 'marketing']].value_counts()

total_summary = total_counts.to_frame(name='total')
total_summary['conversion_rate'] = total_summary['total'] / total_summary['total'].iloc[0]
total_summary['drop_off'] = total_summary['total'].diff(periods=-1).abs()

print(total_summary)


#Visualize

#Bar Chart of User Drop off per Stage on website
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x=funnel_summary.index, y='users', data=funnel_summary.reset_index())
plt.title("Simulated Product Funnel - Drop-Off Analysis")
plt.ylabel("Number of Users")
plt.xlabel("Funnel Stage")
plt.show()

#Funnel Chart
import plotly.express as px
import plotly.io as pio  

fig = px.funnel(
    funnel_summary.reset_index(),
    x = funnel_summary.index,
    y = 'users',
    title = 'Simulated Product Funnel'
)

pio.renderers.default = 'browser' 

fig.show()

#Outputs 
funnel_summary.to_csv(r'C:\Users\MehakGanju\Documents\Repositories\Personal\Product Funnel Analysis\output files\funnel_by_event.csv')

device_summary.to_csv(r'C:\Users\MehakGanju\Documents\Repositories\Personal\Product Funnel Analysis\output files\funnel_by_device.csv')

marketing_summary.to_csv(r'C:\Users\MehakGanju\Documents\Repositories\Personal\Product Funnel Analysis\output files\funnel_by_marketing.csv')
