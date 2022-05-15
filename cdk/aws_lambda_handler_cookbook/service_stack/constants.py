SERVICE_ROLE_ARN = 'CookBookServiceRoleArn'
LAMBDA_BASIC_EXECUTION_ROLE = 'AWSLambdaBasicExecutionRole'
SERVICE_ROLE = 'CookBookServiceRole'

APIGATEWAY = 'Apigateway'
GW_RESOURCE = 'service'
LAMBDA_LAYER_NAME = 'common'
API_HANDLER_LAMBDA_MEMORY_SIZE = 128  # MB
API_HANDLER_LAMBDA_TIMEOUT = 10  # seconds
POWERTOOLS_SERVICE_NAME = 'POWERTOOLS_SERVICE_NAME'
SERVICE_NAME = 'CookBook'
METRICS_NAMESPACE = 'my_product_kpi'
POWERTOOLS_TRACE_DISABLED = 'POWERTOOLS_TRACE_DISABLED'
POWER_TOOLS_LOG_LEVEL = 'LOG_LEVEL'
BUILD_FOLDER = '.build/lambdas/'
COMMION_LAYER_BUILD_FOLDER = '.build/common_layer'
ENVIRONMENT = 'dev'
CONFIGURATION_NAME = 'my_conf'
CONFIGURATION_MAX_AGE_MINUTES = '5'  # time to store appconfig conf in the cache before refetching it


def get_stack_name() -> str:
    return 'cookbook'
