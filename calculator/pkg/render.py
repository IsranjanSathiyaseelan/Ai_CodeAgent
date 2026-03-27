# render.py

def render(expression, result):
    """
    Returns a formatted string with the expression and result in a box.
    """
    # Convert result to int if it's a whole number
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    
    lines = [
        f"Expression: {expression}",
        f"Result: {result}"
    ]
    
    # Determine the box width (longest line + padding)
    width = max(len(line) for line in lines) + 4
    border = "+" + "-" * (width - 2) + "+"
    
    # Build the box
    boxed_lines = [border]
    for line in lines:
        boxed_lines.append(f"| {line.ljust(width - 4)} |")
    boxed_lines.append(border)
    
    return "\n".join(boxed_lines)