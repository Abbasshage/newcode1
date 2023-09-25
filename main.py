import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_volleyball_court():
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Volleyball court dimensions (FIVB standard)
    court_width = 9  # meters
    court_length = 18  # meters
    front_width = 9  # meters
    front_length = 6  # meters
    center_width = 9  # meters
    center_length = 3  # meters
        
    # Draw the volleyball court boundary
    ax.add_patch(patches.Rectangle((0, 0), court_length, court_width, linewidth=2, edgecolor='blue', facecolor='none'))

    # Draw the volleyball front zone boundary
    ax.add_patch(patches.Rectangle((6, 0), front_length, front_width, linewidth=2, edgecolor='red', facecolor='none'))
    
   # Draw the volleyball center line boundary
    ax.add_patch(patches.Rectangle((9, 0), center_length, center_width, linewidth=2, edgecolor='red', facecolor='none'))
    
    ax.set_xlim(0, court_length)
    ax.set_ylim(0, court_width)
    ax.set_aspect('equal')
    plt.title("Volleyball Court")

    # Save the image as a PNG file
    plt.savefig("volleyball_court.png", dpi=300)
    plt.show()

# Example usage:
draw_volleyball_court()


