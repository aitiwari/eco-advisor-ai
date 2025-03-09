 
import plotly.graph_objects as go
import pandas as pd

class ImpactVisualizer:
    def create_timeline(self, roadmap_data):
        df = pd.DataFrame(roadmap_data)
        fig = px.timeline(df, 
                         x_start="Start", 
                         x_end="End", 
                         y="Phase",
                         color="Category",
                         title="Sustainability Roadmap")
        return fig
    
    def comparison_radar(self, current, simulated):
        categories = list(current.keys())
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=list(current.values()),
            theta=categories,
            fill='toself',
            name='Current'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=list(simulated.values()),
            theta=categories,
            fill='toself',
            name='Simulated'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            showlegend=True
        )
        return fig