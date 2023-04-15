def split_data(data, interval):
	current_time = 0
	start_time = data[0][0]
	part = []
	current_part = []

	for i in range(len(data)):
		current_time = data[i][0]
		if (float(current_time) - float(start_time)) <= float(interval):
			current_part.append(data[i])
		else:
			start_time = current_time
			part.append(current_part)
			current_part = []

	return part