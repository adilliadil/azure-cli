# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_vm_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.compute import ComputeManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   ComputeManagementClient)


def cf_ssh_public_key(cli_ctx, *_):
    return cf_vm_cl(cli_ctx).ssh_public_keys