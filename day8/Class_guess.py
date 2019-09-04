"""
面向对象的猜字游戏
"""
from random import  randint
class GuessGame(object):
    def __init__(self):
        self._answer = None
        self._count = None
        self._hint = None
    def reset(self):
        self._answer = randint(1,100)
        self._count = 0
        self._hint = None

    def guess(self, your_answer):
        self._count += 1
        if your_answer > self._answer:
            self._hint = '猜大了'
        elif your_answer < self._answer:
            self._hint = '猜小了'
        else:
            self._hint = '恭喜你猜对了'
            return True
        return False

    @property
    def count(self):
        return self._count

    @property
    def hint(self):
        return self._hint
if __name__ == '__main__':
    if __name__ == '__main__':
        gm = GuessGame()
        play_again = True
        while play_again:
            game_over = False
            gm.reset()
            while not game_over:
                your_answer = int(input('请输入: '))
                game_over = gm.guess(your_answer)
                print(gm.hint)
            if gm.count > 7:
                print('智商余额不足!')
            play_again = input('再玩一次?(yes|no)') == 'yes'