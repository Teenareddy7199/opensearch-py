# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
from typing import Any, Union

from ..client.utils import NamespacedClient as NamespacedClient

class AlertingClient(NamespacedClient):
    def search_monitor(
        self, body: Any, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def get_monitor(
        self,
        monitor_id: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def run_monitor(
        self,
        monitor_id: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def create_monitor(
        self,
        body: Union[Any, None] = ...,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def update_monitor(
        self,
        monitor_id: Any,
        body: Union[Any, None] = ...,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def delete_monitor(
        self,
        monitor_id: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def get_destination(
        self,
        destination_id: Union[Any, None] = ...,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def create_destination(
        self,
        body: Union[Any, None] = ...,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def update_destination(
        self,
        destination_id: Any,
        body: Union[Any, None] = ...,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def delete_destination(
        self,
        destination_id: Any,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
    def get_alerts(
        self, params: Union[Any, None] = ..., headers: Union[Any, None] = ...
    ) -> Union[bool, Any]: ...
    def acknowledge_alert(
        self,
        monitor_id: Any,
        body: Union[Any, None] = ...,
        params: Union[Any, None] = ...,
        headers: Union[Any, None] = ...,
    ) -> Union[bool, Any]: ...
