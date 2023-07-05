class IsNotFound(Exception):
    """データがみつからない時のエラー

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, *args):
        super().__init__(*args)
