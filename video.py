import turtle

# Function to draw a filled circle
def draw_filled_circle(turtle_obj, radius, color):
    turtle_obj.begin_fill()
    turtle_obj.color(color)
    turtle_obj.circle(radius)
    turtle_obj.end_fill()

# Function to draw an eye
def draw_eye(turtle_obj, x, y, radius, color):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    draw_filled_circle(turtle_obj, radius, color)

# Function to draw a smile
def draw_smile(turtle_obj, x, y, radius):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(-60)
    turtle_obj.pendown()
    turtle_obj.circle(radius, 120)

# Main function to draw the cartoon character
def draw_cartoon_character():
    # Setup screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Python Turtle Cartoon Character")

    # Create turtle object
    character = turtle.Turtle()
    character.speed(0)

    # Draw head
    draw_filled_circle(character, 100, "yellow")

    # Draw eyes
    draw_eye(character, -40, 120, 15, "black")
    draw_eye(character, 40, 120, 15, "black")

    # Draw pupils
    draw_eye(character, -40, 120, 5, "white")
    draw_eye(character, 40, 120, 5, "white")

    # Draw smile
    draw_smile(character, 0, 60, 60)

    # Hide turtle and display result
    character.hideturtle()
    turtle.done()

# Call the main function to draw the cartoon character
if __name__ == "__main__":
    draw_cartoon_character()
