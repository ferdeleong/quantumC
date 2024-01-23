qubit = cirq.NamedQubit("q0")
my_circuit = cirq.Circuit()
my_circuit.append(cirq.measure(qubit) )
print(my_circuit)

sim = cirq.Simulator()
result = sim.run(my_circuit)
result


qubit = cirq.NamedQubit("q0")
my_circuit = cirq.Circuit( )
my_circuit.append(cirq.H(qubit))
print(my_circuit)

state_vector = cirq.final_state_vector(my_circuit)
ket = cirq.dirac_notation( state_vector=state_vector )

print( state_vector, ket )
bloch_sphere.BlochSphere( state_vector=state_vector )

my_circuit.append(cirq.measure(qubit))
my_circuit

simulator = cirq.Simulator()
result = simulator.run(my_circuit, repetitions=10)
print( result )

my_qubit = cirq.NamedQubit("q0")
my_circuit = cirq.Circuit()
my_circuit.append(cirq.X(my_qubit))
my_circuit.append(cirq.H(my_qubit))
my_circuit

state_vector = cirq.final_state_vector(my_circuit)
ket = cirq.dirac_notation( state_vector=state_vector )


cirq_web.bloch_sphere.BlochSphere( state_vector=state_vector )
print( state_vector, ket )

cirq_web.bloch_sphere.BlochSphere( state_vector=state_vector )

my_circuit.append(cirq.measure(my_qubit))
my_circuit

simulator = cirq.Simulator()
result = simulator.run(my_circuit, repetitions=10)
print( result )