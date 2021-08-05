#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "d4cabddb-98a7-4bc1-87a3-31ac893f6826")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ElizaHuangTaigidian2021")
    # CONNECTION_NAME = os.environ.get("ConnectionName", "")
    # SERVICE_URL=os.environ.get("Service_url", "https://smba.trafficmanager.net/apac/")

# https://azure-bot-framework.herokuapp.com/api/messages