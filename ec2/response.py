{
    'Groups': [
        {
            'GroupName': 'string',
            'GroupId': 'string'
        },
    ],
    'Instances': [
        {
            'AmiLaunchIndex': 123,
            'ImageId': 'string',
            'InstanceId': 'string',
            'InstanceType': 'a1.medium...',
            'KernelId': 'string',
            'KeyName': 'string',
            'LaunchTime': datetime(2015, 1, 1),
            'Monitoring': {
                'State': 'disabled'|'disabling'|'enabled'|'pending'
            },
            'Placement': {
                'AvailabilityZone': 'string',
                'Affinity': 'string',
                'GroupName': 'string',
                'PartitionNumber': 123,
                'HostId': 'string',
                'Tenancy': 'default'|'dedicated'|'host',
                'SpreadDomain': 'string',
                'HostResourceGroupArn': 'string',
                'GroupId': 'string'
            },
            'Platform': 'Windows',
            'PrivateDnsName': 'string',
            'PrivateIpAddress': 'string',
            'ProductCodes': [
                {
                    'ProductCodeId': 'string',
                    'ProductCodeType': 'devpay'|'marketplace'
                },
            ],
            'PublicDnsName': 'string',
            'PublicIpAddress': 'string',
            'RamdiskId': 'string',
            'State': {
                'Code': 123,
                'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
            },
            'StateTransitionReason': 'string',
            'SubnetId': 'string',
            'VpcId': 'string',
            'Architecture': 'i386'|'x86_64'|'arm64'|'x86_64_mac'|'arm64_mac',
            'BlockDeviceMappings': [
                {
                    'DeviceName': 'string',
                    'Ebs': {
                        'AttachTime': datetime(2015, 1, 1),
                        'DeleteOnTermination': True|False,
                        'Status': 'attaching'|'attached'|'detaching'|'detached',
                        'VolumeId': 'string',
                        'AssociatedResource': 'string',
                        'VolumeOwnerId': 'string'
                    }
                },
            ],
            'ClientToken': 'string',
            'EbsOptimized': True|False,
            'EnaSupport': True|False,
            'Hypervisor': 'ovm'|'xen',
            'IamInstanceProfile': {
                'Arn': 'string',
                'Id': 'string'
            },
            'InstanceLifecycle': 'spot'|'scheduled'|'capacity-block',
            'ElasticGpuAssociations': [
                {
                    'ElasticGpuId': 'string',
                    'ElasticGpuAssociationId': 'string',
                    'ElasticGpuAssociationState': 'string',
                    'ElasticGpuAssociationTime': 'string'
                },
            ],
            'ElasticInferenceAcceleratorAssociations': [
                {
                    'ElasticInferenceAcceleratorArn': 'string',
                    'ElasticInferenceAcceleratorAssociationId': 'string',
                    'ElasticInferenceAcceleratorAssociationState': 'string',
                    'ElasticInferenceAcceleratorAssociationTime': datetime(2015, 1, 1)
                },
            ],
            'NetworkInterfaces': [
                {
                    'Association': {
                        'CarrierIp': 'string',
                        'CustomerOwnedIp': 'string',
                        'IpOwnerId': 'string',
                        'PublicDnsName': 'string',
                        'PublicIp': 'string'
                    },
                    'Attachment': {
                        'AttachTime': datetime(2015, 1, 1),
                        'AttachmentId': 'string',
                        'DeleteOnTermination': True|False,
                        'DeviceIndex': 123,
                        'Status': 'attaching'|'attached'|'detaching'|'detached',
                        'NetworkCardIndex': 123,
                        'EnaSrdSpecification': {
                            'EnaSrdEnabled': True|False,
                            'EnaSrdUdpSpecification': {
                                'EnaSrdUdpEnabled': True|False
                            }
                        }
                    },
                    'Description': 'string',
                    'Groups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'Ipv6Addresses': [
                        {
                            'Ipv6Address': 'string',
                            'IsPrimaryIpv6': True|False
                        },
                    ],
                    'MacAddress': 'string',
                    'NetworkInterfaceId': 'string',
                    'OwnerId': 'string',
                    'PrivateDnsName': 'string',
                    'PrivateIpAddress': 'string',
                    'PrivateIpAddresses': [
                        {
                            'Association': {
                                'CarrierIp': 'string',
                                'CustomerOwnedIp': 'string',
                                'IpOwnerId': 'string',
                                'PublicDnsName': 'string',
                                'PublicIp': 'string'
                            },
                            'Primary': True|False,
                            'PrivateDnsName': 'string',
                            'PrivateIpAddress': 'string'
                        },
                    ],
                    'SourceDestCheck': True|False,
                    'Status': 'available'|'associated'|'attaching'|'in-use'|'detaching',
                    'SubnetId': 'string',
                    'VpcId': 'string',
                    'InterfaceType': 'string',
                    'Ipv4Prefixes': [
                        {
                            'Ipv4Prefix': 'string'
                        },
                    ],
                    'Ipv6Prefixes': [
                        {
                            'Ipv6Prefix': 'string'
                        },
                    ],
                    'ConnectionTrackingConfiguration': {
                        'TcpEstablishedTimeout': 123,
                        'UdpStreamTimeout': 123,
                        'UdpTimeout': 123
                    }
                },
            ],
            'OutpostArn': 'string',
            'RootDeviceName': 'string',
            'RootDeviceType': 'ebs'|'instance-store',
            'SecurityGroups': [
                {
                    'GroupName': 'string',
                    'GroupId': 'string'
                },
            ],
            'SourceDestCheck': True|False,
            'SpotInstanceRequestId': 'string',
            'SriovNetSupport': 'string',
            'StateReason': {
                'Code': 'string',
                'Message': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'VirtualizationType': 'hvm'|'paravirtual',
            'CpuOptions': {
                'CoreCount': 123,
                'ThreadsPerCore': 123,
                'AmdSevSnp': 'enabled'|'disabled'
            },
            'CapacityReservationId': 'string',
            'CapacityReservationSpecification': {
                'CapacityReservationPreference': 'open'|'none',
                'CapacityReservationTarget': {
                    'CapacityReservationId': 'string',
                    'CapacityReservationResourceGroupArn': 'string'
                }
            },
            'HibernationOptions': {
                'Configured': True|False
            },
            'Licenses': [
                {
                    'LicenseConfigurationArn': 'string'
                },
            ],
            'MetadataOptions': {
                'State': 'pending'|'applied',
                'HttpTokens': 'optional'|'required',
                'HttpPutResponseHopLimit': 123,
                'HttpEndpoint': 'disabled'|'enabled',
                'HttpProtocolIpv6': 'disabled'|'enabled',
                'InstanceMetadataTags': 'disabled'|'enabled'
            },
            'EnclaveOptions': {
                'Enabled': True|False
            },
            'BootMode': 'legacy-bios'|'uefi'|'uefi-preferred',
            'PlatformDetails': 'string',
            'UsageOperation': 'string',
            'UsageOperationUpdateTime': datetime(2015, 1, 1),
            'PrivateDnsNameOptions': {
                'HostnameType': 'ip-name'|'resource-name',
                'EnableResourceNameDnsARecord': True|False,
                'EnableResourceNameDnsAAAARecord': True|False
            },
            'Ipv6Address': 'string',
            'TpmSupport': 'string',
            'MaintenanceOptions': {
                'AutoRecovery': 'disabled'|'default'
            },
            'CurrentInstanceBootMode': 'legacy-bios'|'uefi'
        },
    ],
    'OwnerId': 'string',
    'RequesterId': 'string',
    'ReservationId': 'string'
}