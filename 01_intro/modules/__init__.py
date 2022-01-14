
def md_hello():
    """This is a simples Hello Function
    """
    print("Hello from a function inside a module") 
    


def md_subtraction (a = float ,b =  float) -> float:
    """This is a Subtraction funtion

    Args:
        a ([type], optional): [description]. Defaults to float.
        b ([type], optional): [description]. Defaults to float.

    Returns:
        float: [description]
    """

    print(md_subtraction.__name__ + ' is running')
    
    return a - b