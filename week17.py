# Create qubits and circuit
qubits = cirq.NamedQubit.range(2, prefix = 'q')
circuit = cirq.Circuit()

circuit.append(cirq.H(qubits[0]))
circuit.append(cirq.CNOT(qubits[0], qubits[1]))
circuit.append(cirq.measure(qubits))

# Create a simulator that uses the noise model
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)

# Get the results
hist = cirq.plot_state_histogram(result, plt.subplot(), title = 'Qubit States', xlabel = 'States', ylabel = 'Occurrences', tick_label=binary_labels(2))

plt.show()


# 1. PREPARE QUBITS
#===================
# Create qubits
q0 = cirq.NamedQubit('state 0')
q1 = cirq.NamedQubit('state 1')
ancilla = cirq.NamedQubit('anc')

# Prepare the given states
circuit_0 = cirq.Circuit()
circuit_0.append(cirq.I(q0))

circuit_1 = cirq.Circuit()
circuit_1.append(cirq.I(q1))


noise = cirq.depolarize(# COMPLETE THIS CODE
circuit = circuit_0 + circuit_1.with_noise(# COMPLETE THIS CODE



# 2. SWAP TEST CIRCUIT
#======================
# Put ancilla in superposition
circuit.append(cirq.H(ancilla))

# Controlled-Swap controlled by ancilla and targeting q0 and q1
circuit.append(cirq.CSWAP(ancilla, q0, q1))

# Apply an H gate on the ancilla.
circuit.append(cirq.H(ancilla))

# Measure ancilla
circuit.append(cirq.measure(ancilla))



# 3. RUN CIRCUIT
#================
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)



# 4. CALCULATE FIDELITY
#=======================
prob_0 = np.sum(result.measurements['anc']) / len(result.measurements['anc'])
fidelity = 1 - 2*prob_0
fidelity