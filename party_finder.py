import itertools


dislikes_rings = [[
	'Adonja',
	'Sigismund',
	'Donavan',
	'Leslie',
	'Kassim',
	'Kaverra',
	'Ediz',
	'Lethaldiran',
	'Riva',
	'Julia',
	'Sara the Fox',
	'Alyssa',
	'Sir Roland',
	'Sir Alistair',
	'Sir Jocelyn',
	'Diev',
],[
	'Ansen',
	'Boadice',
	'Sir Rayne',
	'Frederick'
]]

likes = [
	['Adonja', 'Ansen'],
	['Sigismund', 'Sara the Fox'],
	['Donavan', 'Frederick'],
	['Diev', 'Leslie'],
	['Kassim', 'Riva'],
	['Kaverra', 'Sir Roland'],
	['Ediz', 'Sir Rayne'],
	['Lethaldiran', 'Julia'],
	['Alyssa', 'Sir Alistair'],
	['Sir Jocelyn', 'Boadice'],
]

likes = {**{k:v for (k, v) in likes}, **{v:k for (k, v) in likes}}

for party_size in reversed(range(8, 20)):
	print('-'*30)
	print(f'PARTY SIZE : {party_size}')
	print('-'*30)
	for party in itertools.combinations(dislikes_rings[0] + dislikes_rings[1], party_size):
		for character in party:
			dislike_ring = []
			if character in dislikes_rings[0]:
				dislike_ring = dislikes_rings[0]
			else:
				dislike_ring = dislikes_rings[1]
			
			character_mood = 0
			character_index = dislike_ring.index(character)
			if dislike_ring[(character_index-1) % len(dislike_ring)] in party:
				break
				character_mood -= 1
			if dislike_ring[(character_index+1) % len(dislike_ring)] in party:
				break
				character_mood -= 1

			if likes[character] in party:
				character_mood += 1

			if character_mood < 0:
				break

		else:
			print(' - '.join(party))


