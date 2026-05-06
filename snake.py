import tkinter as tk
import random

# Konstanty hry
WIDTH = 600
HEIGHT = 400
SIZE = 20
SPEED = 100  # ms mezi pohyby

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Had - Snake Game")

        # Plátno pro kreslení
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Skóre
        self.score = 0
        self.score_label = tk.Label(root, text=f"Skóre: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        # Počáteční stav
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Seznam souřadnic (x, y)
        self.direction = "Right"
        self.food = None
        self.running = True

        # Nabindování kláves
        self.root.bind("<Left>", lambda e: self.change_direction("Left"))
        self.root.bind("<Right>", lambda e: self.change_direction("Right"))
        self.root.bind("<Up>", lambda e: self.change_direction("Up"))
        self.root.bind("<Down>", lambda e: self.change_direction("Down"))

        self.spawn_food()
        self.game_loop()

    def spawn_food(self):
        """Vytvoří jídlo na náhodné pozici."""
        while True:
            x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
            y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, new_dir):
        """Změní směr, pokud není opačný k aktuálnímu."""
        opposites = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir

    def move(self):
        """Pohne hadem o jeden krok."""
        head_x, head_y = self.snake[0]

        if self.direction == "Left":
            head_x -= SIZE
        elif self.direction == "Right":
            head_x += SIZE
        elif self.direction == "Up":
            head_y -= SIZE
        elif self.direction == "Down":
            head_y += SIZE

        new_head = (head_x, head_y)

        # Kontrola kolizí
        if (head_x < 0 or head_x >= WIDTH or 
            head_y < 0 or head_y >= HEIGHT or 
            new_head in self.snake):
            self.running = False
            return

        self.snake.insert(0, new_head)

        # Snědení jídla
        if new_head == self.food:
            self.score += 1
            self.score_label.config(text=f"Skóre: {self.score}")
            self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        """Vykreslí hada a jídlo na plátno."""
        self.canvas.delete("all")
        
        # Jídlo
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx + SIZE, fy + SIZE, fill="red", outline="white")

        # Had
        for i, (sx, sy) in enumerate(self.snake):
            color = "green" if i == 0 else "lime" # Hlava je tmavší zelená
            self.canvas.create_rectangle(sx, sy, sx + SIZE, sy + SIZE, fill=color, outline="black")

    def game_over(self):
        """Zobrazí nápis Game Over."""
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2, 
            text="GAME OVER", fill="white", 
            font=("Arial", 30, "bold")
        )

    def game_loop(self):
        """Hlavní smyčka hry."""
        if self.running:
            self.move()
            self.draw()
            self.root.after(SPEED, self.game_loop)
        else:
            self.game_over()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
