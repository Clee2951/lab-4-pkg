from .shapes import Shape, Rectangle, Triangle
def area_stats(*shapes):
    if not shapes:
        raise ValueError("At least one Shape is required")
    areas = [shape.area() for shape in shapes ]
    #areas = areas.sort()
    return {
    "n": len(areas),
    "total": sum(areas),
    "mean": sum(areas)/ len(areas),
    "min": areas[0],
    "max": areas[-1],
    }