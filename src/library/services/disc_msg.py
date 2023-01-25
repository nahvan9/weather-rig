from library import utils

# Discord message formats

def time(value, *args, **kwargs):
    return f':clock1: Time: {value}'

def location(value, *args, **kwargs):
    return f':airplane: Location: {value}'

def temperature(value, unit='', *args, **kwargs):
    return f':thermometer: Temperature: {value} {unit}'

def tempBounds(value, unit='', *args, **kwargs):
    return f':left_right_arrow: Temperature Bounds: {value} {unit}'

def rtn(value, *args, **kwargs):
    return f':white_check_mark: Return Val: {value}'

def status(value, *args, **kwargs):
    return f':hourglass: Status: {value}'

def pid(value, *args, **kwargs):
    return f':tools: Process ID: {value}'

def machine(value, *args, **kwargs):
    return f':desktop: Worker name: {value}'

def chkInterval(value, *args, **kwargs):
    return f':timer: Next status check in {utils.HrMinSec(value)}'

# get function names
labelConversions = {
    'Time': 'time',
    'Location': 'location',
    'Temperature': 'temperature',
    'Temperature Bounds': 'tempBounds',
    'Return': 'rtn',
    'Status': 'status',
    'Process ID': 'pid',
    'Worker Name': 'machine',
    'Check Interval': 'chkInterval',
}