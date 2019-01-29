import random

team_name = 'RoBradlert'
strategy_name = 'Undesicive'
strategy_description = 'I have never been interrogated before, I hope I get out!'
    
def move(my_history, their_history, my_score, their_score):
    if 'c' in their_history[-1]:
        return 'b'
    else:
        if random.random() < 0.5:
            return random.choice(their_history[-5])
        else:
            return 'b'


def test_move(my_history, their_history, my_score, their_score, result):
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history = '',
              their_history = '', 
              my_score = 0,
              their_score = 0,
              result = 'b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history = 'bbb',
              their_history = 'ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score = 0, 
              their_score = 0,
              result = 'b')    