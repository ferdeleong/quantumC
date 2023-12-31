import cirq
from random import choices
import binascii

encode_gates = {0: cirq.I, 1: cirq.X}
basis_gates = {'Z': cirq.I, 'X': cirq.H}

num_bits = 10
qubits = cirq.NamedQubit.range(num_bits, prefix = 'q')

# Phase 1: Alice Sends

# Step 1: Alice randomly chooses Bits
alice_key = choices([0, 1], k = num_bits)

print('Alice\'s initial key: ', alice_key)

# Step 2: Alice randomly chooses Bases

alice_bases = choices(['Z', 'X'], k = num_bits)

print('\nAlice\'s randomly chosen bases: ', alice_bases)

# Step 3: Alice creates Qubits

alice_circuit = cirq.Circuit()

for bit in range(num_bits):

  encode_value = alice_key[bit]
  encode_gate = encode_gates[encode_value]

  basis_value = alice_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  alice_circuit.append(encode_gate(qubit))
  alice_circuit.append(basis_gate(qubit))
  
# Step 4: Alice sends the Qubits to Bob trough a public quantum channel

# Phase 2: Bob Receives

# Step 5: Bob Randomly Chooses Bases

bob_bases = choices(['Z', 'X'], k = num_bits)
print('Bob\'s randomly chosen bases: ', bob_bases)

bob_circuit = cirq.Circuit()

for bit in range(num_bits):

  basis_value = bob_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  bob_circuit.append(basis_gate(qubit))
  
# Step 6: Bob measures Qubits

bob_circuit.append(cirq.measure(qubits, key = 'bob key'))

print(bob_circuit)

# Step 7: Bob creates a Key

bb84_circuit = alice_circuit + bob_circuit

sim = cirq.Simulator()
results = sim.run(bb84_circuit)
bob_key = results.measurements['bob key'][0]

print('\nBob\'s initial key: ', bob_key)

# Phase 3: Alice and Bob Compare Bases

final_alice_key = []
final_bob_key = []

for bit in range(num_bits):

  if alice_bases[bit] == bob_bases[bit]:
    final_alice_key.append(alice_key[bit])
    final_bob_key.append(bob_key[bit])

print('\nAlice\'s key: ', final_alice_key)
print('Bob\'s key: ', final_bob_key)

# Step 9: Alice and Bob compare the first bits of the key

num_bits_to_compare = int(len(final_alice_key) * .5)
if final_alice_key[0:num_bits_to_compare] == final_bob_key[0:num_bits_to_compare]:
  final_alice_key = final_alice_key[num_bits_to_compare:]
  final_bob_key = final_bob_key[num_bits_to_compare:]

  print('\n\nWe can use our keys!')
  print('Alice Key: ', final_alice_key)
  print('Bob Key: ', final_bob_key)

else:
  print('\n\nEve was listening, we need to use a different channel!')
  
# Part 2: Alice, Bob and Eve's Measure Attack

encode_gates = {0: cirq.I, 1: cirq.X}
basis_gates = {'Z': cirq.I, 'X': cirq.H}

num_bits = 100
qubits = cirq.NamedQubit.range(num_bits, prefix = 'q')

alice_key = choices([0, 1], k = num_bits)

print('Alice\'s initial key: ', alice_key)

alice_bases = choices(['Z', 'X'], k = num_bits)

print('\nAlice\'s randomly chosen bases: ', alice_bases)

alice_circuit = cirq.Circuit()

for bit in range(num_bits):

  encode_value = alice_key[bit]
  encode_gate = encode_gates[encode_value]

  basis_value = alice_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  alice_circuit.append(encode_gate(qubit))
  alice_circuit.append(basis_gate(qubit))
  

eve_circuit = cirq.Circuit()
eve_circuit.append(cirq.measure(qubits, key = 'eve key'))

eve_intercept_circuit = alice_circuit + eve_circuit

sim = cirq.Simulator()
results = sim.run(eve_intercept_circuit)
eve_key = results.measurements['eve key'][0]

print('\nEve\'s initial key: ', eve_key)

alice_circuit = cirq.Circuit()

for bit in range(num_bits):

  encode_value = eve_key[bit]
  encode_gate = encode_gates[encode_value]

  qubit = qubits[bit]
  alice_circuit.append(encode_gate(qubit))

print('\nAlice\'s Phase 1 circuit after Eve\'s interception:\n', alice_circuit)

bob_bases = choices(['Z', 'X'], k = num_bits)
print('Bob\'s randomly chosen bases: ', bob_bases)

bob_circuit = cirq.Circuit()

for bit in range(num_bits):

  basis_value = bob_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  bob_circuit.append(basis_gate(qubit))
  
bob_circuit.append(cirq.measure(qubits, key = 'bob key'))

print(bob_circuit)

bb84_circuit = alice_circuit + bob_circuit

sim = cirq.Simulator()
results = sim.run(bb84_circuit)
bob_key = results.measurements['bob key'][0]

print('\nBob\'s initial key: ', bob_key)

final_alice_key = []
final_bob_key = []
final_eve_key = []

for bit in range(num_bits):

  if alice_bases[bit] == bob_bases[bit]:
    final_alice_key.append(alice_key[bit])
    final_bob_key.append(bob_key[bit])
    final_eve_key.append(eve_key[bit])

print('\nAlice\'s key: ', final_alice_key)
print('Bob\'s key: ', final_bob_key)
print('Eve\'s key: ', final_eve_key)

num_bits_to_compare = int(len(final_alice_key) * .5)
if final_alice_key[0:num_bits_to_compare] == final_bob_key[0:num_bits_to_compare]:
  final_alice_key = final_alice_key[num_bits_to_compare:]
  final_bob_key = final_bob_key[num_bits_to_compare:]
  final_eve_key = final_eve_key[num_bits_to_compare:]

  print('\n\nWe can use our keys!')
  print('Alice Key: ', final_alice_key)
  print('Bob Key: ', final_bob_key)
  print('Eve Key: ', final_eve_key)

else:
  print('\n\nEve was listening, we need to use a different channel!')
  
# Intercept and Resend Attack
  
encode_gates = {0: cirq.I, 1: cirq.X}
basis_gates = {'Z': cirq.I, 'X': cirq.H}

num_bits = 100
qubits = cirq.NamedQubit.range(num_bits, prefix = 'q')

alice_key = choices([0, 1], k = num_bits)

print('Alice\'s initial key: ', alice_key)

alice_bases = choices(['Z', 'X'], k = num_bits)

print('\nAlice\'s randomly chosen bases: ', alice_bases)

alice_circuit = cirq.Circuit()

for bit in range(num_bits):

  encode_value = alice_key[bit]
  encode_gate = encode_gates[encode_value]

  basis_value = alice_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  alice_circuit.append(encode_gate(qubit))
  alice_circuit.append(basis_gate(qubit))

eve_bases = choices(['Z', 'X'], k = num_bits)
print('Eve\'s randomly chosen bases: ', eve_bases)

eve_circuit = cirq.Circuit()

for bit in range(num_bits):

  basis_value = eve_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  eve_circuit.append(basis_gate(qubit))

eve_circuit.append(cirq.measure(qubits, key = 'eve key'))

eve_intercept_circuit = alice_circuit + eve_circuit

sim = cirq.Simulator()
results = sim.run(eve_intercept_circuit)
eve_key = results.measurements['eve key'][0]

print('\nEve\'s initial key: ', eve_key)

alice_circuit = cirq.Circuit()

for bit in range(num_bits):

  encode_value = eve_key[bit]
  encode_gate = encode_gates[encode_value]

  basis_value = eve_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  alice_circuit.append(encode_gate(qubit))
  alice_circuit.append(basis_gate(qubit))

print('\nAlice\'s Phase 1 circuit after Eve\'s interception:\n', alice_circuit)

bob_bases = choices(['Z', 'X'], k = num_bits)
print('Bob\'s randomly chosen bases: ', bob_bases)

bob_circuit = cirq.Circuit()

for bit in range(num_bits):

  basis_value = bob_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  bob_circuit.append(basis_gate(qubit))
  
bob_circuit.append(cirq.measure(qubits, key = 'bob key'))

print(bob_circuit)

bb84_circuit = alice_circuit + bob_circuit

sim = cirq.Simulator()
results = sim.run(bb84_circuit)
bob_key = results.measurements['bob key'][0]

print('\nBob\'s initial key: ', bob_key)

final_alice_key = []
final_bob_key = []
final_eve_key = []

for bit in range(num_bits):

  if alice_bases[bit] == bob_bases[bit]:
    final_alice_key.append(alice_key[bit])
    final_bob_key.append(bob_key[bit])
    final_eve_key.append(eve_key[bit])

print('\nAlice\'s key: ', final_alice_key)
print('Bob\'s key: ', final_bob_key)
print('Eve\'s key: ', final_eve_key)

num_bits_to_compare = int(len(final_alice_key) * .5)
if final_alice_key[0:num_bits_to_compare] == final_bob_key[0:num_bits_to_compare]:
  final_alice_key = final_alice_key[num_bits_to_compare:]
  final_bob_key = final_bob_key[num_bits_to_compare:]
  final_eve_key = final_eve_key[num_bits_to_compare:]

  print('\n\nWe can use our keys!')
  print('Alice Key: ', final_alice_key)
  print('Bob Key: ', final_bob_key)
  print('Eve Key: ', final_eve_key)

else:
  print('\n\nEve was listening, we need to use a different channel!')
  
# Phase 4: 

encode_gates = {0: cirq.I, 1: cirq.X}
basis_gates = {'Z': cirq.I, 'X': cirq.H}

num_bits = 100
qubits = cirq.NamedQubit.range(num_bits, prefix = 'q')

alice_key = choices([0, 1], k = num_bits)

print('Alice\'s initial key: ', alice_key)

alice_bases = choices(['Z', 'X'], k = num_bits)

print('\nAlice\'s randomly chosen bases: ', alice_bases)

alice_circuit = cirq.Circuit()

for bit in range(num_bits):

  encode_value = alice_key[bit]
  encode_gate = encode_gates[encode_value]

  basis_value = alice_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  alice_circuit.append(encode_gate(qubit))
  alice_circuit.append(basis_gate(qubit))
  
eve_qubits = cirq.NamedQubit.range(num_bits, prefix="eve")

for bit in range(num_bits):

  qubit = qubits[bit]
  eve_qubit = eve_qubits[bit]

  alice_circuit.append(cirq.CNOT(qubit, eve_qubit))
  
bob_bases = choices(['Z', 'X'], k = num_bits)
print('Bob\'s randomly chosen bases: ', bob_bases)

bob_circuit = cirq.Circuit()

for bit in range(num_bits):

  basis_value = bob_bases[bit]
  basis_gate = basis_gates[basis_value]

  qubit = qubits[bit]
  bob_circuit.append(basis_gate(qubit))
  
bob_circuit.append(cirq.measure(qubits, key = 'bob key'))

print(bob_circuit)

bb84_circuit = alice_circuit + bob_circuit

sim = cirq.Simulator()
results = sim.run(bb84_circuit)
bob_key = results.measurements['bob key'][0]

print('\nBob\'s initial key: ', bob_key)

basis_value = bob_bases[bit]
basis_gate = basis_gates[basis_value]

qubit = eve_qubits[bit]
bb84_circuit.append(basis_gate(qubit))
bb84_circuit.append(cirq.measure(qubit))

sim = cirq.Simulator()
results = sim.run(bb84_circuit)

final_eve_key.append(results.measurements['eve' + str(bit)][0][0])

print('\nAlice\'s key: ', final_alice_key)
print('Bob\'s key: ', final_bob_key)
print('Eve\'s key: ', final_eve_key)

basis_value = bob_bases[bit]
basis_gate = basis_gates[basis_value]

qubit = eve_qubits[bit]
bb84_circuit.append(basis_gate(qubit))
bb84_circuit.append(cirq.measure(qubit))

sim = cirq.Simulator()
results = sim.run(bb84_circuit)

final_eve_key.append(results.measurements['eve' + str(bit)][0][0])

print('\nAlice\'s key: ', final_alice_key)
print('Bob\'s key: ', final_bob_key)
print('Eve\'s key: ', final_eve_key)

num_bits_to_compare = int(len(final_alice_key) * .5)
if final_alice_key[0:num_bits_to_compare] == final_bob_key[0:num_bits_to_compare]:
  final_alice_key = final_alice_key[num_bits_to_compare:]
  final_bob_key = final_bob_key[num_bits_to_compare:]
  final_eve_key = final_eve_key[num_bits_to_compare:]

  print('\n\nWe can use our keys!')
  print('Alice Key: ', final_alice_key)
  print('Bob Key: ', final_bob_key)
  print('Eve Key: ', final_eve_key)

else:
  print('\n\nEve was listening, we need to use a different channel!')

