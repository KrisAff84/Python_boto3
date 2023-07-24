# This is copy and paste from boto3 documentation. Needs to be edited

import boto3


ec2 = boto3.client('ec2')

response = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': 'string',
            'VirtualName': 'string',
            'Ebs': {
                'DeleteOnTermination': True|False,
                'Iops': 123,
                'SnapshotId': 'string',
                'VolumeSize': 123,
                'VolumeType': 'standard'|'io1'|'io2'|'gp2'|'sc1'|'st1'|'gp3',
                'KmsKeyId': 'string',
                'Throughput': 123,
                'OutpostArn': 'string',
                'Encrypted': True|False
            },
            'NoDevice': 'string'
        },
    ],
    ImageId='string',
    InstanceType='t2.micro'
    Ipv6AddressCount=123,
    Ipv6Addresses=[
        {
            'Ipv6Address': 'string'
        },
    ],
    KernelId='string',
    KeyName='KrisKeyPair',
    MaxCount=123,
    MinCount=123,
    Monitoring={
        'Enabled': True|False
    },
    Placement={
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
    RamdiskId='string',
    SecurityGroupIds=[
        'string',
    ],
    SecurityGroups=[
        'string',
    ],
    SubnetId='string',
    UserData='string',
    AdditionalInfo='string',
    ClientToken='string',
    DisableApiTermination=True|False,
    DryRun=True|False,
    EbsOptimized=True|False,
    IamInstanceProfile={
        'Arn': 'string',
        'Name': 'string'
    },
    InstanceInitiatedShutdownBehavior='stop'|'terminate',
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True|False,
            'DeleteOnTermination': True|False,
            'Description': 'string',
            'DeviceIndex': 123,
            'Groups': [
                'string',
            ],
            'Ipv6AddressCount': 123,
            'Ipv6Addresses': [
                {
                    'Ipv6Address': 'string'
                },
            ],
            'NetworkInterfaceId': 'string',
            'PrivateIpAddress': 'string',
            'PrivateIpAddresses': [
                {
                    'Primary': True|False,
                    'PrivateIpAddress': 'string'
                },
            ],
            'SecondaryPrivateIpAddressCount': 123,
            'SubnetId': 'string',
            'AssociateCarrierIpAddress': True|False,
            'InterfaceType': 'string',
            'NetworkCardIndex': 123,
            'Ipv4Prefixes': [
                {
                    'Ipv4Prefix': 'string'
                },
            ],
            'Ipv4PrefixCount': 123,
            'Ipv6Prefixes': [
                {
                    'Ipv6Prefix': 'string'
                },
            ],
            'Ipv6PrefixCount': 123
        },
    ],
    PrivateIpAddress='string',
    ElasticGpuSpecification=[
        {
            'Type': 'string'
        },
    ],
    ElasticInferenceAccelerators=[
        {
            'Type': 'string',
            'Count': 123
        },
    ],
    TagSpecifications=[
        {
            'ResourceType': 'capacity-reservation'|'client-vpn-endpoint'|'customer-gateway'|'carrier-gateway'|'coip-pool'|'dedicated-host'|'dhcp-options'|'egress-only-internet-gateway'|'elastic-ip'|'elastic-gpu'|'export-image-task'|'export-instance-task'|'fleet'|'fpga-image'|'host-reservation'|'image'|'import-image-task'|'import-snapshot-task'|'instance'|'instance-event-window'|'internet-gateway'|'ipam'|'ipam-pool'|'ipam-scope'|'ipv4pool-ec2'|'ipv6pool-ec2'|'key-pair'|'launch-template'|'local-gateway'|'local-gateway-route-table'|'local-gateway-virtual-interface'|'local-gateway-virtual-interface-group'|'local-gateway-route-table-vpc-association'|'local-gateway-route-table-virtual-interface-group-association'|'natgateway'|'network-acl'|'network-interface'|'network-insights-analysis'|'network-insights-path'|'network-insights-access-scope'|'network-insights-access-scope-analysis'|'placement-group'|'prefix-list'|'replace-root-volume-task'|'reserved-instances'|'route-table'|'security-group'|'security-group-rule'|'snapshot'|'spot-fleet-request'|'spot-instances-request'|'subnet'|'subnet-cidr-reservation'|'traffic-mirror-filter'|'traffic-mirror-session'|'traffic-mirror-target'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-connect-peer'|'transit-gateway-multicast-domain'|'transit-gateway-policy-table'|'transit-gateway-route-table'|'transit-gateway-route-table-announcement'|'volume'|'vpc'|'vpc-endpoint'|'vpc-endpoint-connection'|'vpc-endpoint-service'|'vpc-endpoint-service-permission'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway'|'vpc-flow-log'|'capacity-reservation-fleet'|'traffic-mirror-filter-rule'|'vpc-endpoint-connection-device-type'|'verified-access-instance'|'verified-access-group'|'verified-access-endpoint'|'verified-access-policy'|'verified-access-trust-provider'|'vpn-connection-device-type'|'vpc-block-public-access-exclusion'|'ipam-resource-discovery'|'ipam-resource-discovery-association'|'instance-connect-endpoint',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    LaunchTemplate={
        'LaunchTemplateId': 'string',
        'LaunchTemplateName': 'string',
        'Version': 'string'
    },
    InstanceMarketOptions={
        'MarketType': 'spot',
        'SpotOptions': {
            'MaxPrice': 'string',
            'SpotInstanceType': 'one-time'|'persistent',
            'BlockDurationMinutes': 123,
            'ValidUntil': datetime(2015, 1, 1),
            'InstanceInterruptionBehavior': 'hibernate'|'stop'|'terminate'
        }
    },
    CreditSpecification={
        'CpuCredits': 'string'
    },
    CpuOptions={
        'CoreCount': 123,
        'ThreadsPerCore': 123,
        'AmdSevSnp': 'enabled'|'disabled'
    },
    CapacityReservationSpecification={
        'CapacityReservationPreference': 'open'|'none',
        'CapacityReservationTarget': {
            'CapacityReservationId': 'string',
            'CapacityReservationResourceGroupArn': 'string'
        }
    },
    HibernationOptions={
        'Configured': True|False
    },
    LicenseSpecifications=[
        {
            'LicenseConfigurationArn': 'string'
        },
    ],
    MetadataOptions={
        'HttpTokens': 'optional'|'required',
        'HttpPutResponseHopLimit': 123,
        'HttpEndpoint': 'disabled'|'enabled',
        'HttpProtocolIpv6': 'disabled'|'enabled',
        'InstanceMetadataTags': 'disabled'|'enabled'
    },
    EnclaveOptions={
        'Enabled': True|False
    },
    PrivateDnsNameOptions={
        'HostnameType': 'ip-name'|'resource-name',
        'EnableResourceNameDnsARecord': True|False,
        'EnableResourceNameDnsAAAARecord': True|False
    },
    MaintenanceOptions={
        'AutoRecovery': 'disabled'|'default'
    },
    DisableApiStop=True|False
)