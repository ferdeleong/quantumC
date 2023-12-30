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

