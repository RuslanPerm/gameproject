import board
import Hero

Wolfova = Hero.Strength(25, 1, 24, 0, "Wolfova")
Tank = Hero.Strength(35, 10, 5, 1, "Танк")
Trushechkinov = Hero.Agility(20, 25, 5, 0, "Трушечкинов")
Dogg = Hero.Agility(17, 18, 15, 1, "Dogg")
ShieldDearer = Hero.Intelligence(11, 17, 22, 0, "ShieldDearer")
Oleg = Hero.Intelligence(8, 15, 27, 1, "Oleg")

board = board.Board()
board.add(Wolfova, 1, 7)
board.add(Tank, 3, 0)
board.add(Trushechkinov, 6, 9)
board.add(Dogg, 9, 1)
board.add(ShieldDearer, 13, 1)
board.add(Oleg, 8, 2)

board.game()