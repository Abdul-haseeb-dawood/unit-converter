import streamlit as st

class LengthConverter:
    def __init__(self):
        # Units organized by categories
        self.unit_categories = {
            "Metric": {
                "Kilometer (km)": 1000.0,
                "Meter (m)": 1.0,
                "Decimeter (dm)": 0.1,
                "Centimeter (cm)": 0.01,
                "Millimeter (mm)": 0.001,
                "Micrometer (µm)": 1e-6,
                "Nanometer (nm)": 1e-9
            },
            "Imperial/US": {
                "Mile (mi)": 1609.344,
                "Yard (yd)": 0.9144,
                "Foot (ft)": 0.3048,
                "Inch (in)": 0.0254
            },
            "Astronomical": {
                "Light Year (ly)": 9.461e15,
                "Astronomical Unit (AU)": 149597870700,
                "Parsec (pc)": 3.086e16
            },
            "Other Metric": {
                "Exameter (Em)": 1e18,
                "Petameter (Pm)": 1e15,
                "Terameter (Tm)": 1e12,
                "Gigameter (Gm)": 1e9,
                "Megameter (Mm)": 1e6,
                "Hectometer (hm)": 100,
                "Dekameter (dam)": 10,
                "Picometer (pm)": 1e-12,
                "Femtometer (fm)": 1e-15,
                "Attometer (am)": 1e-18
            }
        }
        
        # Flatten units for conversion
        self.units = {}
        for category in self.unit_categories.values():
            self.units.update(category)

    def convert(self, value, from_unit, to_unit):
        try:
            value = float(value)
            # Convert to meters first, then to target unit
            meters = value * self.units[from_unit]
            result = meters / self.units[to_unit]
            return result
        except ValueError:
            return "Invalid input"
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    st.set_page_config(page_title="Length Unit Converter", page_icon="🧮")
    
    # Add custom CSS
    st.markdown("""
        <style>
        .stApp {
        background: linear-gradient(to top,rgb(226, 167, 235),rgb(243, 196, 185));
        color: maroon;
    }
        .main {
            padding: 2rem;
        }
        .stSelectbox {
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Title and description
    st.title("🧮 Length Unit Converter")
    st.markdown("Convert between different units of length measurement")
    
    # Initialize converter
    converter = LengthConverter()
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("From")
        # Category selection for source unit
        from_category = st.selectbox(
            "Select source category",
            options=list(converter.unit_categories.keys()),
            key="from_category"
        )
        # Unit selection based on category
        from_unit = st.selectbox(
            "Select source unit",
            options=list(converter.unit_categories[from_category].keys()),
            key="from_unit"
        )
        # Input value
        value = st.number_input("Enter value", value=1.0)

    with col2:
        st.subheader("To")
        # Category selection for target unit
        to_category = st.selectbox(
            "Select target category",
            options=list(converter.unit_categories.keys()),
            key="to_category"
        )
        # Unit selection based on category
        to_unit = st.selectbox(
            "Select target unit",
            options=list(converter.unit_categories[to_category].keys()),
            key="to_unit"
        )

    # Convert button
    if st.button("Convert"):
        result = converter.convert(value, from_unit, to_unit)
        
        # Display result in a nice format
        st.markdown("### Result")
        result_container = st.container()
        with result_container:
            st.markdown(
                f"""
                <div style="padding: 1rem; border-radius: 0.5rem; background-color: #f0f2f6;">
                    {value} {from_unit} = 
                    <span style="font-size: 1.2em; font-weight: bold;">
                        {result:.10g} {to_unit}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Add information about the converter
    with st.expander("ℹ️ About this converter"):
        st.markdown("""
            This length converter supports various unit categories:
            - Metric units (kilometer to nanometer)
            - Imperial/US units (mile, yard, foot, inch)
            - Astronomical units (light year, parsec, AU)
            - Extended metric units (exa to atto)
            
            All conversions are performed using standard conversion factors relative to meters.
        """)

if __name__ == "__main__":
    main()
