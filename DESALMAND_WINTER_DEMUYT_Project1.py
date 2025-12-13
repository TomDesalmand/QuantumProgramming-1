# Project 1: Grover’s algorithm
#
# %%
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator



def initialize_circuit(n):
    qr = QuantumRegister(n, "q")
    cr = ClassicalRegister(n, "c")
    qc = QuantumCircuit(qr, cr)
    qc.h(qr)
    return qc

n = 3
qc = initialize_circuit(n)
qc.draw(output='mpl')
backend = AerSimulator()
compiled = transpile(qc, backend)
result = backend.run(compiled, shots=1024).result()
print(result)



