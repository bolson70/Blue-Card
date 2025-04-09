import os
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Path to the building images
BUILDING_FOLDER = "static/buildings"

# Firefighter size-up categories
size_up_prompts = [
    "Describe the building type and construction.",
    "Identify occupancy type and potential hazards.",
    "Assess fire conditions and location.",
    "Evaluate exposures and surrounding risks.",
    "Determine firefighting strategy (Offensive/Defensive).",
    "List the additional resources needed."
]

def get_random_building():
    """Fetches a random building image from the static/buildings folder."""
    if not os.path.exists(BUILDING_FOLDER):
        return None
    buildings = [f for f in os.listdir(BUILDING_FOLDER) if f.endswith(('.jpg', '.png', '.jpeg'))]
    return random.choice(buildings) if buildings else None

@app.route("/", methods=["GET", "POST"])
def size_up():
    """Handles the display of a random building and user input for size-up practice."""
    building_image = get_random_building()
    prompt = random.choice(size_up_prompts)

    feedback = None
    if request.method == "POST":
        user_response = request.form["size_up"]
        feedback = f"Your size-up: {user_response}. Keep practicing to master BlueCard!"

    return render_template("size_up.html", building_image=building_image, prompt=prompt, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
