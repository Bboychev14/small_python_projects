from unittest import TestCase, main

from hero import Hero


class HeroTests(TestCase):

    def test_constructor(self):
        test_hero = Hero("test", 80, 30.5, 15.8)
        self.assertEqual("test", test_hero.username)
        self.assertEqual(80, test_hero.level)
        self.assertEqual(30.5, test_hero.health)
        self.assertEqual(15.8, test_hero.damage)

    def setUp(self) -> None:
        self.hero = Hero("Badrhari", 40, 25, 1)

    def test_battle_with_same_names(self):
        enemy = Hero("Badrhari", 79, 30.5, 20)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_self_health_equal_or_less_than_zero(self):
        enemy = Hero("Medi", 80, 20, 18)
        self.hero.health = 0
        self.assertEqual(0, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
        self.hero.health = - 1
        self.assertEqual(- 1, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_health_equal_or_less_than_zero(self):
        enemy = Hero("Medi", 80, 0, 15)
        self.assertEqual(0, enemy.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

        enemy.health = - 1
        self.assertEqual(- 1, enemy.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_for_draw_case(self):
        enemy = Hero("Medi", 30, 20, 1)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_battle_for_draw_case_border_data(self):
        enemy = Hero("Medi", 30, 20, 1)
        enemy.health = 40
        self.assertEqual(40, enemy.health)
        enemy.level = 25
        self.assertEqual(25, enemy.level)
        border_result = self.hero.battle(enemy)
        self.assertEqual("Draw", border_result)

    def test_battle_with_enemy_health_equal_to_zero(self):
        enemy = Hero("Medi", 15, 40, 1)
        result = self.hero.battle(enemy)
        self.assertEqual(41, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(6, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_with_enemy_health_less_than_zero(self):
        enemy = Hero("Medi", 15, 20, 1)
        result = self.hero.battle(enemy)
        self.assertEqual(41, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(6, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_with_self_health_equal_to_zero(self):
        enemy = Hero("Medi", 10, 50, 2.5)
        result = self.hero.battle(enemy)
        self.assertEqual(11 ,enemy.level)
        self.assertEqual(15, enemy.health)
        self.assertEqual(7.5, enemy.damage)
        self.assertEqual("You lose", result)

    def test_battle_with_self_health_less_than_zero(self):
        enemy = Hero("Medi", 10, 50, 3)
        result = self.hero.battle(enemy)
        self.assertEqual(11 ,enemy.level)
        self.assertEqual(15, enemy.health)
        self.assertEqual(8, enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_method(self):
        expected =  f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        result = self.hero.__str__()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()