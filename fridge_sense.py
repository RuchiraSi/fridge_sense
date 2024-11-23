# Importing necessary libraries
import streamlit as st
import pandas as pd

# Mock AI Model (Simulated for Now)
def ai_recognize_ingredients(image):
    """
    Simulates AI ingredient recognition from an uploaded image.
    Returns a list of recognized ingredients.
    """
    # Mock ingredients based on random recognition
    return ["Milk", "Eggs", "Cheese", "Tomatoes"]

# Placeholder for ingredient data
if "ingredients" not in st.session_state:
    st.session_state["ingredients"] = []

# App Title
st.title("FridgeSense - AI-Powered Ingredient Tracker")

# Navigation Sidebar
menu = st.sidebar.radio("Menu", ["Home", "Ingredient Tracker", "Recipe Generator", "Community Hub"])

# Home Section
if menu == "Home":
    st.header("Welcome to FridgeSense!")
    st.write("Track your fridge contents, reduce food waste, and discover amazing recipes!")
    st.image("https://via.placeholder.com/600x300?text=FridgeSense+Prototype", caption="Your Smart Kitchen Companion")

# Ingredient Tracker Section with AI
elif menu == "Ingredient Tracker":
    st.header("🛒 AI Ingredient Tracker")
    
    # Upload Image for AI Recognition
    st.subheader("📸 Upload Fridge Image")
    uploaded_image = st.file_uploader("Choose a photo of your fridge", type=["jpg", "jpeg", "png"])
    
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        st.write("Analyzing image...")
        
        # Simulate AI Recognition
        recognized_ingredients = ai_recognize_ingredients(uploaded_image)
        st.success(f"AI detected the following ingredients: {', '.join(recognized_ingredients)}")
        
        # Add to Tracker
        if st.button("Add to Tracker"):
            for ingredient in recognized_ingredients:
                st.session_state["ingredients"].append({"Ingredient": ingredient, "Expiry Date": "Not Set"})
            st.success("Ingredients added to your tracker!")

    # Form to Add Ingredients Manually
    with st.form("add_ingredient"):
        col1, col2 = st.columns(2)
        ingredient = col1.text_input("Ingredient Name")
        expiry_date = col2.date_input("Expiry Date", key="manual_expiry")
        submit = st.form_submit_button("Add Ingredient")
        
        if submit and ingredient:
            st.session_state["ingredients"].append({"Ingredient": ingredient, "Expiry Date": expiry_date})
            st.success(f"Added {ingredient} with expiry date {expiry_date}")

    # Display Current Ingredients
    if st.session_state["ingredients"]:
        st.subheader("Your Fridge Contents")
        df = pd.DataFrame(st.session_state["ingredients"])
        st.table(df)
    else:
        st.info("No ingredients added yet.")

# Recipe Generator Section
elif menu == "Recipe Generator":
    st.header("🍳 Recipe Generator")
    st.write("Choose ingredients to find matching recipes!")
    
    if st.session_state["ingredients"]:
        all_ingredients = [item["Ingredient"] for item in st.session_state["ingredients"]]
        selected_ingredients = st.multiselect("Your Ingredients", all_ingredients, default=[])
        
        if selected_ingredients:
            # Mock recipe suggestions
            st.subheader("Suggested Recipes")
            recipes = {
                frozenset(["Milk", "Eggs"]): "Fluffy Pancakes",
                frozenset(["Tomatoes", "Cheese"]): "Caprese Salad",
                frozenset(["Milk", "Cheese"]): "Cheesy Pasta"
            }
            matched_recipes = [
                recipe for ingredients, recipe in recipes.items() 
                if frozenset(selected_ingredients).issubset(ingredients)
            ]
            if matched_recipes:
                for recipe in matched_recipes:
                    st.success(recipe)
            else:
                st.warning("No recipes match your ingredients.")
        else:
            st.info("Select ingredients to get started.")
    else:
        st.info("No ingredients available in the tracker. Add some first!")

# Community Hub Section
elif menu == "Community Hub":
    st.header("🌐 Community Hub")
    st.write("Share your favorite recipes or tips!")
    post = st.text_area("Write something...")
    if st.button("Post"):
        st.success("Your post has been shared!")
    # Mock display of community posts
    st.subheader("Recent Posts")
    mock_posts = [
        {"user": "Alice", "post": "Check out my avocado toast recipe! 🥑"},
        {"user": "Bob", "post": "Leftover veggies? Make a hearty soup!"}
    ]
    for p in mock_posts:
        st.write(f"**{p['user']}**: {p['post']}")
