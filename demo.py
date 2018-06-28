import World

def main():
	while True:
		agent= World.player
		max_act, max_val = max_Q(agent)
		(agent, a, r, agent_updated)= do_action(max_act)

		max_act, max_val = max_Q(agent_updated)

		World.start_game()
		print ("Sucsess! Score:", max_val)