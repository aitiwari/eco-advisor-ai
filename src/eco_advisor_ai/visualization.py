 
import pandas as pd
import plotly.express as px
from typing import Tuple
from .config import AppConfig

class EmissionVisualizer:
    """Handles data visualization for emission data."""
    
    def __init__(self):
        self.config = AppConfig()

    def create_charts(self, emissions_data: dict) -> Tuple[px.pie, px.bar]:
        """Create pie and bar charts from emission data."""
        df = self._prepare_data(emissions_data)
        return self._create_pie_chart(df), self._create_bar_chart(df)

    def _prepare_data(self, emissions_data: dict) -> pd.DataFrame:
        """Convert emissions data to DataFrame."""
        return pd.DataFrame({
            "Category": list(emissions_data.keys()),
            "Emissions": list(emissions_data.values())
        }).sort_values("Emissions", ascending=False)

    def _create_pie_chart(self, df: pd.DataFrame) -> px.pie:
        """Generate pie chart visualization."""
        return px.pie(
            df,
            values="Emissions",
            names="Category",
            title="Carbon Footprint Breakdown",
            color_discrete_sequence=px.colors.sequential.Emrld
        )

    def _create_bar_chart(self, df: pd.DataFrame) -> px.bar:
        """Generate bar chart visualization."""
        return px.bar(
            df,
            x="Category",
            y="Emissions",
            title="Emissions by Category (kg CO2)",
            color="Category",
            color_discrete_sequence=px.colors.sequential.Emrld
        )