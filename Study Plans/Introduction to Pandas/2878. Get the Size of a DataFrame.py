import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return[players.shape[0],players.shape[1]]
    #players.shape[0] gives the number of rows in the DataFrame players.
    #players.shape[1] gives the number of columns in the DataFrame players.
    #This line thus returns a list containing these two values: [players.shape[0], players.shape[1]].
