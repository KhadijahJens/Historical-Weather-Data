import unittest
from weather import Weather


class MyTestCase(unittest.TestCase):

    def test_get_mean_temp(self):
        temp_instance = Weather(52.52, 13.41, 1, 14, 2024, 0, 0, 0,
                                0, 0, 0, 0, 0, 0)
        temp_instance.get_mean_temp()

        avg_temp = temp_instance.avg_temp
        min_temp = temp_instance.min_temp
        max_temp = temp_instance.max_temp

        self.assertEqual(avg_temp, 40.239999999999995)
        self.assertEqual(min_temp, 33.5)
        self.assertEqual(max_temp, 48.7)

    def test_get_max_wind(self):
        wind_instance = Weather(52.52, 13.41, 1, 14, 2024, 0, 0, 0,
                                0, 0, 0, 0, 0, 0)
        wind_instance.get_max_wind()

        avg_wind = wind_instance.avg_wind
        min_wind = wind_instance.min_wind
        max_wind = wind_instance.max_wind

        self.assertEqual(avg_wind, 17.86)
        self.assertEqual(min_wind, 12.8)
        self.assertEqual(max_wind, 20.4)

    def test_get_precip_sum(self):
        precip_instance = Weather(52.52, 13.41, 1, 14, 2024, 0, 0, 0,
                                  0, 0, 0, 0, 0, 0)
        precip_instance.get_precip_sum()

        sum_precip = precip_instance.sum_precip
        min_precip = precip_instance.min_precip
        max_precip = precip_instance.max_precip

        self.assertEqual(sum_precip, 0.568)
        self.assertEqual(min_precip, 0.0)
        self.assertEqual(max_precip, 0.469)


if __name__ == '__main__':
    unittest.main()
