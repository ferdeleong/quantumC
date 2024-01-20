vec = [1/np.sqrt(2), 1/np.sqrt(2)]

# @title
num_qubits = 4
qubits = cirq.NamedQubit.range(num_qubits, prefix = 'q')
circuit = cirq.Circuit()
circuit.append(cirq.H(qubits[0]))

for i in range(num_qubits - 1):
  circuit.append(cirq.CNOT(qubits[i], qubits[i+1]))

print(circuit)

# @title
my_qubits = cirq.NamedQubit.range(4, prefix="q")
my_circuit = cirq.Circuit()
my_gates = [cirq.X, cirq.H, cirq.X, cirq.H]

for i in range(4):
  gate = my_gates[i]
  my_circuit.append(gate(my_qubits[i]))

my_circuit


my_qubits = cirq.NamedQubit.range(3, prefix="q")
my_circuit = cirq.Circuit()

my_circuit.append(cirq.H.on_each(my_qubits))
my_circuit