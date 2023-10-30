# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from streamlit_marquee import streamlit_marquee
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain 


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

# Car Information

# Database of Cars including their make, digital address, and hourly cost per Ether.
# A single Ether is currently valued at $1,500
car_database = {
    "Toyota": ["Toyota", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", 22, "Images/Toyota.jpg"],
    "Honda": ["Honda", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",  151, "Images/Honda.jpg"],
    "Tesla": ["Tesla","0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", 31, "Images/Tesla.jpeg"],
    "Porsche": ["Porsche","0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", 50, "Images/Porsche.jpg"],
    "Ford": ["Ford", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", 60, "Images/Ford.jpg"]
}

# A list of the Cars
cars = ["Toyota", "Honda", "Tesla", "Porsche", "Ford"]


def get_cars():
    """Display the database of KryptoJobs2Go car information."""
    db_list = list(car_database.values())

    for number in range(len(cars)):
        st.image(db_list[number][3], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        #st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][2], "eth")
        st.text(" \n")

# Streamlit Code

# Streamlit application headings

#st.markdown("# Car Rental!")
streamlit_marquee(**{
    # the marquee container background color
    'background': "#5D00FF",
    # the marquee text size
    'fontSize': '48px',
    # the marquee text color
    "color": "#ffffff",
    # the marquee text content
    'content': 'Welcome to our Car Rental Shop! View our rental selection below!',
    # the marquee container width
    'width': '600px',
    # the marquee container line height
    'lineHeight': "35px",
    # the marquee duration
    'animationDuration': '10s',
})
#using the streamlit extras import, make any emoji rain on your app using the following code
rain(
    emoji="❄️",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)
#this uses an import with the streamlit extras import, it provides a 'clickable button' that when pressed, will show text underneath it
stoggle(
    "Click me!",
    """Surprise! You Just Earned 8% off!""",
)
#st.markdown("## Rent a Car!")
st.text(" \n")

# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
ether = get_balance(w3, account.address)
st.sidebar.write(ether)

# Create a select box to chose a FinTech Hire car
car = st.sidebar.selectbox("Select a Car", cars)

# Create a input field to record the number of hours the car worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Car Name, Hourly Rate, and Ethereum Address")

# Identify the car
car = car_database[car][0]

# Write the cars make to the sidebar
st.sidebar.write(car)

# Identify the cars hourly rate
hourly_rate = car_database[car][2]

# Write the cars hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the cars Ethereum Address
car_address = car_database[car][1]

# Write cars Ethereum Address to the sidebar
st.sidebar.write(car_address)

# Write the rental cars make to the sidebar

st.sidebar.markdown("## Total Rent in Ether")

# Calculate total `rent` for the car by multiplying the cars hourly
# rate from the car database (`car_database[car][2]`) by the
# value of the `hours` variable
rent = car_database[car][2]*hours

# @TODO
# Write the `rent` calculation to the Streamlit sidebar
st.sidebar.write(rent)

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.

if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `car_address`, and the `rent` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, car_address, rent)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.snow()

# The function that starts the Streamlit application
# Writes KryptoJobs2Go cars to the Streamlit page
get_cars()