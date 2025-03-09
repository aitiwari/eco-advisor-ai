import streamlit as st
from .config import AppConfig
from .calculations import CarbonCalculator
from .visualization import EmissionVisualizer
from .groq_client import GroqClient

class EcoAdvisorApp:
    """Main application class for EcoAdvisor AI."""
    
    def __init__(self):
        self.config = AppConfig()
        self.calculator = CarbonCalculator()
        self.visualizer = EmissionVisualizer()

    def setup_page(self):
        """Configure Streamlit page settings."""
        st.set_page_config(
            page_title=self.config.page_title,
            page_icon=self.config.page_icon,
            layout=self.config.layout
        )

    def run(self):
        """Main application runner."""
        self.setup_page()
        st.title(self.config.page_title)
        
        tab1, tab2, tab3 = st.tabs(["Calculator", "AI Advisor", "About"])
        with tab1:
            self._render_calculator()
        with tab2:
            self._render_advisor()
        with tab3:
            self._render_about()

    def _render_calculator(self):
        """Render calculator tab components."""
        st.header("Carbon Footprint Calculator")
        user_inputs = self._get_user_inputs()
        emissions = self.calculator.calculate_emissions(user_inputs)
        self._display_results(emissions)
        st.session_state.user_data = {**user_inputs, **emissions}

    def _get_user_inputs(self):
        """Collect user inputs through form."""
        col1, col2 = st.columns(2)
        with col1:
            inputs = {
                "electricity": st.number_input("Monthly electricity (kWh)", min_value=0.0),
                "gas": st.number_input("Monthly gas (m³)", min_value=0.0),
                "car_km": st.number_input("Weekly car distance (km)", min_value=0.0),
            }
        with col2:
            inputs.update({
                "flight_hours": st.number_input("Annual flight hours", min_value=0.0),
                "diet_type": st.selectbox("Diet type", ["Meat-based", "Vegetarian"]),
                "bus_km": st.number_input("Weekly public transport (km)", min_value=0.0)
            })
        return inputs

    def _display_results(self, emissions: dict):
        """Display calculation results and visualizations."""
        st.subheader("Annual Carbon Footprint")
        self._show_metrics(emissions)
        self._show_visualizations(emissions)

    def _show_metrics(self, emissions: dict):
        """Display metrics and progress bars."""
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("Total CO2 Emissions", f"{emissions['Total']:,.2f} kg")
        
        with col2:
            for category in self.config.progress_bar_categories:
                value = emissions.get(category, 0)
                st.progress(
                    value / emissions["Total"], 
                    text=f"{category}: {value:,.1f} kg"
                )

    def _show_visualizations(self, emissions: dict):
        """Display interactive charts."""
        filtered_data = {k: v for k, v in emissions.items() if k != "Total"}
        pie_chart, bar_chart = self.visualizer.create_charts(filtered_data)
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(pie_chart, use_container_width=True)
        with col2:
            st.plotly_chart(bar_chart, use_container_width=True)

    def _render_advisor(self):
        """Render AI advisor tab components."""
        st.header("AI Sustainability Advisor")
        
        if "user_data" not in st.session_state:
            st.warning("Please calculate your footprint first")
            return
        
        api_key = st.text_input("Groq API Key:", type="password")
        if st.button("Get Recommendations") and api_key:
            self._handle_recommendations(api_key)

    def _handle_recommendations(self, api_key: str):
        """Fetch and display AI recommendations."""
        try:
            client = GroqClient(api_key)
            recommendations = client.get_recommendations(st.session_state.user_data)
            st.subheader("Personalized Recommendations")
            st.write(recommendations)
        except Exception as e:
            st.error(f"Error: {str(e)}")

    def _render_about(self):
        """Render about tab content."""
        st.header("About EcoAdvisor AI")
        st.markdown("""
        ## Sustainable Living Made Easy
        **Features:**
        - 🧮 Carbon footprint calculator
        - 🤖 AI-powered recommendations
        - 📊 Interactive visualizations
        - 📱 Mobile-friendly interface
        **Technology Stack:**
        - Streamlit
        - Groq API
        - Plotly
        - Python
        [GitHub Repository](https://github.com/yourusername/eco-advisor-ai)
        """)

