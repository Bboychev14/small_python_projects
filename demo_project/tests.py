with self.assertRaises(ValueError) as context:
    self.driver.drive_best_cargo_offer()
self.assertEqual("There are no offers available.", str(context.exception))