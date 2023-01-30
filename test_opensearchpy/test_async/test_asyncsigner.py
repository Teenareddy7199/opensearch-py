# -*- coding: utf-8 -*-
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


import sys

import pytest

from ..test_cases import TestCase

pytestmark = pytest.mark.asyncio


class TestAsyncSigner(TestCase):
    @pytest.mark.skipif(
        sys.version_info < (3, 6), reason="AWSV4SignerAsyncAuth requires python3.6+"
    )
    async def test_aws_signer_async_as_http_auth(self):
        region = "us-west-2"

        from newopensearchpy.helpers.asyncsigner import AWSV4SignerAsyncAuth

        auth = AWSV4SignerAsyncAuth(self.mock_session(), region)
        headers = auth("GET", "http://localhost")
        self.assertIn("Authorization", headers)
        self.assertIn("X-Amz-Date", headers)
        self.assertIn("X-Amz-Security-Token", headers)

    @pytest.mark.skipif(
        sys.version_info < (3, 6), reason="AWSV4SignerAuth requires python3.6+"
    )
    async def test_aws_signer_async_when_region_is_null(self):
        session = self.mock_session()

        from newopensearchpy.helpers.asyncsigner import AWSV4SignerAsyncAuth

        with pytest.raises(ValueError) as e:
            AWSV4SignerAsyncAuth(session, None)
        assert str(e.value) == "Region cannot be empty"

        with pytest.raises(ValueError) as e:
            AWSV4SignerAsyncAuth(session, "")
        assert str(e.value) == "Region cannot be empty"

    @pytest.mark.skipif(
        sys.version_info < (3, 6), reason="AWSV4SignerAuth requires python3.6+"
    )
    async def test_aws_signer_async_when_credentials_is_null(self):
        region = "us-west-1"

        from newopensearchpy.helpers.asyncsigner import AWSV4SignerAsyncAuth

        with pytest.raises(ValueError) as e:
            AWSV4SignerAsyncAuth(None, region)
        assert str(e.value) == "Credentials cannot be empty"

        with pytest.raises(ValueError) as e:
            assert str(e.value) == "Credentials cannot be empty"

    @pytest.mark.skipif(
        sys.version_info < (3, 6), reason="AWSV4SignerAsyncAuth requires python3.6+"
    )
    async def test_aws_signer_async_when_service_is_specified(self):
        region = "us-west-2"
        service = "aoss"

        from newopensearchpy.helpers.asyncsigner import AWSV4SignerAsyncAuth

        auth = AWSV4SignerAsyncAuth(self.mock_session(), region, service)
        headers = auth("GET", "http://localhost")
        self.assertIn("Authorization", headers)
        self.assertIn("X-Amz-Date", headers)
        self.assertIn("X-Amz-Security-Token", headers)
        self.assertIn("X-Amz-Content-SHA256", headers)
