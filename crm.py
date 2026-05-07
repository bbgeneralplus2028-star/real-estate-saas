def pipeline_stage(score):
    if score >= 80:
        return "HOT"
    elif score >= 60:
        return "WARM"
    return "COLD"
