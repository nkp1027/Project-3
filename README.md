# Project-3
## Project Proposal
Our project goal is to create an online car rental business that offers a variety of vehicles that can be rented per hour at set prices of Ethereum. The majority of this will be created by a mix of Python and Streamlit while having connections to Ganache as well to show that the transactions are working. Ideally, a customer will visit the site, pick a car they would like to rent and select the number of hours they desire to rent it for. The price will automatically be calculated and displayed on the sidebar of the Streamlit app. Once this occurs, the customer can submit a transaction which will then prompt a confirmation and animation on the page.
## Project Members
Nipun, Jeff, Exzavier, Nostalgie
## Title
Car Rental App
## Project Description
We'll first start off by working on our crypto_wallet script ensuring we have a fully functional way to make transactions within our app. We will make 3 functions. The first python function will be a way to generate an account with a functional Ethereum wallet. First we'll pull our Mnemonic phrase from our Ganache and place it within an .env file to then link together with our Wallet variable. From there we will obtain our Ethereum private key from the wallet set to use and convert it into an Ethereum account suitable to use for our payments. The second python function simply obtains the balance of our account by getting the balance of the address in Wei to then convert Wei into the easier to read Ethereum. Our final function within our crypto_wallet script enables us to send transactions to our Ganache account. We have to first set the gas price strategy and from there we will convert the Ethereum amount to Wei to be able to get the gas estimate. Finally we'll construct a raw transaction to have signed when making purchases within our car rental app. Now we will work within our car_shop script to make a fully functional app. We will first link together the wallet by setting our web3 variable to pull from the Ganache web address. From there we will import all of our created functions from crypto_wallet to make sure our wallet is usable for the car rental application. We then made a list for the car database, cars available for rent, and a function to display all the car's information by iterating through the database. The last of this script touches on adding the final touches to our car rental app to make it usable and appealing to the eye. We added necessities varying from a title, dropdown menus for various things, and indications of a receipt to know if the transaction has been approved or declined. We also added cool features from adding a marquee with a color background, a coupon to save some money, and a raindown background feature to make our app pop just a little more.
## Team Task Breakdown
All group members were responsible for individual research on new libraries that could be used for the app. It was a collaborative effort to build the app with the correct and precise coding required for it to function the way we intended it to. 
## Testing the App
In an effort to consolidate information and save time in teaching one to use this app successfully, we have uploaded a youtube video with step by step instructions. The link is provided here:
https://youtu.be/k6qMIj-ZbHY

## Installations
To install the Streamlit Marquee:
pip install streamlit-marquee

To install Streamlit Extras:
pip install streamlit-extras

To install Ganache:
Visit https://trufflesuite.com/ganache/ and click on the download button in the middle of the screen.

To install Web3.py:
pip install web3==5.17

To install bip44:
pip install bip44

To install ethereum tester:
pip install eth-tester==0.5.0b3

To install mnemonic:
pip install mnemonic

To install streamlit:
pip install streamlit
