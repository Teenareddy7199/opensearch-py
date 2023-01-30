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

PY3 = sys.version_info[0] == 3


class AWSV4SignerAsyncAuth:
    """
    AWS V4 Request Signer for Async Requests.
    """

    def __init__(self, credentials, region, service="es"):  # type: ignore
        if not credentials:
            raise ValueError("Credentials cannot be empty")
        self.credentials = credentials

        if not region:
            raise ValueError("Region cannot be empty")
        self.region = region

        if not service:
            raise ValueError("Service name cannot be empty")
        self.service = service

    def __call__(self, method, url, query_string, body):  # type: ignore
        return self._sign_request(method, url, query_string, body)  # type: ignore

    def _sign_request(self, method, url, query_string, body):
        """
        This method helps in signing the request by injecting the required headers.
        :param prepared_request: unsigned headers
        :return: signed headers
        """

        from botocore.auth import SigV4Auth
        from botocore.awsrequest import AWSRequest

        # create an AWS request object and sign it using SigV4Auth
        aws_request = AWSRequest(
            method=method,
            url=url,
            data=body,
        )

        sig_v4_auth = SigV4Auth(self.credentials, self.service, self.region)
        sig_v4_auth.add_auth(aws_request)
        aws_request.headers["X-Amz-Content-SHA256"] = sig_v4_auth.payload(aws_request)

        # copy the headers from AWS request object into the prepared_request
        return dict(aws_request.headers.items())
