import turtle
import time

screen = turtle.Screen()
screen.title("2D Tower of Hanoi - Realistic Version")
screen.bgcolor("#e0f7fa")  # blue color

# Custom bg
# screen.bgpic('background.gif')

num_disks = int(screen.numinput("Input", "Enter the number of disks (1-10):", minval=1, maxval=10))
speed = screen.numinput("Input", "Enter the speed of the animation (1=slow, 10=fast):", minval=1, maxval=10)

# Create turtle for pegs
peg = turtle.Turtle()
peg.speed(0)
peg.hideturtle()

# To draw pegs with shadows and borders
def draw_pegs():
    peg.penup()
    peg.pensize(5)
    
    colors = ['#8B4513', '#8B4513', '#8B4513']  
    shadow_color = '#A0522D'  # Darker shadow color for pegs

    for i, x_pos in enumerate([-200, 0, 200]):
        # Draw shadow
        peg.color(shadow_color)
        peg.goto(x_pos - 5, -105)
        peg.setheading(90)
        peg.pendown()
        peg.forward(205)
        peg.penup()

        # Draw peg with a border effect
        peg.color(colors[i])
        peg.goto(x_pos, -100)
        peg.pendown()
        peg.forward(200)
        peg.penup()

# Custom Disk class with textures and shading
class Disk(turtle.Turtle):
    def __init__(self, size, color, texture_color):
        super().__init__(shape="square")
        self.size = size
        self.shapesize(1, size)  # Adjust size
        self.color(color)
        self.fillcolor(texture_color)  # Add texture-like color
        self.penup()
        self.speed(speed)  # Set speed for disk movement

    def move_to(self, x, y, delay=0.1):
        # Move the disk to x, y coordinates with easing for smoother effect
        start_x, start_y = self.pos()
        dx = (x - start_x) / 20
        dy = (y - start_y) / 20
        for _ in range(20):
            self.goto(self.xcor() + dx, self.ycor() + dy)
            time.sleep(delay)

disk_list = [] 
peg_positions = [-200, 0, 200]  # Peg positions on x-axis
peg_stacks = [[], [], []]  # Disks currently on each peg

# Function to set up the disks on the first peg with textures and shadows
def setup_disks():
    colors = ['#FF4500', '#1E90FF', '#32CD32', '#FFA500', '#9400D3', '#FFD700', '#FF1493', '#8B4513', '#00CED1', '#FF69B4']  # Disk colors
    textures = ['#FF6347', '#4682B4', '#2E8B57', '#FF8C00', '#8A2BE2', '#FFD700', '#FF69B4', '#A0522D', '#20B2AA', '#FFB6C1']  # Lighter colors for texture
    for i in range(num_disks, 0, -1):
        disk = Disk(i * 2, colors[i - 1], textures[i - 1])
        disk_list.append(disk)
        peg_stacks[0].append(disk)  # Add disk to first peg
        disk.move_to(peg_positions[0], -100 + (len(peg_stacks[0]) - 1) * 20, delay=0)  # Initial position without delay

# To move a disk with easing
def move_disk(from_peg, to_peg):
    if peg_stacks[from_peg]:
        # Pop the top disk from the from_peg stack
        disk = peg_stacks[from_peg].pop()
        disk.move_to(disk.xcor(), 120, delay=0.02)
        disk.move_to(peg_positions[to_peg], 120, delay=0.02)

        # Calculate new y-position based on how many disks are on the destination peg
        new_y = -100 + len(peg_stacks[to_peg]) * 20
        disk.move_to(peg_positions[to_peg], new_y, delay=0.02)
        peg_stacks[to_peg].append(disk)

# Tower of Hanoi recursive solution
def hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        move_disk(from_peg, to_peg)
    else:
        hanoi(n - 1, from_peg, aux_peg, to_peg)
        move_disk(from_peg, to_peg)
        hanoi(n - 1, aux_peg, to_peg, from_peg)

draw_pegs()
setup_disks()

# Start solving the Tower of Hanoi
hanoi(num_disks, 0, 2, 1)

screen.mainloop()
