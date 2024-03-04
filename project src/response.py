from utils import tx, rx
from gpt import genCompletion
def response(x):
    rx.print('>>> '+x)
    tx.print('>>> '+genCompletion(x))