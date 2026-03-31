def hello(name=None):
    """
    Generate a greeting message.
    
    Args:
        name (str, optional): Name to greet. Defaults to 'World'.
    
    Returns:
        str: Greeting message
    
    Raises:
        TypeError: If name is not a string or None
    """
    if name is None:
        name = 'World'
    
    if not isinstance(name, str):
        raise TypeError("name must be a string or None")
    
    if not name.strip():
        raise ValueError("name cannot be empty")
    
    return f'Hello, {name}!'
