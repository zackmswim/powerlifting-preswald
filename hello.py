## Program compares Deadlift vs Bodyweight of users. 
### Slider allows to filter out users by Deadlift weight.
#### Could not figure out why it wasn't updating in realtime. 


from preswald import text, plotly, connect, get_df, table, slider, query
import plotly.express as px

# Add Headings
text("# Welcome to the Gym")
text("🏋️ Powerlifting Performance Explorer")

# Connect to data
connect()

# Slider comes first - Deadlift VS Bodyweight
threshold = slider("Minimum Deadlift (kg)", min_val=0, max_val=400, default=150)

# Query and filter dataset
df = query("SELECT * FROM X_test LIMIT 1000", "X_test")
filtered_df = df[df["BestDeadliftKg"] >= threshold]

# Plot if filtered data exists
if not filtered_df.empty:
    fig = px.scatter(
        filtered_df,
        x='BodyweightKg',
        y='BestDeadliftKg',
        title=f'Bodyweight vs. Best Deadlift (≥ {threshold} kg)',
        labels={'BodyweightKg': 'Bodyweight (kg)', 'BestDeadliftKg': 'Best Deadlift (kg)'}
    )
    fig.update_traces(textposition='top center', marker=dict(size=10, color='purple'))
    fig.update_layout(template='plotly_white')
    
# Show filtered table and plot
    plotly(fig)
    table(filtered_df, title=f"Lifters (Deadlift ≥ {threshold} kg)")
else:
    text("❌ No lifters match the current filter.")
