# Copyright 2021 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from variable_repr import VariableRepr, VariableReprSet


class OperatorRepr(Operator):
    """
    The representation of an operator at compile-phase
    """

    def __init__(self, unique_op_name: str, op = None):
        self.op = op
        self.unique_op_name = unique_op_name
        self._inputs = None
        self._outputs = None
        # todo parse op inputs & outputs
    
    @property
    def inputs(self):
        return self._inputs
    
    @inputs.setter
    def inputs(self, value):
        if isinstance(value, list):
            self._inputs = VariableReprSet(value)
        else:
            self._inputs = value
 
    @property
    def outputs(self):
        return self._outputs
    

