# If you receive -1 means you are P1 and you have to start.
def generateReply(self, receivedMove, _sendReply=None):
    if receivedMove == -1:
        # Implement logic to generate first move as P1
        move = 0
    else:
        # Implement your logic here to generate next move
        move = 1

    if _sendReply:
        _sendReply(move)
