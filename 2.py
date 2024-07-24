import turtle

def draw_koch_segment(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        draw_koch_segment(t, order-1, size)
        t.left(60)
        draw_koch_segment(t, order-1, size)
        t.right(120)
        draw_koch_segment(t, order-1, size)
        t.left(60)
        draw_koch_segment(t, order-1, size)

def draw_koch_snowflake(t, order, size):
    for _ in range(3):
        draw_koch_segment(t, order, size)
        t.right(120)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    size = 300  # Розмір сніжинки

    # Налаштування Turtle
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()

    draw_koch_snowflake(t, level, size)

    turtle.done()

if __name__ == "__main__":
    main()