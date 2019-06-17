def solve_ode_for_t(self, y_0, t_0, t_target, y_prime):
	"""
	Ordinary Differential Equation solver for equations of the form:
		y^{\prime}(t) = p(t)*y(t),
	where t_0 is the starting value in the timescale and
		y_0 = y(t_0)
	is the initial value provided by the user.

	Arguments:
		"y_0" is the initial value assigned to y(t_0) that is used as a starting point to evaluate the ODE.
		"t_0" is the initial value that is considered the starting point in the timescale from which to solve subsequent points.
		t_0 is the value that is plugged into y to determine y_0 via: y_0 = y(t_0).

		"t_target" is the timescale value for which y should be evaluated and returned.

		"y_prime" is the function y'(t) of the ODE y'(t) = p(t)*y(t). 
		NOTE: "y_prime" MUST be defined such that the arguments ("t" and "y") appear in this order: y_prime(t, y).
		If this particular order is not used, then the solve_ode_for_t() function will plug in the wrong values for t and y when solving.
		This means that the solve_ode_for_t() function will (except in specific cases like when t = y) return an incorrect result.

	Other Variables:
		"t_current" is the current value of t. t must be a value in the timescale.

		"y_current" holds the value obtained from y(t_current).

	The function will solve for the next t value until the value of y(t_target) is obtained.
	y(t_target) is then returned.
	Currently, t_target > t_0 is a requirement -- solving for a t_target < t_0 is not supported.

	Note: y(t_0) = y_0
	print("solve_ode_for_t arguments:")
	print("y_0 =", y_0)
	print("t_0 =", t_0)
	print("t_target =", t_target)
	print("")
	
	The following is more validation code -- this is very similar to the validation code in the dIntegral function.
	"""
	t_in_ts = False
	t_0_in_ts = False
	discretePoint = False
	
	for x in self.ts:
		if not isinstance(x, list) and t_target == x:
			t_in_ts = True
			
		if not isinstance(x, list) and t_0 == x: 
			discretePoint = True
			t_0_in_ts = True
		
		if isinstance(x, list) and t_target <= x[1] and t_target >= x[0]:
			t_in_ts = True
		
		if isinstance(x, list) and t_0 < x[1] and t_0 >= x[0]:
			discretePoint = False
			t_0_in_ts = True
			
		if isinstance(x, list) and t_0 == x[1]:
			discretePoint = True
			t_0_in_ts = True
		
		if t_in_ts and t_0_in_ts:                
			break
	
	if t_in_ts and not t_0_in_ts:
		raise Exception("solve_ode_for_t: t_0 is not a value in the timescale.")
	
	if not t_in_ts and t_0_in_ts:
		raise Exception("solve_ode_for_t: t_target is not a value in the timescale.")
	
	if not t_in_ts and not t_0_in_ts:
		raise Exception("solve_ode_for_t: t_0 and t_target are not values in the timescale.")
	
	if t_0 == t_target:
		return y_0
	
	elif t_0 > t_target:
		raise Exception("solve_ode_for_t: t_0 cannot be greater than t_target.")
	
	#----------------------------------------------------------------------------#
	
	t_current = t_0
	y_current = y_0
	
	ODE = integrate.ode(y_prime)
	
	while self.isInTimescale(t_current):# Technically safer than "while True:"
		if discretePoint:      
			"""
			print("Solving right scattered point where:")
			print("t_current =", t_current)
			print("y_current =", y_current)
			print("t_target =", t_target)
			print("y_prime(t_current, y_current) =", y_prime(t_current, y_current))
			print("self.mu(t_current) =", self.mu(t_current))
			print()            
			"""
			y_sigma_of_t_current = y_current + y_prime(t_current, y_current) * self.mu(t_current)
			
			t_next = self.sigma(t_current)
			"""
			print("t_next = self.sigma(t_current) =", t_next)
			print()                
			print("Result:")
			print("y_sigma_of_t_current =", y_sigma_of_t_current)
			print()
			"""                
			if t_target == t_next:
				# print("t_target == t_next -> returning y_sigma_of_t_current\n")
				return y_sigma_of_t_current
			
			if self.isDiscretePoint(t_next):
				discretePoint = True
				# print("[NEXT IS DISCRETE POINT]")
				
			else:
				# print("[NEXT IS NOT DISCRETE POINT]")
				discretePoint = False
			
			t_current = t_next
			y_current = y_sigma_of_t_current                
							
		else:
			"""
			print("Solving right dense point where:")                    
			print("t_current =", t_current)
			print("y_current =", y_current)
			print("t_target =", t_target)
			print()
			"""
			ODE.set_initial_value(y_current, t_current)
			
			if self.isDiscretePoint(t_current):
				raise Exception("t_current is NOT in a list/interval! Something went wrong!")
			
			else:
				interval_of_t_current = self.getCorrespondingInterval(t_current)
				"""
				print("Integration conditions:")
				print("t_current =", t_current)
				print("interval_of_t_current =", interval_of_t_current)
				"""                
				if t_target <= interval_of_t_current[1] and t_target >= interval_of_t_current[0]:
					# print("Integrating to t =", t_target)
					# print()
					ODE_integration_result = ODE.integrate(t_target)
					"""
					print("Result:")
					print("ODE_integration_result =", ODE_integration_result)
					print()
					"""
					return ODE_integration_result
				
				elif t_target > interval_of_t_current[1]:
					# print("Integrating to t =", interval_of_t_current[1])
					# print()
					ODE_integration_result = ODE.integrate(interval_of_t_current[1])
					"""
					print("Result:")
					print("ODE_integration_result =", ODE_integration_result)
					print()
					"""
					t_current = interval_of_t_current[1]
					y_current = ODE_integration_result
					
					# print("[NEXT IS DISCRETE POINT]")
					discretePoint = True

			if not ODE.successful():
				raise Exception("ODE.successful() returned False!");
	

def solve_ode_for_t_with_odeint(self, y_0, t_0, t_target, y_prime, stepSize = 0.0001):
	"""
	This function is another version of the solve_ode_for_t() function.
	It uses scipy.integrate.odeint to integrate over intervals rather than the scipy.integrate.ode method used by the solve_ode_for_t() function.
	In general, it seems to be less accurate than solve_ode_for_t().
	The additional stepSize argument (default value = 0.0001) can be used to somewhat mitigate this inaccuracy. 
	However, even with extremely small step sizes (like stepSize = 0.0000001), solve_ode_for_t() seems to be better.

	NOTE: The scipy.integrate.odeint function requires that the argument function, y_prime(), has its arguments in a particular order.
	The required order is exactly inverse to what is required by the scipy.integrate.ode function -- this has a high potential for user error.
	y_prime for this function must be of the form: y_prime(y, t).
	If y_prime(t, y) is provided, nonsensical results will be returned since the wrong values will be plugged into y and t.

	Note: y(t_0) = y_0
	print("solve_ode_for_t arguments:")
	print("y_0 =", y_0)
	print("t_0 =", t_0)
	print("t_target =", t_target)
	print("")
	
	The following is more validation code -- this is very similar to the validation code in the dIntegral function.
	"""
	t_in_ts = False
	t_0_in_ts = False
	discretePoint = False

	for x in self.ts:
		if not isinstance(x, list) and t_target == x:
			t_in_ts = True

		if not isinstance(x, list) and t_0 == x: 
			discretePoint = True
			t_0_in_ts = True

		if isinstance(x, list) and t_target <= x[1] and t_target >= x[0]:
			t_in_ts = True

		if isinstance(x, list) and t_0 < x[1] and t_0 >= x[0]:
			discretePoint = False
			t_0_in_ts = True

		if isinstance(x, list) and t_0 == x[1]:
			discretePoint = True
			t_0_in_ts = True

		if t_in_ts and t_0_in_ts:                
			break

	if t_in_ts and not t_0_in_ts:
		raise Exception("solve_ode_for_t_with_odeint: t_0 is not a value in the timescale.")

	if not t_in_ts and t_0_in_ts:
		raise Exception("solve_ode_for_t_with_odeint: t_target is not a value in the timescale.")

	if not t_in_ts and not t_0_in_ts:
		raise Exception("solve_ode_for_t_with_odeint: t_0 and t_target are not values in the timescale.")

	if t_0 == t_target:
		return y_0

	elif t_0 > t_target:
		raise Exception("solve_ode_for_t_with_odeint: t_0 cannot be greater than t_target.")

	#----------------------------------------------------------------------------#

	t_current = t_0
	y_current = y_0

	while self.isInTimescale(t_current):
		if discretePoint:
			"""
			print("Solving right scattered point where:")
			print("t_current =", t_current)
			print("y_current =", y_current)
			print("t_target =", t_target)
			print("y_prime(y_current, t_current) =", y_prime(y_current, t_current))
			print("self.mu(t_current) =", self.mu(t_current))
			print()
			"""
			y_sigma_of_t_current = y_current + y_prime(y_current, t_current) * self.mu(t_current)

			t_next = self.sigma(t_current)
			"""
			print("t_next = self.sigma(t_current) =", t_next)
			print()                
			print("Result:")
			print("y_sigma_of_t_current =", y_sigma_of_t_current)
			print()
			"""             
			if t_target == t_next:
				# print("t_target == t_next -> returning y_sigma_of_t_current\n")
				return y_sigma_of_t_current
			
			if self.isDiscretePoint(t_next):
				discretePoint = True
				# print("[NEXT IS DISCRETE POINT]")
				
			else:
				# print("[NEXT IS NOT DISCRETE POINT]")
				discretePoint = False
			
			t_current = t_next
			y_current = y_sigma_of_t_current                
							
		else:
			"""
			print("Solving right dense point where:")                    
			print("t_current =", t_current)
			print("y_current =", y_current)
			print("t_target =", t_target)
			print()
			"""            
			if self.isDiscretePoint(t_current):
				raise Exception("t_current is NOT in a list/interval! Something went wrong!")
			
			else:
				interval_of_t_current = self.getCorrespondingInterval(t_current)
				"""
				print("Integration conditions:")
				print("t_current =", t_current)
				print("interval_of_t_current =", interval_of_t_current)
				"""                
				if t_target <= interval_of_t_current[1] and t_target >= interval_of_t_current[0]:
					# print("Integrating to t =", t_target)
					# print()                                             

					current_interval = np.arange(t_current, t_target + stepSize, stepSize)

					# print(current_interval)
					# print()

					ODE_integration_result = integrate.odeint(y_prime, y_current, current_interval)
					ODE_integration_result = ODE_integration_result[len(ODE_integration_result) - 1]

					# print("Result:")
					# print("ODE_integration_result =", ODE_integration_result)
					# print()

					return ODE_integration_result

				elif t_target > interval_of_t_current[1]:
					# print("Integrating to t =", interval_of_t_current[1])
					# print()

					current_interval = np.arange(t_current, interval_of_t_current[1] + stepSize, stepSize)

					# print(current_interval)
					# print()

					ODE_integration_result = integrate.odeint(y_prime, y_current, current_interval)
					ODE_integration_result = ODE_integration_result[len(ODE_integration_result) - 1]

					# print("Result:")
					# print("ODE_integration_result =", ODE_integration_result)
					# print()

					t_current = interval_of_t_current[1]
					y_current = ODE_integration_result

					# print("[NEXT IS DISCRETE POINT]")
					discretePoint = True


def solve_ode_system_for_t(self, y_0, t_0, t_target, y_prime, stepSize = 0.0001):
	"""
	Ordinary Differential Equation System Solver

	Arguments:
		"y_0" is a list of the initial values assigned to y(t_0). These are used as a starting point from which to evaluate the system.

		"t_0" is the initial value that is considered the starting point in the timescale from which to solve subsequent points.
		Initially, t_0 is the value that is plugged into y to determine y_0 via: y_0 = y(t_0).
	
		"t_target" is the timescale value for which y should be evaluated and returned.
		Since this function solves a system of equations, the result will be a list of values that constitute the results for each of the equations in the system for t_target.

		"y_prime" is the system of equations where each individual equation is of the form y'(t) = p(t)*y(t). 
		NOTE: Since this solver uses the scipy.integrate.odeint function to obtain its result, y_prime MUST be defined with a specific format.
		As an example, for a system of two equations, y_prime would have to defined in the following manner:
 
			def y_prime_vector(vector, t): # Argument order is required by the scipy.integrate.odeint class -- "y_prime_vector(y, vector)" will result in incorrect results
				x, y = vector # Extract and store the first item from "vector" into x and the second item into y

				dt_vector = [x*t, y*t*t] # Define the system of equations

				return dt_vector # Return the system

	NOTE: If the number of items in y_0 is not the same as the number of equations in y_prime, then this solver will fail.

	Note: y(t_0) = y_0
	print("solve_ode_for_t arguments:")
	print("y_0 =", y_0)
	print("t_0 =", t_0)
	print("t_target =", t_target)
	print("")

	The following is more validation code -- this is very similar to the validation code in the dIntegral function.
	"""
	t_in_ts = False
	t_0_in_ts = False
	discretePoint = False

	for x in self.ts:
		if not isinstance(x, list) and t_target == x:
			t_in_ts = True

		if not isinstance(x, list) and t_0 == x: 
			discretePoint = True
			t_0_in_ts = True

		if isinstance(x, list) and t_target <= x[1] and t_target >= x[0]:
			t_in_ts = True

		if isinstance(x, list) and t_0 < x[1] and t_0 >= x[0]:
			discretePoint = False
			t_0_in_ts = True

		if isinstance(x, list) and t_0 == x[1]:
			discretePoint = True
			t_0_in_ts = True

		if t_in_ts and t_0_in_ts:                
			break

	if t_in_ts and not t_0_in_ts:
		raise Exception("solve_ode_system_for_t: t_0 is not a value in the timescale.")

	if not t_in_ts and t_0_in_ts:
		raise Exception("solve_ode_system_for_t: t_target is not a value in the timescale.")

	if not t_in_ts and not t_0_in_ts:
		raise Exception("solve_ode_system_for_t: t_0 and t_target are not values in the timescale.")

	if t_0 == t_target:
		return y_0

	elif t_0 > t_target:
		raise Exception("solve_ode_system_for_t: t_0 cannot be greater than t_target.")

	#----------------------------------------------------------------------------#

	t_current = t_0
	y_current = y_0

	while self.isInTimescale(t_current):
		if discretePoint:
			"""
			print("Solving right scattered point where:")
			print("t_current =", t_current)
			print("y_current =", y_current)
			print("t_target =", t_target)
			print("y_prime(y_current, t_current) =", y_prime(y_current, t_current))
			print("self.mu(t_current) =", self.mu(t_current))
			print()
			"""                
			#------------------------------#
			
			# print("y_prime(y_current, t_current) =", y_prime(y_current, t_current), "self.mu(t_current) =", self.mu(t_current))
			
			temp1 = list(map(lambda x: x * self.mu(t_current), y_prime(y_current, t_current)))
				 
			# print("y_current:", y_current, "temp1:", temp1)
			
			temp2 = list(map(lambda x, y: x + y, y_current, temp1))
			
			# print("temp2 =", temp2)
			
			y_sigma_of_t_current = temp2                
			
			#------------------------------#
				
			t_next = self.sigma(t_current)
			"""
			print("t_next = self.sigma(t_current) =", t_next)
			print()                
			print("Result:")
			print("y_sigma_of_t_current =", y_sigma_of_t_current)
			print()
			"""                
			if t_target == t_next:
				# print("t_target == t_next -> returning y_sigma_of_t_current\n")
				return y_sigma_of_t_current

			if self.isDiscretePoint(t_next):
				discretePoint = True
				# print("[NEXT IS DISCRETE POINT]")

			else:
				# print("[NEXT IS NOT DISCRETE POINT]")
				discretePoint = False

			t_current = t_next
			y_current = y_sigma_of_t_current                

		else:
			"""
			print("Solving right dense point where:")                    
			print("t_current =", t_current)
			print("y_current =", y_current)
			print("t_target =", t_target)
			print()
			""" 
			if self.isDiscretePoint(t_current):
				raise Exception("t_current is NOT in a list/interval! Something went wrong!")

			else:
				interval_of_t_current = self.getCorrespondingInterval(t_current)

				# print("Integration conditions:")
				# print("t_current =", t_current)
				# print("interval_of_t_current =", interval_of_t_current)

				if t_target <= interval_of_t_current[1] and t_target >= interval_of_t_current[0]:
					# print("Integrating to t =", t_target)
					# print()                                             

					current_interval = np.arange(t_current, t_target + stepSize, stepSize)

					# print(current_interval)
					# print()

					ODE_integration_result = integrate.odeint(y_prime, y_current, current_interval)

					# print("Result:")
					# print("ODE_integration_result =", ODE_integration_result)
					# print()

					ODE_integration_result = ODE_integration_result[len(ODE_integration_result) - 1]

					return ODE_integration_result

				elif t_target > interval_of_t_current[1]:
					# print("Integrating to t =", interval_of_t_current[1])
					# print()

					current_interval = np.arange(t_current, interval_of_t_current[1] + stepSize, stepSize)

					# print(current_interval)
					# print()

					ODE_integration_result = integrate.odeint(y_prime, y_current, current_interval)                        

					# print("Result:")
					# print("ODE_integration_result =", ODE_integration_result)
					# print()

					ODE_integration_result = ODE_integration_result[len(ODE_integration_result) - 1]

					t_current = interval_of_t_current[1]
					y_current = ODE_integration_result

					# print("[NEXT IS DISCRETE POINT]")
					discretePoint = True


	def solve_dde_for_t(self, y_0, t_0, t_target, y_prime, y_prime_jitcdde, delay_function, max_delay, past_function, stepSize=0.01, times_of_interest=None, c_backend=False):
		"""
		Delay Differential Equation Solver (currently unfinished)
		Note: make sure that t_0 works with times_of_interest
		"""
		print("solve_ode_for_t arguments:")
		print("y_0 =", y_0)
		print("t_0 =", t_0)        
		print("t_target =", t_target)
		print("max_delay =", max_delay)
		print("past_function =", past_function)
		print("")

		# The following is more validation code -- this is very similar to the validation code in the dIntegral function.
		#----------------------------------------------------------------------------#

		t_in_ts = False
		t_0_in_ts = False
		discretePoint = False

		for x in self.ts:
			if not isinstance(x, list) and t_target == x:
				t_in_ts = True

			if not isinstance(x, list) and t_0 == x: 
				discretePoint = True
				t_0_in_ts = True

			if isinstance(x, list) and t_target <= x[1] and t_target >= x[0]:
				t_in_ts = True

			if isinstance(x, list) and t_0 < x[1] and t_0 >= x[0]:
				discretePoint = False
				t_0_in_ts = True

			if isinstance(x, list) and t_0 == x[1]:
				discretePoint = True
				t_0_in_ts = True

			if t_in_ts and t_0_in_ts:                
				break

		if t_in_ts and not t_0_in_ts:
			raise Exception("solve_dde_for_t: t_0 is not a value in the timescale.")

		if not t_in_ts and t_0_in_ts:
			raise Exception("solve_dde_for_t: t_target is not a value in the timescale.")

		if not t_in_ts and not t_0_in_ts:
			raise Exception("solve_dde_for_t: t_0 and t_target are not values in the timescale.")

		if t_0 == t_target:
			return y_0

		elif t_0 > t_target:
			raise Exception("solve_dde_for_t: t_0 cannot be greater than t_target.")

		#----------------------------------------------------------------------------#

		t_current = t_0
		y_current = y_0

		all_results = []

		past_points = []

		# if times_of_interest == None:
			# times_of_interest = [t_0]

		# else:
			# times_of_interest.append([t_0])

		DDE = self.initializeJiTCDDE(y_prime_jitcdde, past_function, max_delay, times_of_interest, c_backend)

		while self.isInTimescale(t_current):
			if discretePoint:               
				print("Solving right scattered point where:")
				print("t_current =", t_current)
				print("y_current =", y_current)
				print("t_target =", t_target)
				print("delay_function(t_current):", delay_function(t_current))
				print("y_prime(t_current, y_current) =", y_prime(t_current, y_current))
				print("y_prime(delay_function(t_current), y_current) =", y_prime(delay_function(t_current), y_current))
				print("self.mu(t_current) =", self.mu(t_current))
				print()            

				#--------#
				# y_sigma_of_t_current = y_current + y_prime(t_current, y_current) * self.mu(t_current)

				# t_next = self.sigma(t_current)                
				#--------#

				delayed_t_current = delay_function(t_current)

				if delayed_t_current > t_current:
					raise Exception("delayed_t_current > t_current")

				if self.isInTimescaleWithError(delayed_t_current):
					print("delayed_t_current = " + str(delayed_t_current) + " is in timescale")

				else:
					# print("************************** delayed_t_current = " + str(delayed_t_current) + " is NOT in timescale **************************")
					raise Exception("delayed_t_current = " + str(delayed_t_current) + " is NOT in timescale")

				print()

				y_sigma_of_t_current = y_current + y_prime(delayed_t_current, y_current) * self.mu(t_current)

				t_next = self.sigma(t_current)     

				print("t_next = self.sigma(t_current) =", t_next)
				print()                
				print("Result:")
				print("y_sigma_of_t_current =", y_sigma_of_t_current)
				print()

				all_results.append(y_sigma_of_t_current)

				if t_target == t_next:
					print("t_target == t_next -> returning y_sigma_of_t_current\n")
					# return y_sigma_of_t_current
					return all_results

				if self.isDiscretePoint(t_next):
					discretePoint = True
					print("[NEXT IS DISCRETE POINT]")
					print()

				else:
					print("[NEXT IS NOT DISCRETE POINT]")
					print()                    
					discretePoint = False

				past_point = [t_current, [y_current], [y_sigma_of_t_current]]

				past_points.append(past_point)

				t_current = t_next
				y_current = y_sigma_of_t_current

			else:
				print("Solving right dense point where:")                    
				print("t_current =", t_current)
				print("y_current =", y_current)
				print("t_target =", t_target)
				print()

				if self.isDiscretePoint(t_current):
					raise Exception("t_current is NOT in a list/interval! Something went wrong!")

				else:
					interval_of_t_current = self.getCorrespondingInterval(t_current)

					print("Integration conditions:")
					print("t_current =", t_current)
					print("interval_of_t_current =", interval_of_t_current)

					if t_target <= interval_of_t_current[1] and t_target >= interval_of_t_current[0]:
						print("Integrating to t =", t_target)
						print()                                             

						current_interval = np.arange(t_current, t_target + stepSize, stepSize)

						print(current_interval)
						print()

						DDE_integration_result = []                        
						DDE = self.updateJiTCDDE(DDE, past_points)                      
						past_points = []

						for time in current_interval:
							if time <= t_target:
								DDE_integration_result = DDE.integrate_blindly(time)
								all_results.append(DDE_integration_result[0])
								print("time =", time, " |  integration_result =", DDE_integration_result)

						# if t_target != DDE.t:
							# raise Exception("t_target != DDE.t: t_target =", t_target, "| DDE.t =", DDE.t)

						#---Testing-Code-Start---#

						t_current = t_target # The following should hold barring accuracy limitations: t_target != DDE.t
						y_current = DDE_integration_result[0]

						# print("t_current is:", t_current)
						# print("DDE.t is:", DDE.t)
						# print("y_current is:", y_current)   
						# print()

						#---Testing-Code-End---#

						print("Result:")
						print("time =", t_current, "| DDE_integration_result =", DDE_integration_result)
						print()

						# return DDE_integration_result[len(DDE_integration_result) - 1]
						return all_results

					elif t_target > interval_of_t_current[1]:
						print("Integrating to t =", interval_of_t_current[1])
						print()

						current_interval = np.arange(t_current, interval_of_t_current[1] + stepSize, stepSize)

						print(current_interval)
						print()

						DDE_integration_result = []                        
						DDE = self.updateJiTCDDE(DDE, past_points)                        
						past_points = []

						for time in current_interval:
							if time <= t_target:
								DDE_integration_result = DDE.integrate_blindly(time)
								all_results.append(DDE_integration_result[0])
								print("time =", time, " |  integration_result =", DDE_integration_result)

						# if interval_of_t_current[1] != DDE.t:
							# raise Exception("interval_of_t_current[1] != DDE.t: interval_of_t_current[1] =", interval_of_t_current[1], "| DDE.t =", DDE.t)

						t_current = interval_of_t_current[1] # The following should hold barring accuracy limitations: interval_of_t_current[1] == DDE.t
						y_current = DDE_integration_result[0]

						# print("t_current is:", t_current)
						# print("DDE.t is:", DDE.t)
						# print("y_current is:", y_current)
						# print()

						print("Result:")
						print("time =", t_current, "| DDE_integration_result =", DDE_integration_result)
						print()

						print("[NEXT IS DISCRETE POINT]")
						print()                        
						discretePoint = True


def initializeJiTCDDE(self, y_prime_jitcdde, past_function, arg_max_delay, arg_times_of_interest, c_backend):
	"""
	Utility function to avoid repeated code.
	Sets up the "jitcdde" class to integrate over intervals.
	For more information see: https://jitcdde.readthedocs.io/en/stable/#the-main-class
	This function is used by the solve_dde_for_t() function.
	"""
	DDE = jitcdde.jitcdde(y_prime_jitcdde, max_delay=arg_max_delay)                  
	DDE.past_from_function(past_function, times_of_interest=arg_times_of_interest)

	if c_backend == False:
		DDE.generate_lambdas()  

	print()

	# print("state:")
	# x = DDE.get_state()

	# for y in x:
		# print(y)

	# print()

	return DDE


def updateJiTCDDE(self, DDE, past_points):
	"""
	Utility function to avoid repeated code.
	Updates the past points of the "jitcdde" class.
	For more information see: https://jitcdde.readthedocs.io/en/stable/#_jitcdde.jitcdde.add_past_point
	This function is used by the solve_dde_for_t() function.
	"""
	# print("state:")
	# x = DDE.get_state()

	# for y in x:
		# print(y)
	# print()

	print("past points:")
	for past_point in past_points:
		time = past_point[0]
		state = past_point[1]
		derivative = past_point[2]            

		print("time:", time, "| state:", state, "| derivative:", derivative)            

		DDE.add_past_point(time, state, derivative)

	print()

	return DDE 


def isInTimescaleWithError(self, t, error=0.000000000000001):
	"""
	Utility function to avoid repeated code.
	Simply checks whether the argument, t, is close to a value in the timescale.
	What "close" means is defined by the argument "error".
	If t is close to a value in the timescale, it will return True. Otherwise, it will return False.
	"""
	for ts_item in self.ts:
		if not isinstance(ts_item, list):
			if ts_item >= (t - error) and ts_item <= (t + error):
				return True

		elif isinstance(ts_item, list):
			if (t >= (ts_item[0] - error) and t <= (ts_item[1] + error)):
				return True

	return False


def isInTimescale(self, t):
	"""
	Utility function to avoid repeated code.
	Simply checks whether the argument, t, is a value in the timescale.
	If t is in the timescale, it will return True. Otherwise, it will return False.
	"""
	for ts_item in self.ts:
		if not isinstance(ts_item, list) and ts_item == t:
			return True

		elif isinstance(ts_item, list) and  (t >= ts_item[0] and t <= ts_item[1]):
			return True
	
	return False


def isDiscretePoint(self, t):
	"""
	Utility function to avoid repeated code.
	Simply checks whether the argument, t, is a discrete point or in an interval of the timescale.
	"""
	for x in self.ts:
		if not isinstance(x, list) and t == x:
			return True           
		
		if isinstance(x, list) and t <= x[1] and t >= x[0]:
			return False
	
	raise Exception("isDiscretePoint(): t was neither a discrete point nor in an interval!")


def getCorrespondingInterval(self, t):
	"""
	Utility function to avoid repeated code.
	Returns the interval in which t is located for the current timescale.
	Will raise an exception if t is not in an interval.
	"""
	for x in self.ts:
		if isinstance(x, list) and t <= x[1] and t >= x[0]:
			return x
	
	raise Exception("getCorrespondingInterval(): t not in an interval!") 