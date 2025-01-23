def validate_csv(data):
    required_columns = {"Air temperature", "Rotational speed", "Tool wear", "Target"}
    return set(required_columns).issubset(data.columns)

def validate_json(input_data):
    required_keys = {"Air temperature", "Rotational speed", "Tool wear"}
    return required_keys.issubset(input_data.keys())