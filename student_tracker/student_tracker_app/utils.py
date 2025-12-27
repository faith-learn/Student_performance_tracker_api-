def calculate_performance_status(marks):
    """
    Simple AI-like logic to determine student performance.
    """
    if marks >= 75:
        return "Excellent"
    elif marks >= 60:
        return "Good"
    elif marks >= 40:
        return "At Risk"
    else:
        return "Failing"
