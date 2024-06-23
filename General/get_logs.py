import json
import boto3


class Format:
    end = '\033[0m'
    blue_underline = '\033[34;4;1m'
    blue = '\033[34m'

def get_log_groups():
    response = cw_logs.describe_log_groups()
    return response['logGroups']


def get_log_streams(log_group, num_of_log_streams):
    response = cw_logs.describe_log_streams(
        logGroupName=log_group,
        orderBy='LastEventTime',
        descending=True,
        limit=num_of_log_streams)
    return response['logStreams']


def get_log_events(log_group, log_stream, num_of_events):
    response = cw_logs.get_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        startFromHead=True,
        limit=num_of_events)
    return response


def handle_python_error(message):
    format_spaces = message.replace('\u00a0', ' ')
    return format_spaces.split('\n')
   

def pretty_print_event(events):
    for event in events['events']:
        message = event['message']
        
        # Check if the message is a JSON object
        if isinstance(message, str):
            message = message.strip()
            if message.startswith('{') and message.endswith('}'):
                try:
                    parsed_message = json.loads(message)
                    event['message'] = parsed_message
                    continue
                except json.JSONDecodeError:
                    pass

            # Handle embedded JSON
            if 'Full event received:' in message:
                try:
                    json_start = message.index('{')
                    prefix = message[:json_start].strip()
                    embedded_json = message[json_start:]
                    parsed_message = json.loads(embedded_json)
                    event['message'] = {"prefix": prefix, "data": parsed_message}
                    continue
                except (json.JSONDecodeError, ValueError) as e:
                    print(f"Error parsing embedded JSON: {e}")
                    pass

            if 'Traceback' in message:
                event['message'] = handle_python_error(message)
                continue
        
        # Check if the message is tab-delimited
        if '\t' in message:
            parsed_message = {}
            for item in message.split('\t'):
                if ':' in item:
                    key, value = item.split(':', 1)
                    parsed_message[key.strip()] = value.strip()
                else:
                    parsed_message[item.strip()] = ''
            event['message'] = parsed_message
            continue
        
        # Fallback to original message if no parsing applied
        event['message'] = message

    return json.dumps(events, indent=2)

if __name__ == "__main__":

    profile, region = input(f"{Format.blue}\nAWS profile, Region: {Format.end}").split()
    session = boto3.Session(profile_name=profile, region_name=region)
    cw_logs = session.client('logs')

    # List log groups
    log_groups = get_log_groups()
    print(f"{Format.blue_underline}\nLog groups in {region}:{Format.end}\n")
    print(json.dumps(log_groups, indent=2))


    log_group = input(f"{Format.blue}\nLog group name: {Format.end}")
    num_of_log_streams = int(input(f"{Format.blue}Limit (Up to 50): {Format.end}"))
    log_streams = get_log_streams(log_group, num_of_log_streams)

    # list log streams in selected log group
    print(f"{Format.blue_underline}\nLog streams in {log_group} log group:{Format.end}\n")
    print(json.dumps(log_streams, indent=2))

    # Get log events in selected log stream
    log_stream = input(f"{Format.blue}\nLog stream name: {Format.end}")
    num_of_events = int(input(f"{Format.blue}Limit (Up to 10000): {Format.end}"))
    log_events = get_log_events(log_group, log_stream, num_of_events)
    # print(log_events)
    
    # Format log events and print
    formatted_log_events = pretty_print_event(log_events)
    print(f"{Format.blue_underline}\nLog events in {log_stream} log stream:{Format.end}\n")
    print(formatted_log_events)

    # Loop if user wants to view more log events
    view_more_log_events = input(f"{Format.blue}\nView more log events? (y/n): {Format.end}")
    while view_more_log_events == 'y':
        print(f"{Format.blue_underline}\nLog streams in {log_group} log group:{Format.end}\n")
        print(json.dumps(log_streams, indent=2))
        log_stream = input(f"{Format.blue}\nLog stream name: {Format.end}")
        num_of_events = int(input(f"{Format.blue}Limit: {Format.end}"))
        log_events = get_log_events(log_group, log_stream, num_of_events)
        formatted_log_events = pretty_print_event(log_events)
        print(f"{Format.blue_underline}\nLog events in {log_stream} log stream:{Format.end}\n")
        print(formatted_log_events)
        view_more_log_events = input(f"{Format.blue}\nView more log events? (y/n): {Format.end}")
    print("Exiting...")