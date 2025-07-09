from geometry import Square, Circle, area_stats

def main():
    # Create shapes
    s = Square(4)
    c = Circle(2.0)

    # Print individual areas
    print(f"Square area: {s.area():.2f}")
    print(f"Circle area: {c.area():.2f}")

    # Compute and print area stats
    stats = area_stats(s, c)
    print("\nArea stats summary:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

if __name__ == "__main__":
    main()