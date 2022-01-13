
def md_hello():
    """[summary]
    """
    print("Hello from a function inside a module") 
    


def md_difference(a = float ,b =  float) -> float:
    """[summary]

    Args:
        a ([type], optional): [description]. Defaults to float.
        b ([type], optional): [description]. Defaults to float.

    Returns:
        float: [description]
    """

    print(md_difference.__name__ + ' is running')
    
    return a - b