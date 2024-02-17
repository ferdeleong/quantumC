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