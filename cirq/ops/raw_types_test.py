# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import cirq


def test_gate_calls_validate():
    class ValiGate(cirq.Gate):
        def validate_args(self, qubits):
            if len(qubits) == 3:
                raise ValueError()

    g = ValiGate()
    q00 = cirq.QubitId()
    q01 = cirq.QubitId()
    q10 = cirq.QubitId()

    _ = g.on(q00)
    _ = g.on(q01)
    _ = g.on(q00, q10)
    with pytest.raises(ValueError):
        _ = g.on(q00, q10, q01)

    _ = g(q00)
    _ = g(q00, q10)
    with pytest.raises(ValueError):
        _ = g(q10, q01, q00)


def test_named_qubit_str():
    q = cirq.NamedQubit('a')
    assert q.name == 'a'
    assert str(q) == 'a'

def test_indexed_qubit_str():
    q = cirq.IndexedQubit(12)
    assert q.index== 12
    assert str(q) == str(12)

# Python 2 gives a different repr due to unicode strings being prefixed with u.
@cirq.testing.only_test_in_python3
def test_named_qubit_repr():
    q = cirq.NamedQubit('a')
    assert repr(q) == "NamedQubit('a')"

@cirq.testing.only_test_in_python3
def test_indexed_qubit_repr():
    q = cirq.IndexedQubit(13)
    assert repr(q) == "IndexedQubit(13)"
