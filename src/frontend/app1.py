import streamlit as st
import requests


st.set_page_config(
    page_title="Merchant Loan Eligibility",
    page_icon="💰",
    layout="centered"
)


st.title(
    "Merchant Loan Eligibility System"
)


st.write(
    "Enter the merchant pharmacy name and location "
    "to predict loan eligibility."
)


pharmacy_name = st.text_input(
    "Pharmacy Name",
    placeholder="Example: Apollo Pharmacy"
)


location = st.text_input(
    "Location",
    placeholder="Example: Anna Nagar, Chennai"
)


if st.button(
    "Check Loan Eligibility"
):

    if not pharmacy_name or not location:

        st.warning(
            "Please enter both pharmacy name and location."
        )

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",

                json={
                    "pharmacy_name": pharmacy_name,
                    "location": location
                },

                timeout=30
            )


            if response.status_code == 200:

                result = response.json()


                st.success(
                    "Prediction completed successfully."
                )


                st.subheader(
                    "Location Details"
                )


                st.write(
                    f"Pharmacy Name: "
                    f"{result['pharmacy_name']}"
                )


                st.write(
                    f"Location: "
                    f"{result['location']}"
                )


                st.write(
                    f"Latitude: "
                    f"{result['latitude']}"
                )


                st.write(
                    f"Longitude: "
                    f"{result['longitude']}"
                )


                st.subheader(
                    "Nearby Facilities"
                )


                features = result[
                    "nearby_features"
                ]


                st.write(
                    f"Nearby Hospitals: "
                    f"{features['nearby_hospital_count']}"
                )


                st.write(
                    f"Nearby Banks: "
                    f"{features['nearby_bank_count']}"
                )


                st.write(
                    f"Nearby ATMs: "
                    f"{features['nearby_atm_count']}"
                )


                st.write(
                    f"Nearby Clinics: "
                    f"{features['nearby_clinic_count']}"
                )


                st.write(
                    f"Nearby Supermarkets: "
                    f"{features['nearby_supermarket_count']}"
                )


                st.write(
                    f"Nearby Bus Stops: "
                    f"{features['nearby_bus_stop_count']}"
                )


                st.subheader(
                    "Loan Eligibility"
                )


                if result[
                    "loan_eligibility"
                ] == "Eligible":

                    st.success(
                        "Loan Eligibility: Eligible"
                    )

                else:

                    st.error(
                        "Loan Eligibility: Not Eligible"
                    )


            else:

                try:

                    error_message = response.json().get(
                        "detail",
                        "Failed to generate prediction."
                    )

                except Exception:

                    error_message = (
                        "Failed to generate prediction."
                    )


                st.error(
                    error_message
                )


        except requests.exceptions.ConnectionError:

            st.error(
                "Unable to connect to FastAPI server. "
                "Please make sure Uvicorn is running."
            )


        except requests.exceptions.Timeout:

            st.error(
                "The request timed out. "
                "Please try again."
            )


        except Exception as e:

            st.error(
                f"An error occurred: {e}"
            )