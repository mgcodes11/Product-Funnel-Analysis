🛍️ Product Funnel Analysis (Base Analysis in Python)
📌 Overview

This project simulates and analyzes a product funnel to understand how users progress through different stages of a website. Funnel analysis helps identify conversion rates and drop-off points, providing insights into where users disengage and where improvements can be made.

The first part of this project focuses on performing the core funnel analysis in Python, including data wrangling, conversion/drop-off calculations, and initial visualizations.

🎯 Objectives

Create a synthetic dataset simulating user behavior across funnel stages.

Calculate conversion rates and drop-off rates between stages.

Visualize the funnel using Python (Matplotlib/Seaborn/Plotly).

Lay the groundwork for interactive dashboards (Tableau/Power BI).

📂 Dataset

The simulated dataset contains user activity across four key funnel stages:

Column	Description
user_id	Unique identifier for each user
event	Funnel stage event (e.g., visit_homepage, sign_up, complete_profile, make_purchase)
timestamp	Event timestamp (datetime)
🔍 Analysis Performed

Stage Counts

Counted the number of unique users at each funnel stage.

Conversion Rate

% of users moving from one stage to the next.

Formula:

Conversion Rate
=
Users at Stage N+1
Users at Stage N
×
100
Conversion Rate=
Users at Stage N
Users at Stage N+1
	​

×100

Drop-Off Rate

% of users lost between two stages.

Formula:

Drop-Off Rate
=
100
−
Conversion Rate
Drop-Off Rate=100−Conversion Rate

📊 Visualizations

Bar Chart (Users by Stage): Shows the number of users remaining at each funnel stage.

Funnel Chart (Plotly): Visualizes user drop-off in a funnel-shaped chart for a more intuitive view.

Example (simulated numbers):

Funnel Stage	Users	Conversion (%)	Drop-Off (%)
Visit Homepage	1000	–	–
Sign Up	600	60%	40%
Complete Profile	400	67%	33%
Make Purchase	200	50%	50%
⚙️ Tech Stack

Python (Pandas, NumPy) – data processing & analysis

Matplotlib / Seaborn – base visualizations

Plotly – interactive funnel chart
