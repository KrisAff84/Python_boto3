# For each role: Trust relationship policy, inline policies, attached permission policies, as well as any principles that can assume the role

import json
import boto3


class Format:
    end = '\033[0m'
    blue_underline = '\033[34;4;1m'
    blue = '\033[34m'


def get_role_permissions(role_name):
    role = iam.get_role(RoleName=role_name)
    inline = iam.list_role_policies(RoleName=role_name)
    attached_policies = iam.list_attached_role_policies(RoleName=role_name)

    if inline['PolicyNames']:
        inline_policies = []
        for policy in inline['PolicyNames']:
            policy = iam.get_role_policy(
                RoleName=role_name,
                PolicyName=policy
            )
            policy = {
                'PolicyName': policy['PolicyName'],
                'Document': policy['PolicyDocument']
            }
            inline_policies.append(policy)
        
        inline['PolicyNames'] = inline_policies
        
    if attached_policies['AttachedPolicies']:
        attached_policy_docs = []
        for policy in attached_policies['AttachedPolicies']:
            arn = policy['PolicyArn']
            default_version_id = iam.get_policy(PolicyArn=arn)['Policy']['DefaultVersionId']
            policy_doc = iam.get_policy_version(
                PolicyArn=arn,
                VersionId=default_version_id
            )['PolicyVersion']['Document']
            policy_with_doc = {
                'PolicyName': policy['PolicyName'],
                'PolicyArn': arn,
                'Document': policy_doc
            }
            attached_policy_docs.append(policy_with_doc)

        attached_policies['AttachedPolicies'] = attached_policy_docs

    response = {
        "Role": role['Role'],
        "InLinePolicies": inline['PolicyNames'] if inline['PolicyNames'] else None,
        "AttachedPolicies": attached_policies['AttachedPolicies'] if attached_policies['AttachedPolicies'] else None,
    }

    return json.dumps(response, indent=4, default=str)


if __name__ == "__main__":
    profile = input(f"{Format.blue}\nAWS profile:{Format.end} ")
    session = boto3.Session(profile_name=profile)
    iam = session.client('iam')
    view_roles = input(f"{Format.blue}\nWould you like to view existing roles? (y/n): {Format.end}")

    if view_roles == 'y':
        roles = iam.list_roles()
        print(f"{Format.blue_underline}\n{len(roles['Roles'])} Roles in account:{Format.end}\n")
        for role in roles['Roles']:
            print(role['RoleName'])
    else:
        pass

    role = input(f"{Format.blue}\nRole name: {Format.end}")
    print(get_role_permissions(role))

    more = input(f"{Format.blue}\nWould you like to get permissions for another role? (y/n): {Format.end}")
    while more == 'y':
        role = input(f"{Format.blue}\nRole name: {Format.end}")
        print(get_role_permissions(role))
        more = input(f"{Format.blue}\nWould you like to get permissions for another role? (y/n): {Format.end}")
    else:
        print(f"{Format.blue}\nExiting...{Format.end}")
        exit()
        