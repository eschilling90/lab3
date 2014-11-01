from unittest import TestCase
from mock import patch
import compute_highest_affinity
import randomized_input

class TestCases(TestCase):
	@patch('__builtin__.open')
	def test1(self, mock_open):
		site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]
		user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]
		time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829] 
		computed_result = compute_highest_affinity.highest_affinity(site_list, user_list, time_list)
		expected_result = ("a.com", "b.com")
		assert computed_result == expected_result

	@patch('__builtin__.open')
	def test2(self, mock_open):
		num_lines = 10000
		num_users = 1000
		site_list = randomized_input.randomized_site_list(num_lines)
		user_list = randomized_input.randomized_user_list(num_lines, num_users)
		time_list = xrange(0,num_lines)
		computed_result = compute_highest_affinity.highest_affinity(site_list, user_list, time_list)
		expected_result = ("facebook", "google")
		assert computed_result == expected_result

	@patch('__builtin__.open')
	def test2r(self, mock_open):
		site_list = ['rare_0.947116503135', 'rare_0.808607646816', 'facebook', 'rare_0.189685015258', 'rare_0.133816939439', 'bbc', 'rare_0.568252611521', 'google', 'rare_0.87538176169', 'cnn', 'cnn', 'facebook', 'rare_0.0580459194524', 'google', 'cnn', 'rare_0.61397224585', 'aol', 'rare_0.863162306928', 'bbc', 'aol', 'aol', 'google', 'rare_0.434654524657', 'aol', 'rare_0.209610014326', 'rare_0.681605721035', 'rare_0.984223665311', 'facebook', 'aol', 'rare_0.505177141857', 'google', 'cnn', 'facebook', 'rare_0.0874375770097', 'bbc', 'rare_0.445512942353', 'yahoo', 'rare_0.518880087409', 'rare_0.0255956674067', 'google', 'cnn', 'rare_0.0305622779494', 'rare_0.432630465423', 'cnn', 'aol', 'rare_0.666954456873', 'rare_0.731529437229', 'cnn', 'facebook', 'rare_0.881771903332', 'rare_0.316580115478', 'facebook', 'facebook', 'rare_0.113040464938', 'facebook', 'rare_0.363407847864', 'rare_0.622618636112', 'facebook', 'cnn', 'google', 'rare_0.0934833212494', 'facebook', 'facebook', 'rare_0.136808185848', 'rare_0.275107607517', 'rare_0.763139723523', 'facebook', 'rare_0.73136114256', 'google', 'rare_0.41293176847', 'rare_0.735043040521', 'rare_0.750323609094', 'yahoo', 'cnn', 'bbc', 'google', 'rare_0.512344482514', 'rare_0.990011024015', 'google', 'google', 'google', 'aol', 'facebook', 'aol', 'yahoo', 'rare_0.696935329262', 'rare_0.987628891217', 'cnn', 'cnn', 'rare_0.379696478141', 'rare_0.653890012305', 'google', 'rare_0.823949204381', 'rare_0.00338758417165', 'rare_0.525679379578', 'google', 'google', 'rare_0.802854973889', 'rare_0.0323349186925', 'rare_0.37866999392']
		user_list = ['user_6', 'user_1', 'user_2', 'user_7', 'user_3', 'user_2', 'user_0', 'user_2', 'user_4', 'user_2', 'user_9', 'user_6', 'user_2', 'user_3', 'user_0', 'user_1', 'user_3', 'user_4', 'user_9', 'user_3', 'user_3', 'user_1', 'user_3', 'user_8', 'user_4', 'user_9', 'user_7', 'user_8', 'user_4', 'user_0', 'user_9', 'user_6', 'user_7', 'user_8', 'user_5', 'user_0', 'user_0', 'user_5', 'user_8', 'user_8', 'user_8', 'user_7', 'user_7', 'user_4', 'user_7', 'user_9', 'user_6', 'user_4', 'user_1', 'user_6', 'user_3', 'user_7', 'user_3', 'user_1', 'user_5', 'user_0', 'user_8', 'user_0', 'user_2', 'user_7', 'user_0', 'user_3', 'user_2', 'user_2', 'user_3', 'user_5', 'user_3', 'user_2', 'user_4', 'user_3', 'user_2', 'user_6', 'user_7', 'user_1', 'user_0', 'user_9', 'user_2', 'user_4', 'user_4', 'user_3', 'user_1', 'user_9', 'user_9', 'user_3', 'user_4', 'user_2', 'user_9', 'user_8', 'user_9', 'user_8', 'user_3', 'user_5', 'user_4', 'user_3', 'user_2', 'user_8', 'user_8', 'user_3', 'user_9', 'user_1']

		time_list = xrange(0,100)

		computed_result = compute_highest_affinity.highest_affinity(site_list, user_list, time_list)
		expected_result = ("facebook", "google")

		assert computed_result == expected_result
		print "Successfully passed test2!"

	@patch('__builtin__.open')
	def test3(self, mock_open):
		a = "a"
		b = "b"
		c = "c"
		d = "d"
		e = "e"
		f = "f"
		g = "g"
		h = "h"

		A = "A"
		B = "B"
		C = "C"
		D = "D"
		E = "E"
		F = "F"
		G = "G"
		H = "H"


		user_list = [A, C, H, A, C, D, E, F, G, C, D, E, F, G, H, C, B, D, E, F, G, C, G, A, D, E, H, A, C, E, H]
		site_list = [a, a, a, b, b, b, b, b, b, c, c, c, c, c, c, d, e, e, e, e, e, f, f, g, g, g, g, h, h, h, h]

		time_list = range(0,30)

		computed_result = compute_highest_affinity.highest_affinity(site_list, user_list, time_list)
		expected_result = (b, c)

		assert computed_result == expected_result

	@patch('__builtin__.open')
	def test4(self, mock_open):

		a = "a"
		b = "b"
		c = "c"
		d = "d"
		e = "e"
		f = "f"
		g = "g"
		h = "h"

		A = "A"
		B = "B"
		C = "C"
		D = "D"
		E = "E"
		F = "F"
		G = "G"
		H = "H"


		site_list = [a,a,a,a,b,b,b,b,c,c,c,d,d,d,d,d]
		user_list = [B,D,E,F,A,B,C,F,B,D,E,A,B,C,D,F]

		time_list = range(0,16)

		computed_result = compute_highest_affinity.highest_affinity(site_list, user_list, time_list)
		expected_result = (b, d)

		assert computed_result == expected_result

		print "Successfully passed test4!"

	@patch('__builtin__.open')
	def test5(self, mock_open):

		a = "a"
		b = "b"
		c = "c"
		d = "d"
		e = "e"
		f = "f"
		g = "g"
		h = "h"

		A = "A"
		B = "B"
		C = "C"
		D = "D"
		E = "E"
		F = "F"
		G = "G"
		H = "H"


		site_list = [a,a,b,c,c,c,d,d,e,e,f,f,g]
		user_list = [B,D,C,A,B,C,B,C,C,D,A,B,A]

		time_list = range(0,13)

		computed_result = compute_highest_affinity.highest_affinity(site_list, user_list, time_list)
		expected_result1 = (c, d)
		expected_result2 = (c, f)


		assert computed_result == expected_result1 or computed_result == expected_result2

		print "Successfully passed test5!"
