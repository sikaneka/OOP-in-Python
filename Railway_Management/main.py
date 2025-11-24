import streamlit as st
from models.train import Train
from models.passenger import Passenger
from models.railway_system import RailwaySystem

# Initialize system
system = RailwaySystem()

# Add sample trains
if not system.trains:
    system.add_train(Train("101", "Rajdhani Express", "Delhi", "Mumbai", 5))
    system.add_train(Train("102", "Shatabdi Express", "Chennai", "Bangalore", 4))
    system.add_train(Train("103", "Duronto Express", "Kolkata", "Delhi", 3))

st.title("🚆 Railway Management System")
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["View Trains", "Book Ticket", "Cancel Ticket", "View All Tickets"])

if page == "View Trains":
    st.subheader("Available Trains")
    for info in system.show_trains():
        st.write(info)

elif page == "Book Ticket":
    st.subheader("🎟️ Book a Ticket")
    name = st.text_input("Passenger Name")
    age = st.number_input("Age", 1, 120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    train_no = st.text_input("Train Number")

    if st.button("Book Now"):
        passenger = Passenger(name, age, gender)
        result = system.book_ticket(train_no, passenger)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success("✅ Ticket Booked Successfully!")
            st.json(result.show_ticket())

elif page == "Cancel Ticket":
    st.subheader("❌ Cancel Ticket")
    ticket_id = st.text_input("Enter Ticket ID")

    if st.button("Cancel Ticket"):
        st.info(system.cancel_ticket(ticket_id))

elif page == "View All Tickets":
    st.subheader("📄 All Booked Tickets")
    if not system.tickets:
        st.warning("No tickets booked yet.")
    else:
        for t in system.tickets:
            st.json(t.show_ticket())
